#!/bin/bash


NEW_PROJECT_NAME=$1
TEMPLATE_DIR="/Users/croaker/git/Utilities/utilities/workflow_docs"
mkdir "$NEW_PROJECT_NAME"
cd ./"$NEW_PROJECT_NAME" || exit
mkdir ./src ./tests ./docs ./.vscode
touch ./.env ./setup.py ./README.md ./MANIFEST.in ./.gitignore ./.vscode/settings.json
export PIPENV_VENV_IN_PROJECT=1
pipenv --three
pipenv install --dev pylint pytest==4.0.2 autopep8 rope mypy sphinx black check-manifest
git init
#cat to files for setup.py, settings.json, .gitignore ?
