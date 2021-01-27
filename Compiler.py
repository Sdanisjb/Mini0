from antlr4 import *
from GramaticaLexer import GramaticaLexer
from GramaticaParser import GramaticaParser
from GramaticaListener import GramaticaListener

import sys
import unittest
from io import StringIO


def getTypeName(lex, tokenType):
    return str(lex.ruleNames[tokenType - 1])


class GrammarTestCase(unittest.TestCase):
    def setUp(self):
        self.lexer = GramaticaLexer(FileStream("Pruebas/miniProgram.txt"))
        self.tokens = CommonTokenStream(self.lexer)
        self.parser = GramaticaParser(self.tokens)

    def test1Token1(self):
        print("-------Prueba de Tokenizador para el programa miniProgram.txt--------")
        t = self.lexer.nextToken()
        while(t.type!= Token.EOF):
             print("<" + getTypeName(self.lexer, t.type) + "," + (t.text if t.text != "\n" else "salto de linea") + ">", end="\t")
             t =self.lexer.nextToken()

        print("\n\n\n\n --------------Fin del Caso de Prueba ------------------------")    
        self.assertEqual(0,0)

    def test2Program(self):
        print("---------Prueba de la regla Programa de la Gramática----------------")
        self.lexer = GramaticaLexer(FileStream("Pruebas/miniProgram.txt"))
        self.tokens = CommonTokenStream(self.lexer)
        self.parser = GramaticaParser(self.tokens)
        
        self.parser.programa()
        print("\n\n\n\n --------------Fin del Caso de Prueba ------------------------")  
        self.assertEqual(0,0) 
    
    def test3ListaDecl(self):
        print("---------Prueba de la regla listaDecl de la Gramática----------------")
        self.lexer = GramaticaLexer(FileStream("Pruebas/test3.txt"))
        self.tokens = CommonTokenStream(self.lexer)
        self.parser = GramaticaParser(self.tokens)
        self.parser.listadecl()
        print("\n\n\n\n --------------Fin del Caso de Prueba ------------------------")
        self.assertEqual(0,0)

    def test4Decl(self):
        print("---------Prueba de la regla decl de la Gramática----------------")
        self.lexer = GramaticaLexer(FileStream("Pruebas/test4.txt"))
        self.tokens = CommonTokenStream(self.lexer)
        self.parser = GramaticaParser(self.tokens)
        self.parser.decl()
        print("\n\n\n\n --------------Fin del Caso de Prueba ------------------------")
        self.assertEqual(0,0)

    def test5global(self):
        print("---------Prueba de la regla global de la Gramática----------------")
        self.lexer = GramaticaLexer(FileStream("Pruebas/test5.txt"))
        self.tokens = CommonTokenStream(self.lexer)
        self.parser = GramaticaParser(self.tokens)
        self.parser.glbal()
        print("\n\n\n\n --------------Fin del Caso de Prueba ------------------------")
        self.assertEqual(0,0)
    
    def test6funcion(self):
        print("---------Prueba de la regla funcion de la Gramática----------------")
        self.lexer = GramaticaLexer(FileStream("Pruebas/test6.txt"))
        self.tokens = CommonTokenStream(self.lexer)
        self.parser = GramaticaParser(self.tokens)
        self.parser.funcion()
        print("\n\n\n\n --------------Fin del Caso de Prueba ------------------------")
        self.assertEqual(0,0)

    def test7listabloque(self):
        print("---------Prueba de la regla bloque de la Gramática----------------")
        self.lexer = GramaticaLexer(FileStream("Pruebas/test7.txt"))
        self.tokens = CommonTokenStream(self.lexer)
        self.parser = GramaticaParser(self.tokens)
        self.parser.bloque()
        print("\n\n\n\n --------------Fin del Caso de Prueba ------------------------")
        self.assertEqual(0,0)

    def test8listaComando(self):
        print("---------Prueba de la regla listaComando de la Gramática----------------")
        self.lexer = GramaticaLexer(FileStream("Pruebas/test8.txt"))
        self.tokens = CommonTokenStream(self.lexer)
        self.parser = GramaticaParser(self.tokens)
        self.parser.listaComando()
        print("\n\n\n\n --------------Fin del Caso de Prueba ------------------------")
        self.assertEqual(0,0)

    def test9comando(self):
        print("---------Prueba de la regla comando de la Gramática----------------")
        self.lexer = GramaticaLexer(FileStream("Pruebas/test9.txt"))
        self.tokens = CommonTokenStream(self.lexer)
        self.parser = GramaticaParser(self.tokens)
        self.parser.comando()
        print("\n\n\n\n --------------Fin del Caso de Prueba ------------------------")
        self.assertEqual(0,0)

    def test10params(self):
        print("---------Prueba de la regla params de la Gramática----------------")
        self.lexer = GramaticaLexer(FileStream("Pruebas/test10.txt"))
        self.tokens = CommonTokenStream(self.lexer)
        self.parser = GramaticaParser(self.tokens)
        self.parser.params()
        print("\n\n\n\n --------------Fin del Caso de Prueba ------------------------")
        self.assertEqual(0,0)

    def test11Aparametro(self):
        print("---------Prueba de la regla parametro de la Gramática----------------")
        self.lexer = GramaticaLexer(FileStream("Pruebas/test11.txt"))
        self.tokens = CommonTokenStream(self.lexer)
        self.parser = GramaticaParser(self.tokens)
        self.parser.parametro()
        print("\n\n\n\n --------------Fin del Caso de Prueba ------------------------")
        self.assertEqual(0,0)

    def test12Avar(self):
        print("---------Prueba de la regla var de la Gramática----------------")
        self.lexer = GramaticaLexer(FileStream("Pruebas/test12.txt"))
        self.tokens = CommonTokenStream(self.lexer)
        self.parser = GramaticaParser(self.tokens)
        self.parser.var()
        print("\n\n\n\n --------------Fin del Caso de Prueba ------------------------")
        self.assertEqual(0,0)

    def test13AComandos(self):
        print("---------Prueba de la regla cmdif de la Gramática----------------")
        self.lexer = GramaticaLexer(FileStream("Pruebas/test131.txt"))
        self.tokens = CommonTokenStream(self.lexer)
        self.parser = GramaticaParser(self.tokens)
        self.parser.cmdif()
        print("---------Prueba de la regla cmdif (ifelse) de la Gramática----------------")
        self.lexer = GramaticaLexer(FileStream("Pruebas/test132.txt"))
        self.tokens = CommonTokenStream(self.lexer)
        self.parser = GramaticaParser(self.tokens)
        self.parser.cmdif()
        print("---------Prueba de la regla cmdif (else) de la Gramática----------------")
        self.lexer = GramaticaLexer(FileStream("Pruebas/test133.txt"))
        self.tokens = CommonTokenStream(self.lexer)
        self.parser = GramaticaParser(self.tokens)
        self.parser.cmdif()
        print("---------Prueba de la regla cmdassign de la Gramática----------------")
        self.lexer = GramaticaLexer(FileStream("Pruebas/test134.txt"))
        self.tokens = CommonTokenStream(self.lexer)
        self.parser = GramaticaParser(self.tokens)
        self.parser.cmdasign
        print("---------Prueba de la regla cmdwhile de la Gramática----------------")
        self.lexer = GramaticaLexer(FileStream("Pruebas/test135.txt"))
        self.tokens = CommonTokenStream(self.lexer)
        self.parser = GramaticaParser(self.tokens)
        self.parser.cmdwhile()
        print("---------Prueba de la regla return de la Gramática----------------")
        self.lexer = GramaticaLexer(FileStream("Pruebas/test136.txt"))
        self.tokens = CommonTokenStream(self.lexer)
        self.parser = GramaticaParser(self.tokens)
        self.parser.cmdreturn()
        print("---------Prueba de la regla llamada de la Gramática----------------")
        self.lexer = GramaticaLexer(FileStream("Pruebas/test137.txt"))
        self.tokens = CommonTokenStream(self.lexer)
        self.parser = GramaticaParser(self.tokens)
        self.parser.llamada()
        print("\n\n\n\n --------------Fin del Caso de Prueba ------------------------")
        self.assertEqual(0,0)

    def test14AlistaExp(self):
        print("---------Prueba de la regla listaExpr de la Gramática----------------")
        self.lexer = GramaticaLexer(FileStream("Pruebas/test14.txt"))
        self.tokens = CommonTokenStream(self.lexer)
        self.parser = GramaticaParser(self.tokens)
        self.parser.listaexp()
        print("\n\n\n\n --------------Fin del Caso de Prueba ------------------------")
        self.assertEqual(0,0)
    
    def test14error(self):
        print("---------Prueba de Errores de la Gramática----------------")
        self.lexer = GramaticaLexer(FileStream("Pruebas/error.txt"))
        self.tokens = CommonTokenStream(self.lexer)
        self.parser = GramaticaParser(self.tokens)
        self.parser.programa()
        print("\n\n\n\n --------------Fin del Caso de Prueba ------------------------")
        self.assertEqual(0,0)
        
        
        
        

if __name__ == "__main__":
    unittest.main()
   # lexer = GramaticaLexer(FileStream("miniProgram.txt"))
   # t =lexer.nextToken()
   # while ( t.type != Token.EOF):
   #     print("<" + getTypeName(lexer, t.type) + "," + str(t.text) + ">")
   #     t =lexer.nextToken()
   # tokens = CommonTokenStream(lexer)
   # parser = GramaticaParser(tokens)
   # parser.programa()

