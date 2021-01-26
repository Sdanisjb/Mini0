grammar Gramatica;
programa  :    NL* decl decl* EOF;

decl  : funcion | glbal;

nl         : NL NL*;

glbal     :  declvar nl;

funcion     :  FUN ID LEFTPAREN params RIGHTPAREN (COLON tipo)? nl

               bloque

            END nl
            ;

bloque      :  (declvar nl)* (comando nl)*;

params     :  /*vacio*/ | parametro ( COMMA parametro );

parametro  : ID COLON tipo;

tipo      : tipobase | LEFTBRACKET RIGHTBRACKET tipo;

tipobase   :  INT | BOOL | CHAR | STRING;

declvar    :  ID COLON tipo;

comando    :  cmdif | cmdwhile | cmdasign | cmdreturn | llamada;

cmdif     :  IF exp nl

              bloque

              ( ELSE IF exp nl

                 bloque

              )

              ( ELSE nl

                 bloque

              )?

             END
            ;
cmdwhile   : WHILE exp nl

               bloque

             LOOP
             ;

cmdasign   : var EQUAL exp;

llamada   :  ID LEFTPAREN listaexp RIGHTPAREN;

listaexp  : /*vacio*/ | exp ( COMMA exp )* ;

cmdreturn : RETURN exp | RETURN ;

var       : ID | var LEFTBRACKET exp RIGHTBRACKET;

exp       :  LITNUMERAL

          | LITSTRING

          | TRUE

          | FALSE

          | var

          | NEW LEFTBRACKET exp RIGHTBRACKET tipo

          | LEFTPAREN exp RIGHTPAREN

          | llamada

          | exp PLUS exp

          | exp MINUS exp

          | exp STAR exp

          | exp DIV exp

          | exp GREATER exp

          | exp LESS exp

          | exp GREATEREQUAL exp

          | exp LESSEQUAL exp

          | exp EQUAL exp

          | exp DIFFERENT exp

          | exp AND exp

          | exp OR exp

          | NOT exp

          | MINUS exp
          ;

NL: ( '\n' )+;
ID: ([a-zA-Z_]) ([a-zA-Z_]|[0-9])*;
LITNUMERAL: ( [0-9]+ | '0x'[0-9a-fA-F]+ );
LITSTRING: '"' ('\\' | '\n' | '\t' | '”' | [a-zA-Z]|[0-9])+  '"';
TRUE: 'true';
FALSE: 'false';
IF: 'if';
ELSE: 'else';
END: 'end';
WHILE: 'while';
LOOP: 'loop';
FUN: 'fun';
RETURN: 'return';
NEW: 'new';
STRING: 'string';
INT: 'int';
CHAR: 'char';
BOOL: 'bool';
AND: 'and';
OR: 'or';
NOT: 'not';

LESS: '<';
GREATER: '>';
LEFTPAREN: '(';
RIGHTPAREN: ')';
LEFTBRACKET: '[';
RIGHTBRACKET: ']';
LEFTBRACE: '{';
RIGHTBRACE: '}';
PLUS: '+';
MINUS: '-';
STAR: '*';
DIV: '/';
COMMA: ',';
COLON: ':';
GREATEREQUAL: '>=';
LESSEQUAL: '<=';
EQUAL: '=';
DIFFERENT: '<>';
WS : [ \t\r]+ -> skip;

