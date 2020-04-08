## Installing the application
If you don't have python on your machine, download Python 3.7. https://www.python.org/downloads/release/python-377/

Install jupyterlab to be able to run the notebook. https://jupyter.org/install
```bash
pip install jupyterlab
```

Install the project dependencies.
```bash
pip install requirements.txt -r
```

## Running the application

```bash
jupyter notebook '.\Control System GUI.ipynb'
```

## Runing Individual Scripts
```bash
python ./transfer_function.py
```

```bash
python ./animate.py
```

## Project Overview
- constants.py => where you can find the inputs for the project
- transfer_function.py => where you can find the information for controls
- animate.py => where you can find the functions used to animate
- Control System GUI.ipync => Jupyter Notebook for running the GUI/Animation