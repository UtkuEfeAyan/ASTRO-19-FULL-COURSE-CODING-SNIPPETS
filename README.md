# ASTRO-19-FULL-COURSE-CODING-SNIPPETS
## Setting Up the Virtual Environment,,, Tutoriol For When I Forget
### Activate the Virtual Environment macOS
```bash
source bin/activate
```
### Install Packages
after virtual environment activated, install packages using pip3
```bash
pip3 install numpy 
```
for specific version
```bash
pip3 install numpy==2.4.4
```
### Deactivate the Virtual Environment

when done deactivate it
```bash
deactivate
```
### Running Python Scripts
always make sure that the virtual environment is activated before running scripts or installing packages or oyu will confuse yourself
```bash
source bin/activate
python session6prompt.py
```
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
- `matplotlib` - creating visualizations in Python
Python Version: 3.14.3 (macOS ARM64)

### activate jupyter lab
WRITE AFTER ACTIVATING SOURCE BIN 
- jupyter lab
jupyter notebook command don't work so us the above command jupyter lab 
also if you are testing something in vs code us th default kernel that inside the vscode one (github) are not the web based one because teh web based one requires you to re download the packages