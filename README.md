# Inventory Manager

A project based off of the Udemy course [Build Real Software with Python, PyQt5 and QT Designer](https://www.udemy.com/course/python-pyqt5/). The project focuses on the creation of a mechanical fastener/parts inventory manager GUI that uses an SQLite3 database.

The course [Python GUI Programming Recipes using PyQt5](https://www.udemy.com/course/python-gui-programming-recipes-using-pyqt5/) was also used in support of this project.

## Program Execution

1. Download the latest executable ZIP file from [Releases](https://github.com/mbloom88/inv-mgr/releases).
1. Un-zip `inv_mgr.zip`. 
1. Open the new `inv_mgr/` directory and run `inv_mgr.exe`.

## Development

### Prerequisites

Required
1. [Python 3.8.3](https://www.python.org/downloads/release/python-383/)
1. [DB Browser for SQLite, v3.12.1](https://sqlitebrowser.org/)
	- Used for SQLite3 database generation.
	- Needed if additional databases will be generated.

Optional
1. [Dark Orange Stylesheet for Qt Designer](https://github.com/sommerc/pyqt-stylesheets/blob/master/pyqtcss/src/dark_orange/style.qss)
	- Gives the Qt Designer GUI a slick look using stylesheets.
1. [Wrench Image](https://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/Wrench_font_awesome.svg/512px-Wrench_font_awesome.svg.png)
	- Used as a fake logo for the GUI.
	- Also used for icon creation.
1. [PNG Resizer](https://onlinepngtools.com/resize-png)
	- Resizes PNG images.
1. [ICO Convert](https://icoconvert.com/)
	- Converts .png images to .ico format for icons.

### Installation

1. Clone the repo to a directory on the target machine.
1. Create a new virtual environment: 
	1. Navigate to a directory outside of the cloned repo.
	1. Enter `python -m venv <my-venv>`, where `<my-venv>` is the desired name for the new virtual environment.
1. Activate the virtual environment:
	1. Make sure you are in the same directory where `<my-venv>` was created.
	1. For Windows: Enter `.\<my-venv>\Scripts\activate`
	1. For Linux or macOS: `source <my-venv>/bin/activate`
1. Navigate to the cloned repo directory and enter `python setup.py install` to install supporting Python packages.

### Project Directory

```
.
├───sandbox: For development and testing purposes only
│	├───db: sqlite3 .db files
│	└───ui: Qt designer .ui files
├───src: source code and resource directory
│   ├───db: sqlite3 .db files
│   └───ui: Qt designer .ui files
├───CHANGELOG.md: project changelog
├───README.md: this document
└───setup.py: Python setuptools installation script
```

### Python Files and Scripts

Prior to generating or running a script, activate the virtual environment. See Installation instructions for details. `deactivate` can be entered when the package is no longer in use (works for all OS). 

The main script of the project is `inv_mgr.py`.

New and supporting script files are to be saved in the `inv-mgr/src/` directory.

### QT Designer GUIs

#### GUI Creation
QT Designer is used to create `.ui` files for the project GUI. The executable is located in the virtual environment at `Lib/site-packages/qt5_applications/Qt/bin/designer.exe`.

New `.ui` QT Designer files are to be saved in the `inv-mgr/src/ui/` directory.

All `.ui` files must be converted to a `.py` file prior to use. To create a `.py` files from a `.ui` file:

1. Navigate to the `inv-mgr/src/ui/` directory.
1. Enter the following command: `pyuic5 -x -o <designer_ui.py> <designer_uo.ui>`
	- `<designer_ui.py>` is the desired `.py` file to create.
	- `<designer_uo.ui>` is the target `.ui` file.

#### Resource Files and Images

Images can be placed onto the GUI using `QLabel` widgets with their text fields cleared. 

Before placing a PNG, a `.qrc` resource file holding the image must be created and saved to the `img-mgr/src/ui/` directory. Once created, the resource file can be added to the `Qlabel` field `pixmap`.

To work within the Python environment, the `.qrc` must be converted to a `.py`, and then the `.py` must be imported into the target Python scripts. To do this:

1.	Enter the command: `pyrcc5 -o <my_resource>_rc.py <my_resource>.qrc`.
	- `<my_resource>` is the name of the resource file. 
	- The `_rc` tag signifies that the Python file is derived from a resource file.
1. Open the `.ui` file that the resource file is used in. 
1. Search for the line `import <my_resource>_rc` and comment it out.
1. Copy the import statement from the previous step and add it to the target Python script(s). **IF THIS STEP IS NOT COMPLETED, COMPILING ISSUES WILL OCCUR.**

### SQLite3 Databases

New databases can be generated using the DB Browser for SQLite tool. 

New `.db` database files are to be saved in the `inv-mgr/src/db/` directory.

### Executable Creation

The project can be turned into an executable by performing the following steps:

1. Navigate to the `<my-venv>/Scripts/` virtual environment directory.
1. Run the `auto-py-to-exe.exe` executable. A new window for the "Auto Py to Exe" software will pop-up.
1. Fill-in the following fields as a bare minimum:
	1. Script Location (main Python script)
	1. Onefile (Choose One Directory)
	1. Console Window (Choose Window Based)
	1. Additional Files (every file that supports the main script)
1. Click `CONVERT .PY TO .EXE`.

The resulting executable and support files can be found in the following virtual environment directory: `<my-venv>/Scripts/output/<script_name>/<script_name>.exe`.

### Releases and Hotfixes

- The working development branch on Github is `develop`.
- to prepare for a new release:
	- Create release branch: `git checkout -b release-X.Y.Z develop`
	- Add, commit and, push the new release to Github.
	- Checkout master branch: `git checkout master`
	- Merge the release to master: `git merge --no-ff release-X.Y.Z`
	- Tag master with the release version: `git tag -a vX.Y.Z -m "tag comments go here"`
	- Push everything to Github `git push --all`; `git push --tags`
- New hotfixes follow the same instructions as new releases, but originally branch from `master`.
