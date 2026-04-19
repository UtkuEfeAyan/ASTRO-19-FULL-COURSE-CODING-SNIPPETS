# ASTRO-19-FULL-COURSE-CODING-SNIPPETS

## Setting Up the Virtual Environment Tutoriol For When I Forget
### Activate the Virtual Environment
On macOS
```bash
source bin/activate
```
### Install Packages
With the virtual environment activated, install packages using pip3:
```bash
pip3 install numpy ipykernel pandas scipy astropy plotly
```
For a specific version:
```bash
pip3 install numpy==2.4.4
```
### Deactivate the Virtual Environment

When done, deactivate it:
```bash
deactivate
```
### Running Python Scripts
Always make sure the virtual environment is activated before running scripts or installing packages:
```bash
source bin/activate
python session6prompt.py
```

## Available Packages

## Available Packages

This environment includes:
- `numpy` — numerical computing
- `scipy` — scientific computing
- `pandas` — data analysis
- `astropy` — astronomy library
- `plotly` — interactive visualizations
- `ipykernel` — Jupyter kernel support
- `jupyter_client` — Jupyter protocol client
- `jupyter_core` — Jupyter core utilities
- `IPython` — interactive Python shell
- `debugpy` — Python debugger

**Python Version:** 3.14.3 (macOS ARM64)