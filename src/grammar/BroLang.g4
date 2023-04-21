grammar BroLang;

prog
    :   'dawg' block 'gg' EOF ;
block
    :   command* ;
command
    :   declaration | assignment | ifthenelse | whileb | forb | print | println ;
declaration
    :   'my g' identifier ('=' data)? ';' ;
assignment
    :   identifier '=' data ';' ;

ifthenelse
    :   'yolo' '(' expression ')' 'pls' '{' block '}' 'sus' '{' block '}' ;
whileb
    :   'let him cook' '(' expression ')' '{' block '}' ;
forb
    :   'until' '(' block ';' expression ';' block ')' '{' block '}' | 'until' '(' expression '::' ID '::' expression ')' '{' block '}' ;
print
    :   'say no more' vals ';' ;
println
    :   'say' vals ';' ;

vals
    :   data (',' data)* ;
data
    :   STRING | expression ;

multiplicative
    :   terminal (('*'|'/'|'%') terminal)*
    ;

additive
    :   multiplicative (('+'|'-') multiplicative)*
    ;

shift
    :   additive (('<<'|'>>') additive)*
    ;

relational
    :   shift (('<'|'>'|'<='|'>=') shift)*
    ;

equality
    :   relational (('=='| '!=') relational)*
    ;

and
    :   equality ( '&' equality)*
    ;

exclusiveOr
    :   and ('^' and)*
    ;

inclusiveOr
    :   exclusiveOr ('|' exclusiveOr)*
    ;

logicalAnd
    :   inclusiveOr ('&&' inclusiveOr)*
    ;

logicalOr
    :   logicalAnd ( '||' logicalAnd)*
    ;

conditional
    :   logicalOr ('?' expression ':' conditional)?
    ;

expression
    :   conditional
    |   additive
    |   terminal
    ;

terminal
    :   number
    |   identifier
    |   '(' expression ')'
    ;

identifier
    : ID
    ;

number
    : DECIMAL
    ;

STRING
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
