# BroLang

A toy programming language inspired by BhaiLang, developed as course project for SER502 - Languages and Programming paradigms at Arizona State University.

## Installation Instruction

### BroLang Setup Steps

** You may also just run `./setup.sh` and the script should tell you if you need to install any tools" **

1. Install Python 3, if you do not have 3.10 install pyenv as well.

2. Install pipenv.
   
   ```sh
   pip install pipenv
   ```

3. Install dependencies.
   
   ```sh
   pipenv install
   ```

## How to Use

** You can also pass file path to `./run.sh` and it should execute it for you. ex: `./run.sh ./data/basic.bl`. **

1. Execute code using the parser package.
   
   ```sh
   pipenv run python brolang <relative path to file>
   ```

ex:

```sh
pipenv run python brolang ./data/basic.bl
```

## References

- Expression grammar heavily inspired from ANTLR's example for the C language, as our operator precedence was functionally similar to C. The example can be found [here](https://github.com/antlr/grammars-v4/blob/master/c/C.g4).
