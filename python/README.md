# Inventory Manager: Source Usage and Development

## Prerequisites

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

## Installation

1. Clone the repo to a directory on the target machine.
1. Create a new virtual environment: 
	1. Navigate to a directory outside of the cloned repo `inv-mgr/`.
	1. Enter `python -m venv <my-venv>`, where `<my-venv>` is the desired name for the new virtual environment.
1. Activate the virtual environment:
	1. Make sure you are in the same directory where `<my-venv>` was created.
	1. For Windows: Enter `.\<my-venv>\Scripts\activate`
	1. For Linux or macOS: `source <my-venv>/bin/activate`
1. Navigate to the `inv-mgr/python/` directory and enter `python setup.py install` to install supporting Python packages.

## Project Directory

```
.
├───src: source code and resource directory
│   ├───db: sqlite3 .db files
│   └───ui: Qt designer .ui files
├───sandbox: For development and testing purposes only
│	├───db: sqlite3 .db files
│	└───ui: Qt designer .ui files
├───README.md: this document
└───setup.py: Python setuptools installation script
```

## Script Use

Directory: `inv-mgr/python/src/`

To run a script rather than an executable, enter `python <script_name>.py` in the command terminal.

- `inv_mgr.py`
	- Main Inventory Manager script.

## Development

- The working development branch on Github is `develop`.
- to prepare for a new release:
	- Create release branch: `git checkout -b release-X.Y.Z develop`
	- Add, commit and, push the new release to Github.
	- Checkout master branch: `git checkout master`
	- Merge the release to master: `git merge --no-ff release-X.Y.Z`
	- Tag master with the release version: `git tag -a X.Y.Z -m "tag comments go here"`
	- Push everything to Github `git push --all`; `git push --tags`
- New hotfixes follow the same instructions as new releases, but originally branch from `master`.

### Python Files and Scripts

Prior to generating or running a script, activate the virtual environment. See Installation instructions for details. `deactivate` can be entered when the package is no longer in use (works for all OS). 

New `.py` Python script files are to be saved in the `inv-mgr/python/src/` directory.

### QT Designer GUIs

#### GUI Creation
QT Designer is used to create `.ui` files for the project GUI. The executable is located in the virtual environment at `Lib/site-packages/qt5_applications/Qt/bin/designer.exe`.

New `.ui` QT Designer files are to be saved in the `inv-mgr/python/src/ui/` directory.

All `.ui` files must be converted to a `.py` file prior to use. To create a `.py` files from a `.ui` file:

1. Navigate to the `inv-mgr/python/src/ui/` directory.
1. Enter the following command: `pyuic5 -x -o <designer_ui.py> <designer_uo.ui>`
	- `<designer_ui.py>` is the desired `.py` file to create.
	- `<designer_uo.ui>` is the target `.ui` file.

#### Resources Files and Images

Images can be placed onto the GUI using `QLabel` widgets with their text fields cleared. 

Before placing a PNG, a `.qrc` resource file holding the image must be created and saved to the `img-mgr/python/src/ui/` directory. Once created, the resource file can be added to the `Qlabel` field `pixmap`.

To working within the Python environment, the `.qrc` must be converted to a `.py`, and then the `.py` must be imported into the main Python scripts. To do this:

1.	Enter the command can be used: `pyrcc5 -o <my_resource>_rc.py <my_resource>.qrc`.
	- `<my_resource>` is the name of the resource file. 
	- The `_rc` tag signifies that the Python file is derived from a resource.
1. Open the `.ui` file that the resource file is used in. 
1. Search for the line `import <my_resource>_rc` and comment it out.
1. Copy the import statement from the previous step and then add it to the main Python script. **IF THIS STEP ISN'T TAKEN, COMPILING ISSUES WILL OCCUR.**

### SQLite3 Databases

New databases can be generated using the DB Browser for SQLite tool. 

New `.db` database files are to be saved in the `inv-mgr/python/src/db/` directory.

### Executable Creation

The project can be turned into an executable by performing the following steps:

1. Navigate to the `<my-venv>/Scripts/` virtual environment directory.
1. Run the `auto-py-to-exe.exe` executable. A new window for the "Auto Py to Exe" software will pop-up.
1. Fill-in the following fields as a bare minimum:
	1. Script Location
	1. Onefile (Choose One Directory)
	1. Console Window (Choose Window Based)
	1. Additional Files
		- Note that if "Add Files" is used, its usually a good idea to assign those files to the appropriate directory if they are not in the root directory where the main Python script is. For example, the `parts.db` database needs to be added and the associated destination field to the right of it should be `db/`.
1. Click `CONVERT .PY TO .EXE`.

The resulting executable and support files can be found in the following virtual environment directory: `<my-venv>/Scripts/output/inv_mgr/inv_mgr.exe`.
