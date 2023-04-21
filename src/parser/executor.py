from compiler.BroLangLexer import BroLangLexer
from compiler.BroLangParser import BroLangParser

from antlr4.tree.Trees import Trees
from antlr4 import CommonTokenStream, FileStream

def execute(filepath: str) -> None:

  lexer = BroLangLexer(FileStream(filepath))
  stream = CommonTokenStream(lexer)
  parser = BroLangParser(stream)
  tree = parser.prog()

  print(Trees.toStringTree(tree, None, parser))