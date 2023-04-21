# Generated from src/grammar/BroLang.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BroLangParser import BroLangParser
else:
    from BroLangParser import BroLangParser

# This class defines a complete listener for a parse tree produced by BroLangParser.
class BroLangListener(ParseTreeListener):

    # Enter a parse tree produced by BroLangParser#prog.
    def enterProg(self, ctx:BroLangParser.ProgContext):
        pass

    # Exit a parse tree produced by BroLangParser#prog.
    def exitProg(self, ctx:BroLangParser.ProgContext):
        pass


    # Enter a parse tree produced by BroLangParser#block.
    def enterBlock(self, ctx:BroLangParser.BlockContext):
        pass

    # Exit a parse tree produced by BroLangParser#block.
    def exitBlock(self, ctx:BroLangParser.BlockContext):
        pass


    # Enter a parse tree produced by BroLangParser#command.
    def enterCommand(self, ctx:BroLangParser.CommandContext):
        pass

    # Exit a parse tree produced by BroLangParser#command.
    def exitCommand(self, ctx:BroLangParser.CommandContext):
        pass


    # Enter a parse tree produced by BroLangParser#declaration.
    def enterDeclaration(self, ctx:BroLangParser.DeclarationContext):
        pass

    # Exit a parse tree produced by BroLangParser#declaration.
    def exitDeclaration(self, ctx:BroLangParser.DeclarationContext):
        pass


    # Enter a parse tree produced by BroLangParser#assignment.
    def enterAssignment(self, ctx:BroLangParser.AssignmentContext):
        pass

    # Exit a parse tree produced by BroLangParser#assignment.
    def exitAssignment(self, ctx:BroLangParser.AssignmentContext):
        pass


    # Enter a parse tree produced by BroLangParser#ifthenelse.
    def enterIfthenelse(self, ctx:BroLangParser.IfthenelseContext):
        pass

    # Exit a parse tree produced by BroLangParser#ifthenelse.
    def exitIfthenelse(self, ctx:BroLangParser.IfthenelseContext):
        pass


    # Enter a parse tree produced by BroLangParser#whileBlock.
    def enterWhileBlock(self, ctx:BroLangParser.WhileBlockContext):
        pass

    # Exit a parse tree produced by BroLangParser#whileBlock.
    def exitWhileBlock(self, ctx:BroLangParser.WhileBlockContext):
        pass


    # Enter a parse tree produced by BroLangParser#forBlock.
    def enterForBlock(self, ctx:BroLangParser.ForBlockContext):
        pass

    # Exit a parse tree produced by BroLangParser#forBlock.
    def exitForBlock(self, ctx:BroLangParser.ForBlockContext):
        pass


    # Enter a parse tree produced by BroLangParser#forRange.
    def enterForRange(self, ctx:BroLangParser.ForRangeContext):
        pass

    # Exit a parse tree produced by BroLangParser#forRange.
    def exitForRange(self, ctx:BroLangParser.ForRangeContext):
        pass


    # Enter a parse tree produced by BroLangParser#print.
    def enterPrint(self, ctx:BroLangParser.PrintContext):
        pass

    # Exit a parse tree produced by BroLangParser#print.
    def exitPrint(self, ctx:BroLangParser.PrintContext):
        pass


    # Enter a parse tree produced by BroLangParser#println.
    def enterPrintln(self, ctx:BroLangParser.PrintlnContext):
        pass

    # Exit a parse tree produced by BroLangParser#println.
    def exitPrintln(self, ctx:BroLangParser.PrintlnContext):
        pass


    # Enter a parse tree produced by BroLangParser#vals.
    def enterVals(self, ctx:BroLangParser.ValsContext):
        pass

    # Exit a parse tree produced by BroLangParser#vals.
    def exitVals(self, ctx:BroLangParser.ValsContext):
        pass


    # Enter a parse tree produced by BroLangParser#data.
    def enterData(self, ctx:BroLangParser.DataContext):
        pass

    # Exit a parse tree produced by BroLangParser#data.
    def exitData(self, ctx:BroLangParser.DataContext):
        pass


    # Enter a parse tree produced by BroLangParser#multiplicative.
    def enterMultiplicative(self, ctx:BroLangParser.MultiplicativeContext):
        pass

    # Exit a parse tree produced by BroLangParser#multiplicative.
    def exitMultiplicative(self, ctx:BroLangParser.MultiplicativeContext):
        pass


    # Enter a parse tree produced by BroLangParser#additive.
    def enterAdditive(self, ctx:BroLangParser.AdditiveContext):
        pass

    # Exit a parse tree produced by BroLangParser#additive.
    def exitAdditive(self, ctx:BroLangParser.AdditiveContext):
        pass


    # Enter a parse tree produced by BroLangParser#relational.
    def enterRelational(self, ctx:BroLangParser.RelationalContext):
        pass

    # Exit a parse tree produced by BroLangParser#relational.
    def exitRelational(self, ctx:BroLangParser.RelationalContext):
        pass


    # Enter a parse tree produced by BroLangParser#equality.
    def enterEquality(self, ctx:BroLangParser.EqualityContext):
        pass

    # Exit a parse tree produced by BroLangParser#equality.
    def exitEquality(self, ctx:BroLangParser.EqualityContext):
        pass


    # Enter a parse tree produced by BroLangParser#conditionalExpr.
    def enterConditionalExpr(self, ctx:BroLangParser.ConditionalExprContext):
        pass

    # Exit a parse tree produced by BroLangParser#conditionalExpr.
    def exitConditionalExpr(self, ctx:BroLangParser.ConditionalExprContext):
        pass


    # Enter a parse tree produced by BroLangParser#shift.
    def enterShift(self, ctx:BroLangParser.ShiftContext):
        pass

    # Exit a parse tree produced by BroLangParser#shift.
    def exitShift(self, ctx:BroLangParser.ShiftContext):
        pass


    # Enter a parse tree produced by BroLangParser#and.
    def enterAnd(self, ctx:BroLangParser.AndContext):
        pass

    # Exit a parse tree produced by BroLangParser#and.
    def exitAnd(self, ctx:BroLangParser.AndContext):
        pass


    # Enter a parse tree produced by BroLangParser#exclusiveOr.
    def enterExclusiveOr(self, ctx:BroLangParser.ExclusiveOrContext):
        pass

    # Exit a parse tree produced by BroLangParser#exclusiveOr.
    def exitExclusiveOr(self, ctx:BroLangParser.ExclusiveOrContext):
        pass


    # Enter a parse tree produced by BroLangParser#inclusiveOr.
    def enterInclusiveOr(self, ctx:BroLangParser.InclusiveOrContext):
        pass

    # Exit a parse tree produced by BroLangParser#inclusiveOr.
    def exitInclusiveOr(self, ctx:BroLangParser.InclusiveOrContext):
        pass


    # Enter a parse tree produced by BroLangParser#logicalAnd.
    def enterLogicalAnd(self, ctx:BroLangParser.LogicalAndContext):
        pass

    # Exit a parse tree produced by BroLangParser#logicalAnd.
    def exitLogicalAnd(self, ctx:BroLangParser.LogicalAndContext):
        pass


    # Enter a parse tree produced by BroLangParser#logicalOr.
    def enterLogicalOr(self, ctx:BroLangParser.LogicalOrContext):
        pass

    # Exit a parse tree produced by BroLangParser#logicalOr.
    def exitLogicalOr(self, ctx:BroLangParser.LogicalOrContext):
        pass


    # Enter a parse tree produced by BroLangParser#expression.
    def enterExpression(self, ctx:BroLangParser.ExpressionContext):
        pass

    # Exit a parse tree produced by BroLangParser#expression.
    def exitExpression(self, ctx:BroLangParser.ExpressionContext):
        pass


    # Enter a parse tree produced by BroLangParser#terminalData.
    def enterTerminalData(self, ctx:BroLangParser.TerminalDataContext):
        pass

    # Exit a parse tree produced by BroLangParser#terminalData.
    def exitTerminalData(self, ctx:BroLangParser.TerminalDataContext):
        pass


    # Enter a parse tree produced by BroLangParser#identifier.
    def enterIdentifier(self, ctx:BroLangParser.IdentifierContext):
        pass

    # Exit a parse tree produced by BroLangParser#identifier.
    def exitIdentifier(self, ctx:BroLangParser.IdentifierContext):
        pass


    # Enter a parse tree produced by BroLangParser#number.
    def enterNumber(self, ctx:BroLangParser.NumberContext):
        pass

    # Exit a parse tree produced by BroLangParser#number.
    def exitNumber(self, ctx:BroLangParser.NumberContext):
        pass


    # Enter a parse tree produced by BroLangParser#string.
    def enterString(self, ctx:BroLangParser.StringContext):
        pass

    # Exit a parse tree produced by BroLangParser#string.
    def exitString(self, ctx:BroLangParser.StringContext):
        pass



del BroLangParser