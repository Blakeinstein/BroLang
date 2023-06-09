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
  
  def visitMultiplicative(self, ctx:BroLangParser.MultiplicativeContext):
    oprs = [self.visit(opr) for opr in ctx.oprs]
    oprs.reverse()
    ops = [op.text for op in ctx.ops]
    ops.reverse()
    res = oprs[0]
    for opr, op in zip(oprs[1:], ops):
      match op:
        case '*':
          res = opr * res
        case '/':
          res = opr / res
        case '%':
          res = opr % res
    
    return res


  def visitAdditive(self, ctx:BroLangParser.AdditiveContext):
    oprs = [self.visit(opr) for opr in ctx.oprs]
    oprs.reverse()
    ops = [op.text for op in ctx.ops]
    ops.reverse()
    res = oprs[0]
    for opr, op in zip(oprs[1:], ops):
      match op:
        case '+':
          res = opr + res
        case '-':
          res = opr - res
      
    return res


  def visitShift(self, ctx:BroLangParser.ShiftContext):
    oprs = [self.visit(opr) for opr in ctx.oprs]
    oprs.reverse()
    ops = [op.text for op in ctx.ops]
    ops.reverse()
    res = oprs[0]
    for opr, op in zip(oprs[1:], ops):
      try:
        match op:
          case '<<':
            res = int(opr) << int(res)
          case '>>':
            res = int(opr) >> int(res)
      except Exception as e:
        print(e)
        print(f"{res:g} isnt an integer bro.")
    return res


  def visitRelational(self, ctx:BroLangParser.RelationalContext):
    oprs = [self.visit(opr) for opr in ctx.oprs]
    oprs.reverse()
    ops = [op.text for op in ctx.ops]
    ops.reverse()
    res = oprs[0]
    for opr, op in zip(oprs[1:], ops):
      match op:
        case '<':
          res = opr < res
        case '>':
          res = opr > res
        case '<=':
          res = opr <= res
        case '>=':
          res = opr >= res
    
    return res


  def visitEquality(self, ctx:BroLangParser.EqualityContext):
    oprs = [self.visit(opr) for opr in ctx.oprs]
    oprs.reverse()
    ops = [op.text for op in ctx.ops]
    ops.reverse()
    res = oprs[0]
    for opr, op in zip(oprs[1:], ops):
      match op:
        case '==':
          res = opr == res
        case '!=':
          res = opr != res
    
    return res


  def visitAnd(self, ctx:BroLangParser.AndContext):
    oprs = [self.visit(opr) for opr in ctx.oprs]
    return reduce(lambda acc, x : (int(acc) & int(x)) , oprs[1:], oprs[0])


  def visitExclusiveOr(self, ctx:BroLangParser.ExclusiveOrContext):
    oprs = [self.visit(opr) for opr in ctx.oprs]
    oprs.reverse()
    return reduce(lambda acc, x : (int(acc) ^ int(x)) , oprs[1:], oprs[0])


  def visitInclusiveOr(self, ctx:BroLangParser.InclusiveOrContext):
    oprs = [self.visit(opr) for opr in ctx.oprs]
    oprs.reverse()
    return reduce(lambda acc, x : (int(acc) | int(x)) , oprs[1:], oprs[0])


  def visitLogicalAnd(self, ctx:BroLangParser.LogicalAndContext):
    oprs = [self.visit(opr) for opr in ctx.oprs]
    oprs.reverse()
    return reduce(lambda acc, x : (int(acc) and int(x)) , oprs[1:], oprs[0])


  def visitLogicalOr(self, ctx:BroLangParser.LogicalOrContext):
    oprs = [self.visit(opr) for opr in ctx.oprs]
    oprs.reverse()
    return reduce(lambda acc, x : (int(acc) or int(x)) , oprs[1:], oprs[0])


  def visitConditionalExpr(self, ctx:BroLangParser.ConditionalExprContext):
    condition = self.visit(ctx.condition)

    if len(ctx.children) == 1:
      return condition

    if condition:
      return self.visit(ctx.true_block)
    else:
      return self.visit(ctx.false_block)


  def visitExpression(self, ctx:BroLangParser.ExpressionContext):
    return self.visitChildren(ctx)


  def visitTerminalData(self, ctx:BroLangParser.TerminalDataContext):
    if ctx.identifier():
      data = self.visit(ctx.identifier())
      self.assert_env(data)
      return self.data_map[data]

    if ctx.expression():
      return self.visit(ctx.expression())
  
    return self.visit(ctx.number())


  def visitNegation(self, ctx:BroLangParser.NegationContext):
    return (not self.visit(ctx.terminalData()))


  def visitIdentifier(self, ctx:BroLangParser.IdentifierContext):
    return ctx.getText()


  def visitNumber(self, ctx:BroLangParser.NumberContext):
    return float(ctx.getText())


  def visitString(self, ctx:BroLangParser.StringContext):
    return ctx.getText().strip('\"')
