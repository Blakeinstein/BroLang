grammar BroLang;

prog
    :   'dawg' block 'gg' EOF ;
block
    :   command* ;
command
    :   declaration | assignment | ifthenelse | whileBlock | forBlock | forRange | print | println ;
declaration
    :   'my g' identifier ('=' data)? ';' ;
assignment
    :   identifier '=' data ';' ;

ifthenelse
    :   'yolo' '(' expression ')' 'pls' '{' true_block=block '}' 'sus' '{' false_block=block '}' ;
whileBlock
    :   'let him cook' '(' expression ')' '{' block '}' ;
forBlock
    :   'until' '(' pre=block '#' expression '#' post=block ')' '{' loop=block '}'
    ;
forRange
    :   'until' '(' start=expression '::' identifier '::' end=expression ')' '{' block '}' 
    ;
print
    :   'say no more' vals ';' ;
println
    :   'say' vals ';' ;

vals
    :   data_terms+=data (',' data_terms+=data)* ;
data
    :   string | expression ;

multiplicative
    :   oprs+=terminalData (ops+=('*'|'/'|'%') oprs+=terminalData)*
    ;

additive
    :   oprs+=multiplicative (ops+=('+'|'-') oprs+=multiplicative)*
    ;


relational
    :   oprs+=shift (ops+=('<'|'>'|'<='|'>=') oprs+=shift)*
    ;

equality
    :   oprs+=relational (ops+=('==' | '!=') oprs+=relational)*
    ;

conditionalExpr
    :   condition=logicalOr ('?' true_block=expression ':' false_block=conditionalExpr)?
    ;

shift
    :   oprs+=additive (ops+=('<<'|'>>') oprs+=additive)*
    ;

and
    :   oprs+=equality ('&' oprs+=equality)*
    ;

exclusiveOr
    :   oprs+=and ('^' oprs+=and)*
    ;

inclusiveOr
    :   oprs+=exclusiveOr ('|' oprs+=exclusiveOr)*
    ;

logicalAnd
    :   oprs+=inclusiveOr ('&&' oprs+=inclusiveOr)*
    ;

logicalOr
    :   oprs+=logicalAnd ( '||' oprs+=logicalAnd)*
    ;

expression
    :   conditionalExpr
    |   additive
    |   negation
    |   terminalData
    ;

terminalData
    :   number
    |   identifier
    |   '(' expression ')'
    ;

negation
    : '!' terminalData
    ;

identifier
    : ID
    ;

number
    : DECIMAL
    ;

string
    : UNICODE_CHARS
    ;

UNICODE_CHARS
    :   '"' ( '\\' ~[\r\n] | ~[\\"\r\n] )* '"'
    ;

ID
    :   [a-zA-Z][a-zA-Z0-9]* 
    ;

DECIMAL
    :   [0-9]+'.'?[0-9]*
    ;

NEWLINE
    :   [\r\n]+ -> skip
    ;

Whitespace
    :   [ \t]+ -> skip
    ;
