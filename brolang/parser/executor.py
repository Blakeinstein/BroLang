from compiler.BroLangLexer import BroLangLexer
from compiler.BroLangParser import BroLangParser
from .visitor import Visitor

from antlr4.tree.Trees import Trees
from antlr4 import CommonTokenStream, FileStream

def execute(filepath: str, print_tree: bool = False) -> None:

  tokens = BroLangLexer(FileStream(filepath))
  stream = CommonTokenStream(tokens)
  parser = BroLangParser(stream)
  tree = parser.prog()

  if print_tree:
    print(Trees.toStringTree(tree, None, parser))

  visitor = Visitor()

  return visitor.visit(tree)