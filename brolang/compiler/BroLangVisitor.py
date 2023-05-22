# Generated from src/grammar/BroLang.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BroLangParser import BroLangParser
else:
    from BroLangParser import BroLangParser

# This class defines a complete generic visitor for a parse tree produced by BroLangParser.

class BroLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BroLangParser#prog.
    def visitProg(self, ctx:BroLangParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BroLangParser#block.
    def visitBlock(self, ctx:BroLangParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BroLangParser#command.
    def visitCommand(self, ctx:BroLangParser.CommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BroLangParser#declaration.
    def visitDeclaration(self, ctx:BroLangParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BroLangParser#assignment.
    def visitAssignment(self, ctx:BroLangParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BroLangParser#ifthenelse.
    def visitIfthenelse(self, ctx:BroLangParser.IfthenelseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BroLangParser#whileBlock.
    def visitWhileBlock(self, ctx:BroLangParser.WhileBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BroLangParser#forBlock.
    def visitForBlock(self, ctx:BroLangParser.ForBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BroLangParser#forRange.
    def visitForRange(self, ctx:BroLangParser.ForRangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BroLangParser#print.
    def visitPrint(self, ctx:BroLangParser.PrintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BroLangParser#println.
    def visitPrintln(self, ctx:BroLangParser.PrintlnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BroLangParser#vals.
    def visitVals(self, ctx:BroLangParser.ValsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BroLangParser#data.
    def visitData(self, ctx:BroLangParser.DataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BroLangParser#multiplicative.
    def visitMultiplicative(self, ctx:BroLangParser.MultiplicativeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BroLangParser#additive.
    def visitAdditive(self, ctx:BroLangParser.AdditiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BroLangParser#relational.
    def visitRelational(self, ctx:BroLangParser.RelationalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BroLangParser#equality.
    def visitEquality(self, ctx:BroLangParser.EqualityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BroLangParser#conditionalExpr.
    def visitConditionalExpr(self, ctx:BroLangParser.ConditionalExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BroLangParser#shift.
    def visitShift(self, ctx:BroLangParser.ShiftContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BroLangParser#and.
    def visitAnd(self, ctx:BroLangParser.AndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BroLangParser#exclusiveOr.
    def visitExclusiveOr(self, ctx:BroLangParser.ExclusiveOrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BroLangParser#inclusiveOr.
    def visitInclusiveOr(self, ctx:BroLangParser.InclusiveOrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BroLangParser#logicalAnd.
    def visitLogicalAnd(self, ctx:BroLangParser.LogicalAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BroLangParser#logicalOr.
    def visitLogicalOr(self, ctx:BroLangParser.LogicalOrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BroLangParser#expression.
    def visitExpression(self, ctx:BroLangParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BroLangParser#terminalData.
    def visitTerminalData(self, ctx:BroLangParser.TerminalDataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BroLangParser#negation.
    def visitNegation(self, ctx:BroLangParser.NegationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BroLangParser#identifier.
    def visitIdentifier(self, ctx:BroLangParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BroLangParser#number.
    def visitNumber(self, ctx:BroLangParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BroLangParser#string.
    def visitString(self, ctx:BroLangParser.StringContext):
        return self.visitChildren(ctx)



del BroLangParser