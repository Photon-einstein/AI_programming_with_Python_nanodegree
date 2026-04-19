import argparse
import os
import torch
import torch.nn as nn
from torch.optim import Adam
from torchvision import datasets, transforms, models
from collections import OrderedDict


def get_input_args():
    """Parse command line arguments for training.

    Args:
        None (reads from sys.argv).

    Returns:
        argparse.Namespace: Parsed arguments with attributes:
            - data_dir (str): Path to the dataset directory.
            - save_dir (str): Directory to save the checkpoint.
            - arch (str): Model architecture ('vgg16' or 'vgg13').
            - learning_rate (float): Learning rate for optimizer.
            - hidden_units (int): Number of hidden units in the first hidden layer.
            - epochs (int): Number of training epochs.
            - gpu (bool): Whether to use GPU for training.
    """
    parser = argparse.ArgumentParser(description="Train a neural network on an image dataset.")
    parser.add_argument('data_dir', type=str, help='Path to the dataset directory (e.g. flowers)')
    parser.add_argument('--save_dir', type=str, default='.', help='Directory to save the checkpoint')
    parser.add_argument('--arch', type=str, default='vgg16', choices=['vgg16', 'vgg13'],
                        help='Model architecture: vgg16 or vgg13 (default: vgg16)')
    parser.add_argument('--learning_rate', type=float, default=0.001, help='Learning rate (default: 0.001)')
    parser.add_argument('--hidden_units', type=int, default=4096, help='Number of hidden units (default: 4096)')
    parser.add_argument('--epochs', type=int, default=5, help='Number of training epochs (default: 5)')
    parser.add_argument('--gpu', action='store_true', help='Use GPU for training')
    return parser.parse_args()


def load_data(data_dir: str) -> tuple:
    """Load and transform the training, validation, and test datasets.

    Args:
        data_dir (str): Root directory containing train/, valid/, test/ subdirectories.

    Returns:
        tuple: (dataloaders dict, image_datasets dict) where each dict has
            'train', 'valid', and 'test' keys.

    Raises:
        ValueError: If data_dir is None or empty.
        FileNotFoundError: If data_dir or any required subdirectory does not exist.
    """
    if not data_dir:
        raise ValueError("data_dir must be a non-empty string.")
    if not os.path.isdir(data_dir):
        raise FileNotFoundError(f"Data directory not found: {data_dir}")

    train_dir = os.path.join(data_dir, 'train')
    valid_dir = os.path.join(data_dir, 'valid')
    test_dir = os.path.join(data_dir, 'test')

    for subdir, name in [(train_dir, 'train'), (valid_dir, 'valid'), (test_dir, 'test')]:
        if not os.path.isdir(subdir):
            raise FileNotFoundError(f"Required '{name}' subdirectory not found: {subdir}")

    data_transforms = {
        'train': transforms.Compose([
            transforms.RandomRotation(30),
            transforms.RandomResizedCrop(224),
            transforms.RandomHorizontalFlip(),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
        ]),
        'valid': transforms.Compose([
            transforms.Resize(255),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
        ]),
        'test': transforms.Compose([
            transforms.Resize(255),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
        ]),
    }

    image_datasets = {
        'train': datasets.ImageFolder(train_dir, transform=data_transforms['train']),
        'valid': datasets.ImageFolder(valid_dir, transform=data_transforms['valid']),
        'test': datasets.ImageFolder(test_dir, transform=data_transforms['test']),
    }

    dataloaders = {
        'train': torch.utils.data.DataLoader(image_datasets['train'], batch_size=64, shuffle=True),
        'valid': torch.utils.data.DataLoader(image_datasets['valid'], batch_size=64),
        'test': torch.utils.data.DataLoader(image_datasets['test'], batch_size=64),
    }

    return dataloaders, image_datasets


def build_model(arch: str, hidden_units: int) -> tuple:
    """Build a pretrained model with a custom classifier.

    Args:
        arch (str): Architecture name ('vgg16' or 'vgg13').
        hidden_units (int): Number of units in the first hidden layer.

    Returns:
        tuple: (model, in_features) where in_features is the classifier input size.

    Raises:
        ValueError: If arch is not supported or hidden_units is not positive.
        TypeError: If hidden_units is not an integer.
    """
    if arch not in ('vgg16', 'vgg13'):
        raise ValueError(f"Unsupported architecture: {arch}. Choose 'vgg16' or 'vgg13'.")
    if not isinstance(hidden_units, int):
        raise TypeError(f"hidden_units must be an integer, got {type(hidden_units).__name__}.")
    if hidden_units < 1:
        raise ValueError(f"hidden_units must be positive, got {hidden_units}.")

    if arch == 'vgg16':
        model = models.vgg16(pretrained=True)
    elif arch == 'vgg13':
        model = models.vgg13(pretrained=True)

    in_features = model.classifier[0].in_features

    for param in model.parameters():
        param.requires_grad = False

    classifier = nn.Sequential(OrderedDict([
        ('fc1', nn.Linear(in_features, hidden_units)),
        ('relu1', nn.ReLU()),
        ('dropout1', nn.Dropout(0.2)),
        ('fc2', nn.Linear(hidden_units, 512)),
        ('relu2', nn.ReLU()),
        ('dropout2', nn.Dropout(0.2)),
        ('fc3', nn.Linear(512, 102)),
        ('output', nn.LogSoftmax(dim=1))
    ]))

    model.classifier = classifier
    return model, in_features


def train_model(model, dataloaders: dict, criterion, optimizer, epochs: int, device) -> None:
    """Train the model and print training/validation loss and accuracy.

    Args:
        model: The neural network model.
        dataloaders (dict): Dictionary with 'train' and 'valid' DataLoaders.
        criterion: Loss function.
        optimizer: Optimizer.
        epochs (int): Number of training epochs.
        device: torch.device for computation.

    Raises:
        ValueError: If epochs < 1 or dataloaders is missing required keys.
        TypeError: If epochs is not an integer.
    """
    if not isinstance(epochs, int):
        raise TypeError(f"epochs must be an integer, got {type(epochs).__name__}.")
    if epochs < 1:
        raise ValueError(f"epochs must be at least 1, got {epochs}.")
    for key in ('train', 'valid'):
        if key not in dataloaders:
            raise ValueError(f"dataloaders dict is missing required key: '{key}'.")

    print_every = 20
    steps = 0

    model.to(device)

    for epoch in range(epochs):
        running_loss = 0
        model.train()

        for inputs, labels in dataloaders['train']:
            steps += 1
            inputs, labels = inputs.to(device), labels.to(device)

            optimizer.zero_grad()

            logps = model(inputs)
            loss = criterion(logps, labels)
            loss.backward()
            optimizer.step()

            running_loss += loss.item()

            if steps % print_every == 0:
                model.eval()
                valid_loss = 0
                accuracy = 0

                with torch.no_grad():
                    for inputs, labels in dataloaders['valid']:
                        inputs, labels = inputs.to(device), labels.to(device)
                        logps = model(inputs)
                        batch_loss = criterion(logps, labels)
                        valid_loss += batch_loss.item()

                        ps = torch.exp(logps)
                        top_p, top_class = ps.topk(1, dim=1)
                        equals = top_class == labels.view(*top_class.shape)
                        accuracy += torch.mean(equals.type(torch.FloatTensor)).item()

                print(f"Epoch {epoch+1}/{epochs}.. "
                      f"Train loss: {running_loss/print_every:.3f}.. "
                      f"Validation loss: {valid_loss/len(dataloaders['valid']):.3f}.. "
                      f"Validation accuracy: {accuracy/len(dataloaders['valid']):.3f}")

                running_loss = 0
                model.train()


def save_checkpoint(model, image_datasets: dict, arch: str, hidden_units: int,
                    epochs: int, optimizer, save_dir: str) -> None:
    """Save the trained model checkpoint.

    Args:
        model: Trained model.
        image_datasets (dict): Image datasets with class_to_idx mapping.
        arch (str): Architecture name.
        hidden_units (int): Number of hidden units.
        epochs (int): Number of training epochs.
        optimizer: Optimizer with state_dict.
        save_dir (str): Directory to save the checkpoint file.

    Raises:
        ValueError: If save_dir is None or empty, or arch is unsupported.
    """
    if not save_dir:
        raise ValueError("save_dir must be a non-empty string.")

    model.class_to_idx = image_datasets['train'].class_to_idx

    checkpoint = {
        'arch': arch,
        'hidden_units': hidden_units,
        'class_to_idx': model.class_to_idx,
        'classifier': model.classifier,
        'state_dict': model.state_dict(),
        'optimizer_state_dict': optimizer.state_dict(),
        'epochs': epochs,
    }

    os.makedirs(save_dir, exist_ok=True)
    filepath = os.path.join(save_dir, 'checkpoint.pth')
    torch.save(checkpoint, filepath)
    print(f"Checkpoint saved to {filepath}")


def main():
    """Main entry point for the training script.

    Parses CLI arguments, loads data, builds the model, trains it,
    and saves a checkpoint.
    """
    args = get_input_args()

    # Set device
    if args.gpu and torch.cuda.is_available():
        device = torch.device("cuda")
        print("Training on GPU.")
    else:
        device = torch.device("cpu")
        if args.gpu:
            print("GPU not available, using CPU.")
        else:
            print("Training on CPU.")

    # Load data
    dataloaders, image_datasets = load_data(args.data_dir)

    # Build model
    model, in_features = build_model(args.arch, args.hidden_units)

    # Define loss and optimizer
    criterion = nn.NLLLoss()
    optimizer = Adam(model.classifier.parameters(), lr=args.learning_rate)

    # Train
    train_model(model, dataloaders, criterion, optimizer, args.epochs, device)

    # Save checkpoint
    save_checkpoint(model, image_datasets, args.arch, args.hidden_units, args.epochs, optimizer, args.save_dir)


if __name__ == '__main__':
    main()
