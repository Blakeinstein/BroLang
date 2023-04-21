from functools import reduce
from antlr4 import *

from compiler.BroLangParser import BroLangParser
from compiler.BroLangVisitor import BroLangVisitor

class Visitor(BroLangVisitor):
  data_map: dict[str, str | float] = dict()

  def assert_env(self, key: str):
    if key not in self.data_map:
      raise Exception(
        f"My brother in christ, variable <{id}> not found, did you forget to declare it?"
      )
  
  def visitProg(self, ctx:BroLangParser.ProgContext):
    self.visitChildren(ctx)
    return 0

  def visitDeclaration(self, ctx:BroLangParser.DeclarationContext):
    id = self.visit(ctx.identifier())
    val = 0.0
    if ctx.data() is not None:
      val = self.visit(ctx.data())
    self.data_map[id] = val

  def visitAssignment(self, ctx:BroLangParser.AssignmentContext):
    id = self.visit(ctx.identifier())
    val = self.visit(ctx.data())
    
    self.assert_env(id)

    self.data_map[id] = val