# AI Programming with Python — Final Project

Project code for Udacity's AI Programming with Python Nanodegree program.  
In this project, an image classifier is built with PyTorch to recognize **102 flower species**, first as a Jupyter notebook and then as a pair of command-line applications.

## Project Structure

```
├── Image Classifier Project.ipynb   # Development notebook (Part 1)
├── train.py                         # CLI training script (Part 2)
├── predict.py                       # CLI prediction script (Part 2)
├── cat_to_name.json                 # Mapping of category labels → flower names
├── flowers/                         # Dataset (train / valid / test splits)
├── project_requirements.md          # Rubric / requirements
└── assets/                          # Supporting assets
```

## Prerequisites

- Python 3.8+
- PyTorch, torchvision
- NumPy, Pillow, matplotlib
- (Optional) A CUDA-capable GPU for faster training

Install dependencies (example with conda):

```bash
conda activate <environment_name>
conda install pytorch torchvision numpy pillow matplotlib -c pytorch
```

## Part 1 — Jupyter Notebook

Open and run all cells in **Image Classifier Project.ipynb**.  
The notebook walks through data loading, model building, training, testing, checkpoint saving/loading, and inference with visualization.

```bash
jupyter notebook "Image Classifier Project.ipynb"
```

## Part 2 — Command-Line Application

### Training (`train.py`)

Train a new network on the flower dataset and save a checkpoint.

**Basic usage:**

```bash
python train.py flowers
```

**All options:**

| Argument                | Default | Description                                                              |
| ----------------------- | ------- | ------------------------------------------------------------------------ |
| `data_dir` (positional) | —       | Path to the dataset directory (must contain `train/`, `valid/`, `test/`) |
| `--save_dir`            | `.`     | Directory to save the checkpoint                                         |
| `--arch`                | `vgg16` | Model architecture: `vgg16` or `vgg13`                                   |
| `--learning_rate`       | `0.001` | Learning rate for the Adam optimizer                                     |
| `--hidden_units`        | `4096`  | Number of units in the first hidden layer                                |
| `--epochs`              | `5`     | Number of training epochs                                                |
| `--gpu`                 | off     | Use GPU for training                                                     |

**Examples:**

```bash
# Train VGG-13 for 10 epochs on GPU, save to checkpoints/
python train.py flowers --arch vgg13 --epochs 10 --gpu --save_dir checkpoints

# Train with a smaller hidden layer and lower learning rate
python train.py flowers --hidden_units 2048 --learning_rate 0.0005 --gpu
```

The checkpoint is saved as `checkpoint.pth` inside the specified `--save_dir`.

### Prediction (`predict.py`)

Predict the flower name from an image using a saved checkpoint.

**Basic usage:**

```bash
python predict.py flowers/test/1/image_06743.jpg checkpoint.pth
```

**All options:**

| Argument                  | Default | Description                                          |
| ------------------------- | ------- | ---------------------------------------------------- |
| `image_path` (positional) | —       | Path to the image file                               |
| `checkpoint` (positional) | —       | Path to the model checkpoint (`.pth`)                |
| `--top_k`                 | `5`     | Return top K most likely classes                     |
| `--category_names`        | `None`  | Path to a JSON file mapping categories to real names |
| `--gpu`                   | off     | Use GPU for inference                                |

**Examples:**

```bash
# Predict top 3 classes with flower names, using GPU
python predict.py flowers/test/1/image_06743.jpg checkpoint.pth \
    --top_k 3 --category_names cat_to_name.json --gpu

# Quick prediction with defaults
python predict.py flowers/test/5/image_05159.jpg checkpoint.pth
```

## Model Architecture

The classifier uses a **VGG** backbone (VGG-16 or VGG-13) pre-trained on ImageNet with its feature layers frozen. The default custom classifier head is:

```
Linear(25088 → 4096) → ReLU → Dropout(0.2)
    → Linear(4096 → 512) → ReLU → Dropout(0.2)
    → Linear(512 → 102) → LogSoftmax
```

Training uses **NLLLoss** with the **Adam** optimizer.

## Dataset

The [102 Category Flower Dataset](https://www.robots.ox.ac.uk/~vgg/data/flowers/102/) is expected under `flowers/` with the following structure:

```
flowers/
├── train/     # Training images (one subfolder per class)
├── valid/     # Validation images
└── test/      # Test images
```

`cat_to_name.json` maps the class folder names (e.g. `"1"`, `"2"`, …) to human-readable flower names.
