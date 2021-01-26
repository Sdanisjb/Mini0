from antlr4 import *
from GramaticaLexer import GramaticaLexer
from GramaticaParser import GramaticaParser
from GramaticaListener import GramaticaListener
import sys

def getTypeName(lex, tokenType):
    return str(lex.ruleNames[tokenType - 1])




if __name__ == "__main__":
    lexer = GramaticaLexer(FileStream("miniProgram.txt"))
    t =lexer.nextToken()
    while ( t.type != Token.EOF):
        print("<" + getTypeName(lexer, t.type) + "," + str(t.text) + ">")
        t =lexer.nextToken()


