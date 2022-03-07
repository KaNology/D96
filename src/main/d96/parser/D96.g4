// Student name: Lê Thiên Ân
// Student ID: 1852255

grammar D96;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    result = super().emit()
    if tk == self.UNCLOSE_STRING:
        raise UncloseString(result.text[1:])
    elif tk == self.ILLEGAL_ESCAPE:
        raise IllegalEscape(result.text[1:])
    elif tk == self.ERROR_CHAR:
        raise ErrorToken(result.text)
    else:
        return result;
}

options {
	language = Python3;
}

program: classDeclaration+ EOF;

// Class Declaration

classDeclaration: CLASS ID (COLON ID)? LP classBody RP;

classBody: (attrDeclaration | methodDeclaration)*;

// Attribute Declaration

// attrDeclaration locals [
//     int attr_counter = 1,
//     int exp_counter = 1
// ]
// : (VAL | VAR) attrList COLON typeName 
// (
//     ASSIGN 
//     (
//         exp (
//             {$exp_counter <= $attr_counter}? (COMMA exp) {$exp_counter = $exp_counter + 1}
//         )* 
//         )
// )?
// SEMI;

// attrList: identifier (COMMA identifier {$attrDeclaration::attr_counter = $attrDeclaration::attr_counter + 1})*;

attrDeclaration: ((VAL | VAR) (attrWithAssign | attrWithoutAssign) SEMI);

attrWithAssign: identifier attrPair exp;

attrPair: COMMA identifier attrPair exp COMMA | COLON typeName ASSIGN;

attrWithoutAssign: attrList COLON typeName;

attrList: identifier (COMMA identifier)*;

identifier: (ID | DOLLAR_ID);

typeName: primitiveType | arrayType | classType;

// Method Declaration

methodDeclaration: (identifier LB paraList? RB 
| CONSTRUCTOR LB paraList? RB
| DESTRUCTOR LB RB) blockStmt;

paraList: paraDeclaration (SEMI paraDeclaration)*;

paraDeclaration: idList COLON typeName;

idList: ID (COMMA ID)*;

// Type and Value

// Primitive Types

primitiveType: BOOLEAN | INT | FLOAT | STRING;

// Array Type

arrayType: ARRAY LS elementType COMMA intLit RS;

elementType: primitiveType | arrayType;

// Class Type

classType: ID;

// Statements

stmt: assignStmt | ifStmt | forInStmt | breakStmt | continueStmt | returnStmt | instanceCall | staticCall | declarationStmt | blockStmt;

// Variable and Constant Declaration Statement

// // this make sure that the *exp* number doesn't EXCEED the *var* number

// declarationStmt locals [
//     int var_counter = 1,
//     int exp_counter = 1
// ]
// : (VAL | VAR) varList COLON typeName 
// (
//     ASSIGN (exp (
//         {$exp_counter <= $var_counter}? (COMMA exp) {$exp_counter = $exp_counter + 1}
//         )*)
// )? SEMI;

// varList: ID (COMMA ID {$declarationStmt::var_counter = $declarationStmt::var_counter + 1})*;

// // this doesn't make sure the *var* number are equal to the *exp* number

// declarationStmt: (VAL | VAR) varList COLON typeName (ASSIGN exp (COMMA exp)*)? SEMI;

// This satisfies both conditions

declarationStmt: ((VAL | VAR) (declarationWithAssign | declarationWithoutAssign) SEMI);

declarationWithAssign: ID declarationPair exp;

declarationPair: COMMA ID declarationPair exp COMMA | COLON typeName ASSIGN;

declarationWithoutAssign: varList COLON typeName;

varList: ID (COMMA ID)*;

// Assignment Statement

assignStmt: assignLHS ASSIGN exp SEMI;

assignLHS: indexOperation | scalar;

scalar: exp DOT ID | ID DOUBLECOLON DOLLAR_ID | ID;

// indexOperation: indexHead (LS exp RS)+;
indexOperation: exp7;

indexHead: exp;

// If Statement

ifStmt: IF ifBody (ELSEIF ifBody)* (ELSE blockStmt)? ;

ifBody: LB exp RB blockStmt;

// For/In Statement

forInStmt: FOREACH LB scalar IN exp DOUBLEDOT exp (BY exp)? RB blockStmt;

// Break Statement

breakStmt: BREAK SEMI;

// Continue Statement

continueStmt: CONTINUE SEMI;

// Return Statement

returnStmt: RETURN exp? SEMI;

// Method Invocation Statement

instanceCall: exp DOT ID LB expList? RB SEMI;

staticCall: ID DOUBLECOLON DOLLAR_ID LB expList? RB SEMI;

// Block Statement

blockStmt: LP stmt* RP;

// Expressions

exp: exp (STRADD | STREQ) exp | exp1; // String

exp1: exp1 (EQUAL | DIFF | LT | LTE | GT | GTE) exp1 | exp2; // Relational

exp2: exp2 (AND | OR) exp3 | exp3; // Logical

exp3: exp3 (ADD | MINUS) exp4 | exp4; // Adding

exp4: exp4 (MUL | DIV | MOD) exp5 | exp5; // Multiplying

exp5: NOT exp5 | exp6; // Logical

exp6: MINUS exp6 | exp7; // Sign

exp7: exp7 (LS exp RS)+ | exp8; // Index Operator

exp8: exp8 DOT ID (LB expList? RB)? | exp9; // Instance Access

exp9: ID DOUBLECOLON DOLLAR_ID (LB expList? RB)? | exp10; // Static Access

exp10: NEW ID LB expList? RB | exp11; // Object Creation

exp11: LB exp RB | operand;

expList: exp (COMMA exp)*;

operand: ID /* for class type and ID */ | ZERO | intLit | FLOATLIT | STRINGLIT | booleanLit | indexArray | SELF | NULL;

// Indexed Array and Multi-dimensional Array

indexArray: ARRAY LB arrayBody? RB;

arrayBody: arrayLit (COMMA arrayLit)*;

arrayLit: exp | indexArray;

// Lexical Structure

// Keywords

BREAK: 'Break';

CONTINUE: 'Continue';

IF: 'If';

ELSEIF: 'Elseif';

ELSE: 'Else';

FOREACH: 'Foreach';

TRUE: 'True';

FALSE: 'False';

ARRAY: 'Array';

IN: 'In';

INT: 'Int';

FLOAT: 'Float';

BOOLEAN: 'Boolean';

STRING: 'String';

RETURN: 'Return';

NULL: 'Null';

CLASS: 'Class';

VAL: 'Val';

VAR: 'Var';

SELF: 'Self';

CONSTRUCTOR: 'Constructor';

DESTRUCTOR: 'Destructor';

NEW: 'New';

BY: 'By';

// Separators

LB: '(';

RB: ')';

LS: '[';

RS: ']';

DOT: '.';

COMMA: ',';

SEMI: ';';

LP: '{';

RP: '}';

COLON: ':';

// Operators

ADD: '+';

MINUS: '-';

MUL: '*';

DIV: '/';

MOD: '%';

NOT: '!';

AND: '&&';

OR: '||';

EQUAL: '==';

ASSIGN: '=';

DIFF: '!=';

GT: '>';

GTE: '>=';

LT: '<';

LTE: '<=';

STREQ: '==.';

STRADD: '+.';

DOUBLECOLON: '::';

DOUBLEDOT: '..';

// Literals

ZERO: '0' | '00' | '0'[xX]'0' | '0'[bB]'0';

// Integers

intLit: (DECINT | OCTINT | HEXINT | BIINT);

DECINT: [1-9]('_'?[0-9])* {
y = str(self.text)
x = y.replace("_", "")
self.text = x[0:]
};

OCTINT: '0'[1-7]('_'?[0-7])*{
y = str(self.text)
x = y.replace("_", "")
self.text = x[0:]
};

HEXINT: '0'[xX][1-9A-F]('_'?[0-9A-F])*{
y = str(self.text)
x = y.replace("_", "")
self.text = x[0:]
};

BIINT: '0'[bB][1]('_'?[0-1])*{
y = str(self.text)
x = y.replace("_", "")
self.text = x[0:]
};

// Float

FLOATLIT: (INTFLOAT DECFLOAT? EXPFLOAT | INTFLOAT DECFLOAT | DECFLOAT EXPFLOAT){
y = str(self.text)
x = y.replace("_", "")
self.text = x[0:]
};

fragment INTFLOAT: [0-9]('_'?[0-9])*;

fragment DECFLOAT: DOT [0-9]*;

fragment EXPFLOAT: [eE] [-+]? [0-9]+;

// Boolean

booleanLit: TRUE | FALSE;

// String

STRINGLIT: '"' STRINGBODY* '"' {
y = str(self.text)
self.text = y[1:-1]
};

fragment STRINGBODY: (~[\\"\b\f\r\n\t] | '\'"' | STRING_ESCAPE);

fragment STRING_ESCAPE: '\\' [bfrnt'\\];

// Identifiers

ID: [_a-zA-Z][_a-zA-Z0-9]*;

DOLLAR_ID: '$' [_a-zA-Z0-9]+;

// Program Comment

COMMENT: '##' .*? '##' -> skip;

WS: [ \t\b\f\r\n]+ -> skip; // skip spaces, tabs, backspace, form feed, carriage return, newlines

ERROR_CHAR: . {raise ErrorToken(self.text)};

UNCLOSE_STRING: '"' STRINGBODY* ( [\b\t\n\f\r'"\\] | EOF ) {
y = str(self.text)
error = ['\b', '\t', '\n', '\f', '\r' , '"', "'", '\\']
if y[-1] in error:
	raise UncloseString(y[1:-1])
else:
    raise UncloseString(y[1:])
};

ILLEGAL_ESCAPE: '"' STRINGBODY* ('\\' ~[bfrnt'\\] | ~'\\') {
y = str(self.text)
raise IllegalEscape(y[1:])
};

// UNTERMINATED_COMMENT: '##' ('#' ~'#' | ~'#')* EOF 
// {
// raise UnterminatedComment()
// }
// ;