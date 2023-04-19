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