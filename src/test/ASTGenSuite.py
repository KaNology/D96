import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_class_declaration(self):
        input = """
        Class Shape {
            $sum(){
                Val a: Int = 1;
            }
        }
        """
        expect = str(
            Program(
                [ClassDecl(Id("Shape"), [])]
            )
        )
        self.assertTrue(TestAST.test(input,expect,300))
   