#!/bin/bash

if ! command -v python &>/dev/null; then
  echo "Python is not installed. Please install Python 3 first."
  exit 1
fi

if ! command -v pipenv &>/dev/null; then
  echo "Pipenv is not installed. Please install pipenv."
  exit 1
fi

# Get Python version
python_version=$(python -c 'import platform; print(platform.python_version())')

# Extract major and minor version numbers
major_version=$(echo "$python_version" | cut -d. -f1)
minor_version=$(echo "$python_version" | cut -d. -f2)

# Check if Python 3.10.X is installed
if [[ $major_version -eq 3 && $minor_version -eq 10 ]]; then
    echo "The correct python version is installed!"
else
    echo "In case pipenv is unable to find python 3.10, you may need to install pyenv."
fi

pipenv install