from parser.executor import execute

import argparse
from pathlib import Path
from os.path import abspath


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("file_path", type=Path, help="Path to the file to be executed.")
  parser.add_argument("-p", "--print_tree", type=bool, default=False, help="Prints the tree of the program.")

  p = parser.parse_args()

  if not p.file_path:
    parser.print_help()
    exit(1)

  path = abspath(p.file_path)
  if not path:
    print(f"File {p.file_path} not found.")
    exit(1)

  execute(path, p.print_tree)