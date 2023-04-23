# SER502-Spring2023-Team21

## Development Environment
 - Systems: Windows, MacOs and Linux (Any Flavor)

 - Tools to build compiler: Python 3.10 and ANTLR 4.12

 - Tools to build runtime: pipenv (optioanlly pyenv, if installed python is not python 3.10)

## Installation Instruction
### DevilsCode Installation Steps

** You may also just run `./setup.sh` and the script should tell you if you need something installed" **

0. Install Python 3, if you do not have 3.10 install pyenv as well.
  1. Install pipenv.
    ```sh
    pip install pipenv
    ```
  2. Install dependencies
    ```sh
    pipenv install
    ```

1. Invoke pipenv shell, and cd to src
```sh
pipenv shell
```

## How to Use
** You can also pass file path to `./run.sh` and it should execute it for you. ex: `./run.sh ./data/loop.bl`. **

1. Execute code using the parser package.
```sh
python -m src <relative path to file>
```

ex:
```sh
python -m src ../data/basic.bl
```
## Bug informaiton

## YouTube Link
