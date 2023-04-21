from parser.executor import execute

from sys import argv

if __name__ == "__main__":
  file = argv[1]
  execute(file)