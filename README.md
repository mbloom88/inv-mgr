# Inventory Manager

This project is based off of the Udemy course [Build Real Software with Python, PyQt5 and QT Designer](https://www.udemy.com/course/python-pyqt5/).

A course [Python GUI Programming Recipes using PyQt5](https://www.udemy.com/course/python-gui-programming-recipes-using-pyqt5/). was also used in support of this project.

Created in a Windows 10 environment. 

## Prerequisites

Required
1. [Python 3.8.3](https://www.python.org/downloads/release/python-383/)

Optional
1. [DB Browser for SQLite, v3.12.1](https://sqlitebrowser.org/)
	- Used for SQLite3 database generation.
	- Needed if additional databases will be generated.

## Installation

1. Clone the repo to a directory on the target machine.
1. Create a new virtual environment: 
	1. Navigate to a directory outside of the cloned repo `inv-mgr`.
	1. Enter `py -m venv <my-venv>`, where `<my-venv>` is the desired name for the new virtual environment.
1. Activate the virtual environment:
	1. Make sure you are in the same directory where `<my-venv>` was created.
	1. For Windows: Enter `.\<my-venv>\Scripts\activate`
	1. For Linux or macOS: `source <my-venv>/bin/activate`
1. Navigate to the `inv-mgr/` directory and enter `py setup.py install` to install supporting Python packages.

## Project Directory

```
.
├───inv_mgr: inventory manager script directory
│   ├───db: sqlite3 .db files
│   └───ui: Qt designer .ui files
├───README.md: this document
└───setup.py: setuptools installation script
```

## Development

### Python Files and Scripts

Prior to generating or running a script, activate the virtual environment. See Installation instructions for details. `deactivate` can be entered when the package is no longer in use (works for all OS). 

To run a script, enter `py <script_name>.py` in the command terminal.

New `.py` Python files are to be saved in the `inv-mgr/inv_mgr/` directory.

### QT Designer GUIs

QT Designer is used to create .ui files for the project GUI. The executable is located in the virtual environment at `Lib/site-packages/qt5_applications/Qt/bin/designer.exe`.

New `.ui` QT Designer files are to be saved in the `inv-mgr/inv_mgr/ui/` directory.

### SQLite3 Databases

New databases can be generated using the DB Browser for SQLite tool. 

New `.db` database files are to be saved in the `inv-mgr/inv_mgr/db/` directory.
