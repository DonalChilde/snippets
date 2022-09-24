
# Python Workflow

## New Project

### Folder Setup

Make a new project folder.

```bash
mkdir $NEW_PROJECT_NAME
cd ./$NEW_PROJECT_NAME
mkdir ./src ./tests ./docs
touch ./.env ./setup.py ./setup.cfg ./MANIFEST.in ./.gitignore ./requirements.txt ./requirements-dev.txt  ./pyproject.toml ./README.rst
```

### requirements.txt

requirements-dev.txt

```txt
pylint
pytest
black
tox
coverage

```

### setup.py with setup.cfg

setup.py

```python
from setuptools import setup

setup()

```

setup.cfg

```cfg
[metadata]
name = pytarpax
version = attr: pytarpax.VERSION
description = My package description
long_description = file: README.rst, CHANGELOG.rst, LICENSE.rst
keywords = tar
license = BSD 3-Clause License
classifiers =
    Programming Language :: Python :: 3
    Programming Language :: Python :: 3.7

[options]
zip_safe = False
include_package_data = True
package_dir=
    =src
packages = find:


[options.package_data]
* = *.txt, *.rst
hello = *.msg

# [options.extras_require]
# pdf = ReportLab>=1.2; RXP
# rest = docutils>=0.3; pack ==1.1, ==1.3

[options.packages.find]
where=src

# [options.data_files]
# /etc/my_package =
#     site.d/00_default.conf
#     host.d/00_default.conf
# data = data/img/logo.png, data/svg/icon.svg
```

pyproject.toml

```txt
[build-system]
requires = [
    "setuptools>=30.3.0",
    "wheel",
]

```

### Virtual Environments Without Pipenv

Make the virtual environment

```bash
python3 -m venv ./.venv
source  ./.venv/bin/activate
pip install setuptools
pip install wheel
pip install -r ./requirements-dev.txt
pip install -r ./requirements.txt
pip install --editable .
pylint --generate-rcfile > ./.pylintrc
```

### With Pipenv

tell pipenv to make the .venv in the project folder

```bash
export PIPENV_VENV_IN_PROJECT=1
echo "PIPENV_VENV_IN_PROJECT=1" >> ./.env
```

open a new shell in pipenv to force creation of new .venv

```bash
pipenv shell
```

Check that the .venv installed in the correct folder.
If not, remove the venv with `pipenv --rm`.
You may also have to remove the PipFile that was created.

install --dev tools

```bash
pipenv install --dev pylint pytest==4.0.2 autopep8 rope mypy sphinx black check-manifest
```

add Setup.py

examples:
<https://github.com/kennethreitz/setup.py/blob/master/setup.py>
<https://python-packaging.readthedocs.io/en/latest/minimal.html>

To install dev code. might have to wait til some code is added?

```bash
pipenv install --dev -e .
```



### git

<https://realpython.com/python-git-github-intro/>
<https://code.visualstudio.com/docs/editor/versioncontrol>
in project folder, init git repo

```git
git init
```

check git status

```git
git status
```

add .gitignore
for OSX, check for .DS_Store in .gitignore
<https://github.com/github/gitignore>

```git
touch .gitignore
```

stage all files

```git
git add .
```

consider interactive mode
<https://git-scm.com/book/en/v2/Git-Tools-Interactive-Staging>

```git
git add -i
```

commit changes, with a commit message

```git
git commit -m "add you commit message here"
```

remove tracked files, recursive with -r

```git
git rm -r --cached *.code-workspace
```

## VSCode

### workspace settings for vscode

these go in .vscode/settings.json
if the file is not yet created, go to Code->preferences->settings and click on folder settings

```json
{
    "python.pythonPath": ".venv/bin/python",
    "python.unitTest.unittestEnabled": false,
    "python.unitTest.pyTestEnabled": true,
    "python.unitTest.nosetestsEnabled": false,
    "python.unitTest.pyTestArgs": [
        "-l",
        "-v",
        "-s",
        "--tb=native",
        "-W ignore::DeprecationWarning",
        "--log-cli-level=INFO"
    ],
    "python.linting.mypyEnabled": true,
    "python.formatting.provider": "black",
    "[python]": {
        "editor.formatOnSave": true,
        "editor.formatOnPaste": true
    }
}
```

keep the Workspace file on top level of project.
the .env file on top level of project can store values including paths to other source folders
<https://code.visualstudio.com/docs/python/environments#_environment-variable-definitions-file>

### launch.json

<https://code.visualstudio.com/docs/python/debugging>

when running from terminal, using multiple source folders

```bash
export PYTHONPATH=/Users/croaker/git/AsyncQueueRunner
```

### not showing underscore in terminal

https://github.com/Microsoft/vscode/issues/35901

```json
"terminal.integrated.fontSize": 16,
"terminal.integrated.fontFamily": "Ubuntu mono",
```

or
```
I fixed the issue by removing 'monospace' from editor.fontFamily in settings.json (or Settings > Text Editor > Font > Font Family):

# Broken: "Hello_World!" -> "Hello World!"
"editor.fontFamily": "'Droid Sans Mono', 'monospace', monospace, 'Droid Sans Fallback'"

# Works: "Hello_World!" -> "Hello_World!"
"editor.fontFamily": "'Droid Sans Mono', monospace, 'Droid Sans Fallback'"
Neither of the other fixes above worked for me.
```

NOTE: removing 'monospace' worked for me on vscode 1.33.1


## Pytest

Pytest command line options:  (pytest -h for full list)

-s                    shortcut for --capture=no.
-v, --verbose         increase verbosity.
-l, --showlocals      show locals in tracebacks (disabled by default).
--show-capture={no,stdout,stderr,log,all}
-W PYTHONWARNINGS, --pythonwarnings=PYTHONWARNINGS
                      set which warnings to report, see -W option of python
                      itself.
--log-level=LOG_LEVEL  logging level used by the logging module

## Python logging

```python
import logging
from sys import stdout

#### setting up logger ####
logger = logging.getLogger(__name__)

#### Log Level ####
# NOTSET=0, DEBUG=10, INFO=20, WARN=30, ERROR=40, and CRITICAL=50
# log_level = logging.DEBUG
# log_level = logging.INFO
log_level = logging.NOTSET
logger.setLevel(log_level)

#### Log Handler ####
log_formatter = logging.Formatter(
    "%(asctime)s — %(name)s — %(levelname)s — %(funcName)s:%(lineno)d — %(message)s", datefmt='%d-%b-%y %H:%M:%S')
# log_handler = logging.StreamHandler(stdout)
log_handler = logging.StreamHandler()
log_handler.setFormatter(log_formatter)
logger.addHandler(log_handler)

# if logger.isEnabledFor(logging.DEBUG):
#     pass
```

## Building projects

python Setup.py sdist
