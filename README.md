# AI programming with Python nanodegree

## Projects

### Project 1 — Pet Image Classifier

Classify pet images using three pretrained CNN architectures (ResNet-18, AlexNet, VGG-16) and evaluate which model best identifies dog breeds vs. non-dogs. The true pet label is extracted from each image's filename and compared against the classifier's prediction. Statistics (% correct dogs, % correct breeds, % correct non-dogs) are computed to benchmark each model.

- **Technologies:** Python 3, PyTorch, torchvision, PIL/Pillow, argparse
- **Location:** `1-Introduction_to_Python_to_AI_programmers/8-Classify_pet_image_project/`

### Project 2 — Flower Image Classifier (Final Project)

Build and train a deep neural network to recognize 102 flower species using transfer learning (VGG-16/VGG-13). Developed first as a Jupyter notebook, then converted into two command-line applications: one for training (`train.py`) and one for inference (`predict.py`).

- **Technologies:** Python 3, PyTorch, torchvision, NumPy, PIL/Pillow, matplotlib, Jupyter Notebook, GPU/CUDA support
- **Location:** `11-Final_project/`

## PEP 8 Guidelines

- Follow the official style guide for Python code: https://peps.python.org/pep-0008/
- Keep lines to 79 characters (72 for docstrings) and use consistent 4-space indentation.
- Name modules, functions, and variables in `lower_snake_case`; classes in `CapWords`.
- Write clear docstrings and inline comments where needed; avoid redundant comments.
- Separate top-level definitions with two blank lines and related code blocks with a single blank line.
- Order imports as standard library, third-party, then local modules, each grouped and alphabetized.

## Python standard library

https://docs.python.org/3.6/library/index.html

## To activate the environment:

```bash
python3 -m venv .venv
pip freeze > requirements.txt
pip install -r requirements.txt
source .venv/bin/activate
deactivate
```

## To get the requirements and install from it:

```bash
pip freeze > requirements.txt
pip install -r requirements.txt
```

## Conda's installation commands

```bash
conda create -n course_2 python=3
conda activate course_2
conda list
conda env list
conda install numpy pandas matplotlib

conda update --all
conda upgrade --all
conda env export > environment.yaml
conda env create -f environment.yaml
conda env remove -n env_name

conda deactivate
```

[Conda Command reference guide](https://docs.conda.io/projects/conda/en/latest/commands/index.html)

## To start Jupyter notebook:

```bash
jupyter notebook
```

[Jupyter documentation](https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/examples_index.html)

## Numpy:

[Numpy official user guide](https://numpy.org/doc/stable/user/index.html)

## Pandas:

[Pandas official user guide](https://pandas.pydata.org/pandas-docs/stable/)

## Sample plots in Matplotlib

https://matplotlib.org/3.3.1/tutorials/introductory/sample_plots.html#sphx-glr-tutorials-introductory-sample-plots-py

## Sample plots in Seaborn

https://seaborn.pydata.org/examples/index.html
