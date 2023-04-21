# Generated from src/grammar/BroLang.g4 by ANTLR 4.12.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,44,265,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,1,0,1,0,1,0,1,0,1,0,1,1,5,1,65,8,1,10,1,12,1,
        68,9,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,78,8,2,1,3,1,3,1,3,1,
        3,3,3,84,8,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,
        1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,
        1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,
        1,11,1,11,1,11,5,11,149,8,11,10,11,12,11,152,9,11,1,12,1,12,3,12,
        156,8,12,1,13,1,13,1,13,5,13,161,8,13,10,13,12,13,164,9,13,1,14,
        1,14,1,14,5,14,169,8,14,10,14,12,14,172,9,14,1,15,1,15,1,15,5,15,
        177,8,15,10,15,12,15,180,9,15,1,16,1,16,1,16,5,16,185,8,16,10,16,
        12,16,188,9,16,1,17,1,17,1,17,1,17,1,17,1,17,3,17,196,8,17,1,18,
        1,18,1,18,5,18,201,8,18,10,18,12,18,204,9,18,1,19,1,19,1,19,5,19,
        209,8,19,10,19,12,19,212,9,19,1,20,1,20,1,20,5,20,217,8,20,10,20,
        12,20,220,9,20,1,21,1,21,1,21,5,21,225,8,21,10,21,12,21,228,9,21,
        1,22,1,22,1,22,5,22,233,8,22,10,22,12,22,236,9,22,1,23,1,23,1,23,
        5,23,241,8,23,10,23,12,23,244,9,23,1,24,1,24,1,24,3,24,249,8,24,
        1,25,1,25,1,25,1,25,1,25,1,25,3,25,257,8,25,1,26,1,26,1,27,1,27,
        1,28,1,28,1,28,0,0,29,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,
        32,34,36,38,40,42,44,46,48,50,52,54,56,0,5,1,0,20,22,1,0,23,24,1,
        0,25,28,1,0,29,30,1,0,33,34,261,0,58,1,0,0,0,2,66,1,0,0,0,4,77,1,
        0,0,0,6,79,1,0,0,0,8,87,1,0,0,0,10,92,1,0,0,0,12,105,1,0,0,0,14,
        113,1,0,0,0,16,125,1,0,0,0,18,137,1,0,0,0,20,141,1,0,0,0,22,145,
        1,0,0,0,24,155,1,0,0,0,26,157,1,0,0,0,28,165,1,0,0,0,30,173,1,0,
        0,0,32,181,1,0,0,0,34,189,1,0,0,0,36,197,1,0,0,0,38,205,1,0,0,0,
        40,213,1,0,0,0,42,221,1,0,0,0,44,229,1,0,0,0,46,237,1,0,0,0,48,248,
        1,0,0,0,50,256,1,0,0,0,52,258,1,0,0,0,54,260,1,0,0,0,56,262,1,0,
        0,0,58,59,5,1,0,0,59,60,3,2,1,0,60,61,5,2,0,0,61,62,5,0,0,1,62,1,
        1,0,0,0,63,65,3,4,2,0,64,63,1,0,0,0,65,68,1,0,0,0,66,64,1,0,0,0,
        66,67,1,0,0,0,67,3,1,0,0,0,68,66,1,0,0,0,69,78,3,6,3,0,70,78,3,8,
        4,0,71,78,3,10,5,0,72,78,3,12,6,0,73,78,3,14,7,0,74,78,3,16,8,0,
        75,78,3,18,9,0,76,78,3,20,10,0,77,69,1,0,0,0,77,70,1,0,0,0,77,71,
        1,0,0,0,77,72,1,0,0,0,77,73,1,0,0,0,77,74,1,0,0,0,77,75,1,0,0,0,
        77,76,1,0,0,0,78,5,1,0,0,0,79,80,5,3,0,0,80,83,3,52,26,0,81,82,5,
        4,0,0,82,84,3,24,12,0,83,81,1,0,0,0,83,84,1,0,0,0,84,85,1,0,0,0,
        85,86,5,5,0,0,86,7,1,0,0,0,87,88,3,52,26,0,88,89,5,4,0,0,89,90,3,
        24,12,0,90,91,5,5,0,0,91,9,1,0,0,0,92,93,5,6,0,0,93,94,5,7,0,0,94,
        95,3,48,24,0,95,96,5,8,0,0,96,97,5,9,0,0,97,98,5,10,0,0,98,99,3,
        2,1,0,99,100,5,11,0,0,100,101,5,12,0,0,101,102,5,10,0,0,102,103,
        3,2,1,0,103,104,5,11,0,0,104,11,1,0,0,0,105,106,5,13,0,0,106,107,
        5,7,0,0,107,108,3,48,24,0,108,109,5,8,0,0,109,110,5,10,0,0,110,111,
        3,2,1,0,111,112,5,11,0,0,112,13,1,0,0,0,113,114,5,14,0,0,114,115,
        5,7,0,0,115,116,3,2,1,0,116,117,5,15,0,0,117,118,3,48,24,0,118,119,
        5,15,0,0,119,120,3,2,1,0,120,121,5,8,0,0,121,122,5,10,0,0,122,123,
        3,2,1,0,123,124,5,11,0,0,124,15,1,0,0,0,125,126,5,14,0,0,126,127,
        5,7,0,0,127,128,3,48,24,0,128,129,5,16,0,0,129,130,3,52,26,0,130,
        131,5,16,0,0,131,132,3,48,24,0,132,133,5,8,0,0,133,134,5,10,0,0,
        134,135,3,2,1,0,135,136,5,11,0,0,136,17,1,0,0,0,137,138,5,17,0,0,
        138,139,3,22,11,0,139,140,5,5,0,0,140,19,1,0,0,0,141,142,5,18,0,
        0,142,143,3,22,11,0,143,144,5,5,0,0,144,21,1,0,0,0,145,150,3,24,
        12,0,146,147,5,19,0,0,147,149,3,24,12,0,148,146,1,0,0,0,149,152,
        1,0,0,0,150,148,1,0,0,0,150,151,1,0,0,0,151,23,1,0,0,0,152,150,1,
        0,0,0,153,156,3,56,28,0,154,156,3,48,24,0,155,153,1,0,0,0,155,154,
        1,0,0,0,156,25,1,0,0,0,157,162,3,50,25,0,158,159,7,0,0,0,159,161,
        3,50,25,0,160,158,1,0,0,0,161,164,1,0,0,0,162,160,1,0,0,0,162,163,
        1,0,0,0,163,27,1,0,0,0,164,162,1,0,0,0,165,170,3,26,13,0,166,167,
        7,1,0,0,167,169,3,26,13,0,168,166,1,0,0,0,169,172,1,0,0,0,170,168,
        1,0,0,0,170,171,1,0,0,0,171,29,1,0,0,0,172,170,1,0,0,0,173,178,3,
        36,18,0,174,175,7,2,0,0,175,177,3,36,18,0,176,174,1,0,0,0,177,180,
        1,0,0,0,178,176,1,0,0,0,178,179,1,0,0,0,179,31,1,0,0,0,180,178,1,
        0,0,0,181,186,3,30,15,0,182,183,7,3,0,0,183,185,3,30,15,0,184,182,
        1,0,0,0,185,188,1,0,0,0,186,184,1,0,0,0,186,187,1,0,0,0,187,33,1,
        0,0,0,188,186,1,0,0,0,189,195,3,46,23,0,190,191,5,31,0,0,191,192,
        3,48,24,0,192,193,5,32,0,0,193,194,3,34,17,0,194,196,1,0,0,0,195,
        190,1,0,0,0,195,196,1,0,0,0,196,35,1,0,0,0,197,202,3,28,14,0,198,
        199,7,4,0,0,199,201,3,28,14,0,200,198,1,0,0,0,201,204,1,0,0,0,202,
        200,1,0,0,0,202,203,1,0,0,0,203,37,1,0,0,0,204,202,1,0,0,0,205,210,
        3,32,16,0,206,207,5,35,0,0,207,209,3,32,16,0,208,206,1,0,0,0,209,
        212,1,0,0,0,210,208,1,0,0,0,210,211,1,0,0,0,211,39,1,0,0,0,212,210,
        1,0,0,0,213,218,3,38,19,0,214,215,5,36,0,0,215,217,3,38,19,0,216,
        214,1,0,0,0,217,220,1,0,0,0,218,216,1,0,0,0,218,219,1,0,0,0,219,
        41,1,0,0,0,220,218,1,0,0,0,221,226,3,40,20,0,222,223,5,37,0,0,223,
        225,3,40,20,0,224,222,1,0,0,0,225,228,1,0,0,0,226,224,1,0,0,0,226,
        227,1,0,0,0,227,43,1,0,0,0,228,226,1,0,0,0,229,234,3,42,21,0,230,
        231,5,38,0,0,231,233,3,42,21,0,232,230,1,0,0,0,233,236,1,0,0,0,234,
        232,1,0,0,0,234,235,1,0,0,0,235,45,1,0,0,0,236,234,1,0,0,0,237,242,
        3,44,22,0,238,239,5,39,0,0,239,241,3,44,22,0,240,238,1,0,0,0,241,
        244,1,0,0,0,242,240,1,0,0,0,242,243,1,0,0,0,243,47,1,0,0,0,244,242,
        1,0,0,0,245,249,3,34,17,0,246,249,3,28,14,0,247,249,3,50,25,0,248,
        245,1,0,0,0,248,246,1,0,0,0,248,247,1,0,0,0,249,49,1,0,0,0,250,257,
        3,54,27,0,251,257,3,52,26,0,252,253,5,7,0,0,253,254,3,48,24,0,254,
        255,5,8,0,0,255,257,1,0,0,0,256,250,1,0,0,0,256,251,1,0,0,0,256,
        252,1,0,0,0,257,51,1,0,0,0,258,259,5,41,0,0,259,53,1,0,0,0,260,261,
        5,42,0,0,261,55,1,0,0,0,262,263,5,40,0,0,263,57,1,0,0,0,18,66,77,
        83,150,155,162,170,178,186,195,202,210,218,226,234,242,248,256
    ]

class BroLangParser ( Parser ):

    grammarFileName = "BroLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'dawg'", "'gg'", "'my g'", "'='", "';'", 
                     "'yolo'", "'('", "')'", "'pls'", "'{'", "'}'", "'sus'", 
                     "'let him cook'", "'until'", "'#'", "'::'", "'say no more'", 
                     "'say'", "','", "'*'", "'/'", "'%'", "'+'", "'-'", 
                     "'<'", "'>'", "'<='", "'>='", "'=='", "'!='", "'?'", 
                     "':'", "'<<'", "'>>'", "'&'", "'^'", "'|'", "'&&'", 
                     "'||'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "UNICODE_CHARS", "ID", "DECIMAL", "NEWLINE", "Whitespace" ]

    RULE_prog = 0
    RULE_block = 1
    RULE_command = 2
    RULE_declaration = 3
    RULE_assignment = 4
    RULE_ifthenelse = 5
    RULE_whileBlock = 6
    RULE_forBlock = 7
    RULE_forRange = 8
    RULE_print = 9
    RULE_println = 10
    RULE_vals = 11
    RULE_data = 12
    RULE_multiplicative = 13
    RULE_additive = 14
    RULE_relational = 15
    RULE_equality = 16
    RULE_conditionalExpr = 17
    RULE_shift = 18
    RULE_and = 19
    RULE_exclusiveOr = 20
    RULE_inclusiveOr = 21
    RULE_logicalAnd = 22
    RULE_logicalOr = 23
    RULE_expression = 24
    RULE_terminalData = 25
    RULE_identifier = 26
    RULE_number = 27
    RULE_string = 28

    ruleNames =  [ "prog", "block", "command", "declaration", "assignment", 
                   "ifthenelse", "whileBlock", "forBlock", "forRange", "print", 
                   "println", "vals", "data", "multiplicative", "additive", 
                   "relational", "equality", "conditionalExpr", "shift", 
                   "and", "exclusiveOr", "inclusiveOr", "logicalAnd", "logicalOr", 
                   "expression", "terminalData", "identifier", "number", 
                   "string" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    T__36=37
    T__37=38
    T__38=39
    UNICODE_CHARS=40
    ID=41
    DECIMAL=42
    NEWLINE=43
    Whitespace=44

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(BroLangParser.BlockContext,0)


        def EOF(self):
            return self.getToken(BroLangParser.EOF, 0)

        def getRuleIndex(self):
            return BroLangParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = BroLangParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(BroLangParser.T__0)
            self.state = 59
            self.block()
            self.state = 60
            self.match(BroLangParser.T__1)
            self.state = 61
            self.match(BroLangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def command(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BroLangParser.CommandContext)
            else:
                return self.getTypedRuleContext(BroLangParser.CommandContext,i)


        def getRuleIndex(self):
            return BroLangParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = BroLangParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2199023673416) != 0):
                self.state = 63
                self.command()
                self.state = 68
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self):
            return self.getTypedRuleContext(BroLangParser.DeclarationContext,0)


        def assignment(self):
            return self.getTypedRuleContext(BroLangParser.AssignmentContext,0)


        def ifthenelse(self):
            return self.getTypedRuleContext(BroLangParser.IfthenelseContext,0)


        def whileBlock(self):
            return self.getTypedRuleContext(BroLangParser.WhileBlockContext,0)


        def forBlock(self):
            return self.getTypedRuleContext(BroLangParser.ForBlockContext,0)


        def forRange(self):
            return self.getTypedRuleContext(BroLangParser.ForRangeContext,0)


        def print_(self):
            return self.getTypedRuleContext(BroLangParser.PrintContext,0)


        def println(self):
            return self.getTypedRuleContext(BroLangParser.PrintlnContext,0)


        def getRuleIndex(self):
            return BroLangParser.RULE_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommand" ):
                listener.enterCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommand" ):
                listener.exitCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommand" ):
                return visitor.visitCommand(self)
            else:
                return visitor.visitChildren(self)




    def command(self):

        localctx = BroLangParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_command)
        try:
            self.state = 77
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 69
                self.declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 70
                self.assignment()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 71
                self.ifthenelse()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 72
                self.whileBlock()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 73
                self.forBlock()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 74
                self.forRange()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 75
                self.print_()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 76
                self.println()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(BroLangParser.IdentifierContext,0)


        def data(self):
            return self.getTypedRuleContext(BroLangParser.DataContext,0)


        def getRuleIndex(self):
            return BroLangParser.RULE_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = BroLangParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(BroLangParser.T__2)
            self.state = 80
            self.identifier()
            self.state = 83
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 81
                self.match(BroLangParser.T__3)
                self.state = 82
                self.data()


            self.state = 85
            self.match(BroLangParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(BroLangParser.IdentifierContext,0)


        def data(self):
            return self.getTypedRuleContext(BroLangParser.DataContext,0)


        def getRuleIndex(self):
            return BroLangParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = BroLangParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.identifier()
            self.state = 88
            self.match(BroLangParser.T__3)
            self.state = 89
            self.data()
            self.state = 90
            self.match(BroLangParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfthenelseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.true_block = None # BlockContext
            self.false_block = None # BlockContext

        def expression(self):
            return self.getTypedRuleContext(BroLangParser.ExpressionContext,0)


        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BroLangParser.BlockContext)
            else:
                return self.getTypedRuleContext(BroLangParser.BlockContext,i)


        def getRuleIndex(self):
            return BroLangParser.RULE_ifthenelse

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfthenelse" ):
                listener.enterIfthenelse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfthenelse" ):
                listener.exitIfthenelse(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfthenelse" ):
                return visitor.visitIfthenelse(self)
            else:
                return visitor.visitChildren(self)




    def ifthenelse(self):

        localctx = BroLangParser.IfthenelseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_ifthenelse)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.match(BroLangParser.T__5)
            self.state = 93
            self.match(BroLangParser.T__6)
            self.state = 94
            self.expression()
            self.state = 95
            self.match(BroLangParser.T__7)
            self.state = 96
            self.match(BroLangParser.T__8)
            self.state = 97
            self.match(BroLangParser.T__9)
            self.state = 98
            localctx.true_block = self.block()
            self.state = 99
            self.match(BroLangParser.T__10)
            self.state = 100
            self.match(BroLangParser.T__11)
            self.state = 101
            self.match(BroLangParser.T__9)
            self.state = 102
            localctx.false_block = self.block()
            self.state = 103
            self.match(BroLangParser.T__10)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(BroLangParser.ExpressionContext,0)


        def block(self):
            return self.getTypedRuleContext(BroLangParser.BlockContext,0)


        def getRuleIndex(self):
            return BroLangParser.RULE_whileBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileBlock" ):
                listener.enterWhileBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileBlock" ):
                listener.exitWhileBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileBlock" ):
                return visitor.visitWhileBlock(self)
            else:
                return visitor.visitChildren(self)




    def whileBlock(self):

        localctx = BroLangParser.WhileBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_whileBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.match(BroLangParser.T__12)
            self.state = 106
            self.match(BroLangParser.T__6)
            self.state = 107
            self.expression()
            self.state = 108
            self.match(BroLangParser.T__7)
            self.state = 109
            self.match(BroLangParser.T__9)
            self.state = 110
            self.block()
            self.state = 111
            self.match(BroLangParser.T__10)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.pre = None # BlockContext
            self.post = None # BlockContext
            self.loop = None # BlockContext

        def expression(self):
            return self.getTypedRuleContext(BroLangParser.ExpressionContext,0)


        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BroLangParser.BlockContext)
            else:
                return self.getTypedRuleContext(BroLangParser.BlockContext,i)


        def getRuleIndex(self):
            return BroLangParser.RULE_forBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForBlock" ):
                listener.enterForBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForBlock" ):
                listener.exitForBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForBlock" ):
                return visitor.visitForBlock(self)
            else:
                return visitor.visitChildren(self)




    def forBlock(self):

        localctx = BroLangParser.ForBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_forBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.match(BroLangParser.T__13)
            self.state = 114
            self.match(BroLangParser.T__6)
            self.state = 115
            localctx.pre = self.block()
            self.state = 116
            self.match(BroLangParser.T__14)
            self.state = 117
            self.expression()
            self.state = 118
            self.match(BroLangParser.T__14)
            self.state = 119
            localctx.post = self.block()
            self.state = 120
            self.match(BroLangParser.T__7)
            self.state = 121
            self.match(BroLangParser.T__9)
            self.state = 122
            localctx.loop = self.block()
            self.state = 123
            self.match(BroLangParser.T__10)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForRangeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.start = None # ExpressionContext
            self.end = None # ExpressionContext

        def identifier(self):
            return self.getTypedRuleContext(BroLangParser.IdentifierContext,0)


        def block(self):
            return self.getTypedRuleContext(BroLangParser.BlockContext,0)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BroLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BroLangParser.ExpressionContext,i)


        def getRuleIndex(self):
            return BroLangParser.RULE_forRange

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForRange" ):
                listener.enterForRange(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForRange" ):
                listener.exitForRange(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForRange" ):
                return visitor.visitForRange(self)
            else:
                return visitor.visitChildren(self)




    def forRange(self):

        localctx = BroLangParser.ForRangeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_forRange)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.match(BroLangParser.T__13)
            self.state = 126
            self.match(BroLangParser.T__6)
            self.state = 127
            localctx.start = self.expression()
            self.state = 128
            self.match(BroLangParser.T__15)
            self.state = 129
            self.identifier()
            self.state = 130
            self.match(BroLangParser.T__15)
            self.state = 131
            localctx.end = self.expression()
            self.state = 132
            self.match(BroLangParser.T__7)
            self.state = 133
            self.match(BroLangParser.T__9)
            self.state = 134
            self.block()
            self.state = 135
            self.match(BroLangParser.T__10)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vals(self):
            return self.getTypedRuleContext(BroLangParser.ValsContext,0)


        def getRuleIndex(self):
            return BroLangParser.RULE_print

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint" ):
                listener.enterPrint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint" ):
                listener.exitPrint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint" ):
                return visitor.visitPrint(self)
            else:
                return visitor.visitChildren(self)




    def print_(self):

        localctx = BroLangParser.PrintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_print)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.match(BroLangParser.T__16)
            self.state = 138
            self.vals()
            self.state = 139
            self.match(BroLangParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintlnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vals(self):
            return self.getTypedRuleContext(BroLangParser.ValsContext,0)


        def getRuleIndex(self):
            return BroLangParser.RULE_println

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintln" ):
                listener.enterPrintln(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintln" ):
                listener.exitPrintln(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintln" ):
                return visitor.visitPrintln(self)
            else:
                return visitor.visitChildren(self)




    def println(self):

        localctx = BroLangParser.PrintlnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_println)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.match(BroLangParser.T__17)
            self.state = 142
            self.vals()
            self.state = 143
            self.match(BroLangParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._data = None # DataContext
            self.data_terms = list() # of DataContexts

        def data(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BroLangParser.DataContext)
            else:
                return self.getTypedRuleContext(BroLangParser.DataContext,i)


        def getRuleIndex(self):
            return BroLangParser.RULE_vals

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVals" ):
                listener.enterVals(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVals" ):
                listener.exitVals(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVals" ):
                return visitor.visitVals(self)
            else:
                return visitor.visitChildren(self)




    def vals(self):

        localctx = BroLangParser.ValsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_vals)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            localctx._data = self.data()
            localctx.data_terms.append(localctx._data)
            self.state = 150
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==19:
                self.state = 146
                self.match(BroLangParser.T__18)
                self.state = 147
                localctx._data = self.data()
                localctx.data_terms.append(localctx._data)
                self.state = 152
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DataContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def string(self):
            return self.getTypedRuleContext(BroLangParser.StringContext,0)


        def expression(self):
            return self.getTypedRuleContext(BroLangParser.ExpressionContext,0)


        def getRuleIndex(self):
            return BroLangParser.RULE_data

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterData" ):
                listener.enterData(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitData" ):
                listener.exitData(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitData" ):
                return visitor.visitData(self)
            else:
                return visitor.visitChildren(self)




    def data(self):

        localctx = BroLangParser.DataContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_data)
        try:
            self.state = 155
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [40]:
                self.enterOuterAlt(localctx, 1)
                self.state = 153
                self.string()
                pass
            elif token in [7, 41, 42]:
                self.enterOuterAlt(localctx, 2)
                self.state = 154
                self.expression()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplicativeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._terminalData = None # TerminalDataContext
            self.oprs = list() # of TerminalDataContexts
            self.s20 = None # Token
            self.ops = list() # of Tokens
            self.s21 = None # Token
            self.s22 = None # Token
            self._tset283 = None # Token

        def terminalData(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BroLangParser.TerminalDataContext)
            else:
                return self.getTypedRuleContext(BroLangParser.TerminalDataContext,i)


        def getRuleIndex(self):
            return BroLangParser.RULE_multiplicative

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicative" ):
                listener.enterMultiplicative(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicative" ):
                listener.exitMultiplicative(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicative" ):
                return visitor.visitMultiplicative(self)
            else:
                return visitor.visitChildren(self)




    def multiplicative(self):

        localctx = BroLangParser.MultiplicativeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_multiplicative)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            localctx._terminalData = self.terminalData()
            localctx.oprs.append(localctx._terminalData)
            self.state = 162
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 7340032) != 0):
                self.state = 158
                localctx._tset283 = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7340032) != 0)):
                    localctx._tset283 = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                localctx.ops.append(localctx._tset283)
                self.state = 159
                localctx._terminalData = self.terminalData()
                localctx.oprs.append(localctx._terminalData)
                self.state = 164
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdditiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._multiplicative = None # MultiplicativeContext
            self.oprs = list() # of MultiplicativeContexts
            self.s23 = None # Token
            self.ops = list() # of Tokens
            self.s24 = None # Token
            self._tset310 = None # Token

        def multiplicative(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BroLangParser.MultiplicativeContext)
            else:
                return self.getTypedRuleContext(BroLangParser.MultiplicativeContext,i)


        def getRuleIndex(self):
            return BroLangParser.RULE_additive

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditive" ):
                listener.enterAdditive(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditive" ):
                listener.exitAdditive(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditive" ):
                return visitor.visitAdditive(self)
            else:
                return visitor.visitChildren(self)




    def additive(self):

        localctx = BroLangParser.AdditiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_additive)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            localctx._multiplicative = self.multiplicative()
            localctx.oprs.append(localctx._multiplicative)
            self.state = 170
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==23 or _la==24:
                self.state = 166
                localctx._tset310 = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==23 or _la==24):
                    localctx._tset310 = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                localctx.ops.append(localctx._tset310)
                self.state = 167
                localctx._multiplicative = self.multiplicative()
                localctx.oprs.append(localctx._multiplicative)
                self.state = 172
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._shift = None # ShiftContext
            self.oprs = list() # of ShiftContexts
            self.s25 = None # Token
            self.ops = list() # of Tokens
            self.s26 = None # Token
            self.s27 = None # Token
            self.s28 = None # Token
            self._tset335 = None # Token

        def shift(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BroLangParser.ShiftContext)
            else:
                return self.getTypedRuleContext(BroLangParser.ShiftContext,i)


        def getRuleIndex(self):
            return BroLangParser.RULE_relational

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelational" ):
                listener.enterRelational(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelational" ):
                listener.exitRelational(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelational" ):
                return visitor.visitRelational(self)
            else:
                return visitor.visitChildren(self)




    def relational(self):

        localctx = BroLangParser.RelationalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_relational)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            localctx._shift = self.shift()
            localctx.oprs.append(localctx._shift)
            self.state = 178
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 503316480) != 0):
                self.state = 174
                localctx._tset335 = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 503316480) != 0)):
                    localctx._tset335 = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                localctx.ops.append(localctx._tset335)
                self.state = 175
                localctx._shift = self.shift()
                localctx.oprs.append(localctx._shift)
                self.state = 180
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EqualityContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._relational = None # RelationalContext
            self.oprs = list() # of RelationalContexts
            self.s29 = None # Token
            self.ops = list() # of Tokens
            self.s30 = None # Token
            self._tset364 = None # Token

        def relational(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BroLangParser.RelationalContext)
            else:
                return self.getTypedRuleContext(BroLangParser.RelationalContext,i)


        def getRuleIndex(self):
            return BroLangParser.RULE_equality

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEquality" ):
                listener.enterEquality(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEquality" ):
                listener.exitEquality(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEquality" ):
                return visitor.visitEquality(self)
            else:
                return visitor.visitChildren(self)




    def equality(self):

        localctx = BroLangParser.EqualityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_equality)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            localctx._relational = self.relational()
            localctx.oprs.append(localctx._relational)
            self.state = 186
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==29 or _la==30:
                self.state = 182
                localctx._tset364 = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==29 or _la==30):
                    localctx._tset364 = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                localctx.ops.append(localctx._tset364)
                self.state = 183
                localctx._relational = self.relational()
                localctx.oprs.append(localctx._relational)
                self.state = 188
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionalExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.condition = None # LogicalOrContext
            self.true_block = None # ExpressionContext
            self.false_block = None # ConditionalExprContext

        def logicalOr(self):
            return self.getTypedRuleContext(BroLangParser.LogicalOrContext,0)


        def expression(self):
            return self.getTypedRuleContext(BroLangParser.ExpressionContext,0)


        def conditionalExpr(self):
            return self.getTypedRuleContext(BroLangParser.ConditionalExprContext,0)


        def getRuleIndex(self):
            return BroLangParser.RULE_conditionalExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditionalExpr" ):
                listener.enterConditionalExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditionalExpr" ):
                listener.exitConditionalExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditionalExpr" ):
                return visitor.visitConditionalExpr(self)
            else:
                return visitor.visitChildren(self)




    def conditionalExpr(self):

        localctx = BroLangParser.ConditionalExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_conditionalExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            localctx.condition = self.logicalOr()
            self.state = 195
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==31:
                self.state = 190
                self.match(BroLangParser.T__30)
                self.state = 191
                localctx.true_block = self.expression()
                self.state = 192
                self.match(BroLangParser.T__31)
                self.state = 193
                localctx.false_block = self.conditionalExpr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ShiftContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._additive = None # AdditiveContext
            self.oprs = list() # of AdditiveContexts
            self.s33 = None # Token
            self.ops = list() # of Tokens
            self.s34 = None # Token
            self._tset416 = None # Token

        def additive(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BroLangParser.AdditiveContext)
            else:
                return self.getTypedRuleContext(BroLangParser.AdditiveContext,i)


        def getRuleIndex(self):
            return BroLangParser.RULE_shift

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterShift" ):
                listener.enterShift(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitShift" ):
                listener.exitShift(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitShift" ):
                return visitor.visitShift(self)
            else:
                return visitor.visitChildren(self)




    def shift(self):

        localctx = BroLangParser.ShiftContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_shift)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            localctx._additive = self.additive()
            localctx.oprs.append(localctx._additive)
            self.state = 202
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==33 or _la==34:
                self.state = 198
                localctx._tset416 = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==33 or _la==34):
                    localctx._tset416 = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                localctx.ops.append(localctx._tset416)
                self.state = 199
                localctx._additive = self.additive()
                localctx.oprs.append(localctx._additive)
                self.state = 204
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AndContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._equality = None # EqualityContext
            self.oprs = list() # of EqualityContexts

        def equality(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BroLangParser.EqualityContext)
            else:
                return self.getTypedRuleContext(BroLangParser.EqualityContext,i)


        def getRuleIndex(self):
            return BroLangParser.RULE_and

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnd" ):
                listener.enterAnd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnd" ):
                listener.exitAnd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAnd" ):
                return visitor.visitAnd(self)
            else:
                return visitor.visitChildren(self)




    def and_(self):

        localctx = BroLangParser.AndContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_and)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            localctx._equality = self.equality()
            localctx.oprs.append(localctx._equality)
            self.state = 210
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==35:
                self.state = 206
                self.match(BroLangParser.T__34)
                self.state = 207
                localctx._equality = self.equality()
                localctx.oprs.append(localctx._equality)
                self.state = 212
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExclusiveOrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._and = None # AndContext
            self.oprs = list() # of AndContexts

        def and_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BroLangParser.AndContext)
            else:
                return self.getTypedRuleContext(BroLangParser.AndContext,i)


        def getRuleIndex(self):
            return BroLangParser.RULE_exclusiveOr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExclusiveOr" ):
                listener.enterExclusiveOr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExclusiveOr" ):
                listener.exitExclusiveOr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExclusiveOr" ):
                return visitor.visitExclusiveOr(self)
            else:
                return visitor.visitChildren(self)




    def exclusiveOr(self):

        localctx = BroLangParser.ExclusiveOrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_exclusiveOr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            localctx._and = self.and_()
            localctx.oprs.append(localctx._and)
            self.state = 218
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==36:
                self.state = 214
                self.match(BroLangParser.T__35)
                self.state = 215
                localctx._and = self.and_()
                localctx.oprs.append(localctx._and)
                self.state = 220
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InclusiveOrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._exclusiveOr = None # ExclusiveOrContext
            self.oprs = list() # of ExclusiveOrContexts

        def exclusiveOr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BroLangParser.ExclusiveOrContext)
            else:
                return self.getTypedRuleContext(BroLangParser.ExclusiveOrContext,i)


        def getRuleIndex(self):
            return BroLangParser.RULE_inclusiveOr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInclusiveOr" ):
                listener.enterInclusiveOr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInclusiveOr" ):
                listener.exitInclusiveOr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInclusiveOr" ):
                return visitor.visitInclusiveOr(self)
            else:
                return visitor.visitChildren(self)




    def inclusiveOr(self):

        localctx = BroLangParser.InclusiveOrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_inclusiveOr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            localctx._exclusiveOr = self.exclusiveOr()
            localctx.oprs.append(localctx._exclusiveOr)
            self.state = 226
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==37:
                self.state = 222
                self.match(BroLangParser.T__36)
                self.state = 223
                localctx._exclusiveOr = self.exclusiveOr()
                localctx.oprs.append(localctx._exclusiveOr)
                self.state = 228
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalAndContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._inclusiveOr = None # InclusiveOrContext
            self.oprs = list() # of InclusiveOrContexts

        def inclusiveOr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BroLangParser.InclusiveOrContext)
            else:
                return self.getTypedRuleContext(BroLangParser.InclusiveOrContext,i)


        def getRuleIndex(self):
            return BroLangParser.RULE_logicalAnd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalAnd" ):
                listener.enterLogicalAnd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalAnd" ):
                listener.exitLogicalAnd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalAnd" ):
                return visitor.visitLogicalAnd(self)
            else:
                return visitor.visitChildren(self)




    def logicalAnd(self):

        localctx = BroLangParser.LogicalAndContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_logicalAnd)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            localctx._inclusiveOr = self.inclusiveOr()
            localctx.oprs.append(localctx._inclusiveOr)
            self.state = 234
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==38:
                self.state = 230
                self.match(BroLangParser.T__37)
                self.state = 231
                localctx._inclusiveOr = self.inclusiveOr()
                localctx.oprs.append(localctx._inclusiveOr)
                self.state = 236
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalOrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._logicalAnd = None # LogicalAndContext
            self.oprs = list() # of LogicalAndContexts

        def logicalAnd(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BroLangParser.LogicalAndContext)
            else:
                return self.getTypedRuleContext(BroLangParser.LogicalAndContext,i)


        def getRuleIndex(self):
            return BroLangParser.RULE_logicalOr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalOr" ):
                listener.enterLogicalOr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalOr" ):
                listener.exitLogicalOr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalOr" ):
                return visitor.visitLogicalOr(self)
            else:
                return visitor.visitChildren(self)




    def logicalOr(self):

        localctx = BroLangParser.LogicalOrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_logicalOr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            localctx._logicalAnd = self.logicalAnd()
            localctx.oprs.append(localctx._logicalAnd)
            self.state = 242
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==39:
                self.state = 238
                self.match(BroLangParser.T__38)
                self.state = 239
                localctx._logicalAnd = self.logicalAnd()
                localctx.oprs.append(localctx._logicalAnd)
                self.state = 244
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def conditionalExpr(self):
            return self.getTypedRuleContext(BroLangParser.ConditionalExprContext,0)


        def additive(self):
            return self.getTypedRuleContext(BroLangParser.AdditiveContext,0)


        def terminalData(self):
            return self.getTypedRuleContext(BroLangParser.TerminalDataContext,0)


        def getRuleIndex(self):
            return BroLangParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = BroLangParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_expression)
        try:
            self.state = 248
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 245
                self.conditionalExpr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 246
                self.additive()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 247
                self.terminalData()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TerminalDataContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def number(self):
            return self.getTypedRuleContext(BroLangParser.NumberContext,0)


        def identifier(self):
            return self.getTypedRuleContext(BroLangParser.IdentifierContext,0)


        def expression(self):
            return self.getTypedRuleContext(BroLangParser.ExpressionContext,0)


        def getRuleIndex(self):
            return BroLangParser.RULE_terminalData

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerminalData" ):
                listener.enterTerminalData(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerminalData" ):
                listener.exitTerminalData(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerminalData" ):
                return visitor.visitTerminalData(self)
            else:
                return visitor.visitChildren(self)




    def terminalData(self):

        localctx = BroLangParser.TerminalDataContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_terminalData)
        try:
            self.state = 256
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [42]:
                self.enterOuterAlt(localctx, 1)
                self.state = 250
                self.number()
                pass
            elif token in [41]:
                self.enterOuterAlt(localctx, 2)
                self.state = 251
                self.identifier()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 3)
                self.state = 252
                self.match(BroLangParser.T__6)
                self.state = 253
                self.expression()
                self.state = 254
                self.match(BroLangParser.T__7)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BroLangParser.ID, 0)

        def getRuleIndex(self):
            return BroLangParser.RULE_identifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifier" ):
                listener.enterIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifier" ):
                listener.exitIdentifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifier" ):
                return visitor.visitIdentifier(self)
            else:
                return visitor.visitChildren(self)




    def identifier(self):

        localctx = BroLangParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            self.match(BroLangParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DECIMAL(self):
            return self.getToken(BroLangParser.DECIMAL, 0)

        def getRuleIndex(self):
            return BroLangParser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber" ):
                return visitor.visitNumber(self)
            else:
                return visitor.visitChildren(self)




    def number(self):

        localctx = BroLangParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self.match(BroLangParser.DECIMAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def UNICODE_CHARS(self):
            return self.getToken(BroLangParser.UNICODE_CHARS, 0)

        def getRuleIndex(self):
            return BroLangParser.RULE_string

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString" ):
                return visitor.visitString(self)
            else:
                return visitor.visitChildren(self)




    def string(self):

        localctx = BroLangParser.StringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_string)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            self.match(BroLangParser.UNICODE_CHARS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





