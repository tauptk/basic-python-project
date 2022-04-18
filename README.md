# A sample Python project

An example repository describing, how simple Python application is structured and what are auxiliary files
required to keep project clean

## Installation

To install the application, simply run

```commandline
pip install .
```

## Installation (dev)

A poetry is required. You can get it [here](https://python-poetry.org)

Once poetry is installed, activate a new virtual environment with

```commandline
poetry shell
```

To install all required dependencies, run the following command

```commandline
poetry install
```

## Running the application

To start the application, execute the following command:

```commandline
export FLASK_APP=basic_python_project/app.py
flask run
```

Application also supports custom command-line interface:
```commandline
flask hello
```
