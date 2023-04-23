from parser.executor import execute

from sys import argv

if __name__ == "__main__":
  file = argv[1]
  print_tree = False
  if len(argv) >= 3 and argv[2] == "-p":
    print_tree = True
  execute(file, print_tree)