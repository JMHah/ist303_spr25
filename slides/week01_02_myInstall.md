

# Exploring in the Terminal
![Exploring (Jusant)](https://i.giphy.com/WQ2EpFMloBumDiuSsr.gif)

## This section not formatted as slides 
- not intended for memorization/review
- run through some common commands
- matches appearance of terminal

## Windows Path
- Check Path: `$Env:PATH`
- If you don't see your python install folder you can add the path in command line
- Append to path:`$Env:PATH = "C:\newPathToAdd;" + $Env:PATH`

## Terminal (aka Shell, command line, CLI)
- view files: `ls`
- change directory: `cd dirName`
   - change directory to parent: `cd..`
   - change directory to home: `cd ~`
   - change directory to root: `cd\`
- create directory: `mkdir newDir`
- remove file/dir: `rm dirName`
- create file: \
`echo "someText" > fileName.ext`
- run a python script: \
`python script.py`


## Virtual environments
**Virtual environments** isolate versions of installed software *within a project scope* independent from what is installed *globally on your computer*. Only packages you install in a specific virtual environment will be available when working on the project.

Note: virtual environments will have pip installed within the environment by default.

- Creating a Virtual Environment
   - in current directory: \
   `python -m venv venvName`
   - customary to name virtual env _venv_: \
   `python -m venv venv`
   - in specific directory: \
   `python -m venv C:\path\venvName`
- Activating a Virtual Environment (Windows)
   - from your virtual environment directory: \
   `./Scripts/activate`
   - from your project directory that contains the venv directory (parent directory of the virtual environment): \
   `./venv/Scripts/activate`
   - from any working directory (powershell): \
   `C:\path to venv\Scripts\activate.ps1` \
   example: `C:\Users\david\Documents\courses\ist303_spr25\test_dir\venv\Scripts\activate.ps1`
   - specific dir (cmd): change `.ps1` to `.bat`
- Activating a Virtual Environment (Linux/MacOS)
   - `source myvenv/bin/activate`
- Deactivate (all platforms): `deactivate`

## Python Package Management
Python packages are managed/installed with pip. Check if you have pip installed: \
`pip --version`

If not, install from terminal (remember that `python` can be shortened to `py` in terminal commands if the py launcher is installed):
- windows: \
`python -m ensurepip --upgrade`
- linux: \
`wget https://bootstrap.pypa.io/get-pip.py` \
`python ./get-pip.py`

### Installing Python packages
- `pip install packageName`
- packages you will need in the course:
   - [Pytest](https://pypi.org/project/pytest/)
   - [Flask](https://flask.palletsprojects.com/en/3.0.x/)
- view installed packages: `pip list`

### Update packages
- `pip install --upgrade package`
- example (upgrade pip package): `pip install --upgrade pip`

### Uninstall packages
- `pip uninstall package`


---
# Starting the Python Interpreter
Will depend whether py launcher is installed. From the terminal:
- with py launcher: `py`
- without py launcher: `python`

You will see `>>>` as the new prompt to denote the python interactive session. 

Exit a python session using `quit()`

You can type and execute python code directly by typing at the prompt.

---
Run a script from within an interactive Python session: \
`exec(open("filename.py").read())`

### [Agile Slides](week01_03_slides_agile.md)



