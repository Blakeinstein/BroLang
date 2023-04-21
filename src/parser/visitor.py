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

 
  def visitIfthenelse(self, ctx:BroLangParser.IfthenelseContext):
    if self.visit(ctx.expression()):
      self.visit(ctx.true_block)
    else:
      self.visit(ctx.false_block)

  
  def visitWhileBlock(self, ctx:BroLangParser.WhileBlockContext):
    while self.visit(ctx.expression()):
      self.visit(ctx.block())

  
  def visitForBlock(self, ctx:BroLangParser.ForBlockContext):
    self.visit(ctx.pre)
    
    while self.visit(ctx.expression()):
      self.visit(ctx.loop)
      self.visit(ctx.post)

 
  def visitForRange(self, ctx:BroLangParser.ForRangeContext):
    id = self.visit(ctx.identifier())
    old_val = None
    if id in self.data_map:
      old_val = self.data_map[id]
    
    i = self.visit(ctx.start)
    end = self.visit(ctx.end)

    while i < end:
      self.data_map[id] = i
      self.visit(ctx.block())
      i += 1
    
    if old_val:
      self.data_map[id] = old_val
    else:
      self.data_map.pop(id)

  
  def visitPrint(self, ctx:BroLangParser.PrintContext):
    print(*self.visit(ctx.vals(), end=""))


  def visitPrintln(self, ctx:BroLangParser.PrintlnContext):
    print(*self.visit(ctx.vals()))

  
  def visitVals(self, ctx:BroLangParser.ValsContext):
    return [self.visit(child) for child in ctx.data_terms]


  def visitData(self, ctx:BroLangParser.DataContext):
    return self.visitChildren(ctx)