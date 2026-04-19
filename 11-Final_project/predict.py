import argparse
import json
import os
import torch
import torch.nn as nn
import numpy as np
from PIL import Image
from torchvision import models
from collections import OrderedDict


def get_input_args():
    """Parse command line arguments for prediction.

    Args:
        None (reads from sys.argv).

    Returns:
        argparse.Namespace: Parsed arguments with attributes:
            - image_path (str): Path to the image file.
            - checkpoint (str): Path to the model checkpoint.
            - top_k (int): Number of top K most likely classes to return.
            - category_names (str or None): Path to a JSON file mapping categories to names.
            - gpu (bool): Whether to use GPU for inference.
    """
    parser = argparse.ArgumentParser(description="Predict flower name from an image.")
    parser.add_argument('image_path', type=str, help='Path to the image file')
    parser.add_argument('checkpoint', type=str, help='Path to the model checkpoint')
    parser.add_argument('--top_k', type=int, default=5, help='Return top K most likely classes (default: 5)')
    parser.add_argument('--category_names', type=str, default=None,
                        help='Path to a JSON file mapping categories to real names')
    parser.add_argument('--gpu', action='store_true', help='Use GPU for inference')
    return parser.parse_args()


def load_checkpoint(filepath: str) -> models.VGG:
    """Load a model checkpoint and rebuild the model.

    Args:
        filepath (str): Path to the saved checkpoint file (.pth).

    Returns:
        models.VGG: The rebuilt model with trained weights and class_to_idx mapping.

    Raises:
        ValueError: If filepath is None or empty.
        FileNotFoundError: If the checkpoint file does not exist.
    """
    if not filepath:
        raise ValueError("filepath must be a non-empty string.")
    if not os.path.isfile(filepath):
        raise FileNotFoundError(f"Checkpoint file not found: {filepath}")

    checkpoint = torch.load(filepath, map_location='cpu')

    arch = checkpoint.get('arch', 'vgg16')
    if arch == 'vgg16':
        model = models.vgg16(pretrained=True)
    elif arch == 'vgg13':
        model = models.vgg13(pretrained=True)
    else:
        raise ValueError(f"Unsupported architecture: {arch}")

    for param in model.parameters():
        param.requires_grad = False

    model.classifier = checkpoint['classifier']
    model.load_state_dict(checkpoint['state_dict'])
    model.class_to_idx = checkpoint['class_to_idx']

    return model


def process_image(image_path: str) -> np.ndarray:
    """Scales, crops, and normalizes a PIL image for a PyTorch model.

    Args:
        image_path (str): Path to the image file.

    Returns:
        np.ndarray: Processed image as a numpy array with shape (3, 224, 224).

    Raises:
        ValueError: If image path is None or empty.
        FileNotFoundError: If the image file does not exist.
    """
    if not image_path:
        raise ValueError("image path must be a non-empty string.")
    if not os.path.isfile(image_path):
        raise FileNotFoundError(f"Image file not found: {image_path}")

    pil_image = Image.open(image_path)

    # Resize keeping aspect ratio, shortest side = 256
    width, height = pil_image.size
    if width < height:
        pil_image = pil_image.resize((256, int(256 * height / width)))
    else:
        pil_image = pil_image.resize((int(256 * width / height), 256))

    # Center crop to 224x224
    width, height = pil_image.size
    left = (width - 224) / 2
    top = (height - 224) / 2
    right = left + 224
    bottom = top + 224
    pil_image = pil_image.crop((left, top, right, bottom))

    # Convert to numpy array and normalize to 0-1
    np_image = np.array(pil_image) / 255.0

    # Normalize with ImageNet mean and std
    mean = np.array([0.485, 0.456, 0.406])
    std = np.array([0.229, 0.224, 0.225])
    np_image = (np_image - mean) / std

    # Transpose from (H, W, C) to (C, H, W)
    np_image = np_image.transpose((2, 0, 1))

    return np_image


def predict(image_path: str, model, topk: int, device) -> tuple:
    """Predict the class (or classes) of an image using a trained model.

    Args:
        image_path (str): Path to the image file.
        model: Trained model with class_to_idx attribute.
        topk (int): Number of top predictions to return.
        device: torch.device for computation.

    Returns:
        tuple: (probs, classes) - lists of top-k probabilities and class labels.

    Raises:
        ValueError: If image_path is None or empty, topk < 1, or model lacks class_to_idx.
        FileNotFoundError: If the image file does not exist.
        TypeError: If topk is not an integer.
    """
    if not image_path:
        raise ValueError("image_path must be a non-empty string.")
    if not os.path.isfile(image_path):
        raise FileNotFoundError(f"Image file not found: {image_path}")
    if not isinstance(topk, int):
        raise TypeError(f"topk must be an integer, got {type(topk).__name__}.")
    if topk < 1:
        raise ValueError(f"topk must be at least 1, got {topk}.")
    if not hasattr(model, 'class_to_idx'):
        raise ValueError("Model does not have a class_to_idx attribute. "
                         "Load the model from a checkpoint that includes class_to_idx.")

    model.eval()
    model.to(device)

    np_image = process_image(image_path)
    tensor_image = torch.from_numpy(np_image).type(torch.FloatTensor)
    tensor_image = tensor_image.unsqueeze(0).to(device)

    with torch.no_grad():
        logps = model(tensor_image)

    ps = torch.exp(logps)
    top_p, top_idx = ps.topk(topk, dim=1)

    top_p = top_p.cpu().numpy().squeeze().tolist()
    top_idx = top_idx.cpu().numpy().squeeze().tolist()

    # Handle single result (topk=1) where squeeze returns a scalar
    if not isinstance(top_p, list):
        top_p = [top_p]
        top_idx = [top_idx]

    idx_to_class = {val: key for key, val in model.class_to_idx.items()}
    top_classes = [idx_to_class[idx] for idx in top_idx]

    return top_p, top_classes


def main():
    """Main entry point for the prediction script.

    Parses CLI arguments, loads a trained model checkpoint, runs inference
    on the given image, and prints the top-K predicted classes with their
    probabilities.
    """
    args = get_input_args()

    # Set device
    if args.gpu and torch.cuda.is_available():
        device = torch.device("cuda")
    else:
        device = torch.device("cpu")
        if args.gpu:
            print("GPU not available, using CPU.")

    # Load model
    model = load_checkpoint(args.checkpoint)

    # Predict
    probs, classes = predict(args.image_path, model, args.top_k, device)

    # Load category names if provided
    if args.category_names:
        with open(args.category_names, 'r') as f:
            cat_to_name = json.load(f)
        names = [cat_to_name.get(cls, cls) for cls in classes]
    else:
        names = classes

    # Print results
    print("\nPrediction Results:")
    print("-" * 40)
    for i in range(len(names)):
        print(f"  {names[i]:30s} {probs[i]:.4f}")


if __name__ == '__main__':
    main()
