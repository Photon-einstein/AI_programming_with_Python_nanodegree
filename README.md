# AI programming with Python nanodegree

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
