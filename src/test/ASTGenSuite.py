import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_class_declaration(self):
        input = """
        Class Shape {

        }
        """
        expect = str(
            Program(
                [ClassDecl(Id("Shape"), [], None)]
            )
        )
        self.assertTrue(TestAST.test(input,expect,300))

    def test_class_with_parent(self):
        input = """
        Class Shape : Line {

        }
        """
        expect = str(
            Program(
                [ClassDecl(Id("Shape"), [], Id("Line"))]
            )
        )
        self.assertTrue(TestAST.test(input,expect,301))

    def test_multiple_class_declaration(self):
        input = """
        Class Dot {

        }

        Class Line : Dot {

        }

        Class Shape : Line {

        }
        """
        expect = str(
            Program(
                [
                    ClassDecl(Id("Dot"),[]),
                    ClassDecl(Id("Line"),[],Id("Dot")),
                    ClassDecl(Id("Shape"),[],Id("Line"))
                ]
            )
        )
        self.assertTrue(TestAST.test(input,expect,302))

    def test_attribute_declaration(self):
        input = """
        Class Dog : Animal {
            Val name, $color, $nickname : String = "Mimi", "Brown", "Davis"; 
            Var $age, leg : Int = 5, 4;
            Val height : Float = 12.5;
            Var isGerman : Boolean = True;
            Var friend, $parent : Dog;
        }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Dog"),
                        [
                            AttributeDecl(Instance(),ConstDecl(Id("name"),StringType(),StringLiteral("Mimi"))),
                            AttributeDecl(Static(),ConstDecl(Id("$color"),StringType(),StringLiteral("Brown"))),
                            AttributeDecl(Static(),ConstDecl(Id("$nickname"),StringType(),StringLiteral("Davis"))),
                            AttributeDecl(Static(),VarDecl(Id("$age"),IntType(),IntLiteral(5))),
                            AttributeDecl(Instance(),VarDecl(Id("leg"),IntType(),IntLiteral(4))),
                            AttributeDecl(Instance(),ConstDecl(Id("height"),FloatType(),FloatLiteral(12.5))),
                            AttributeDecl(Instance(),VarDecl(Id("isGerman"),BoolType(),BooleanLiteral(True))),
                            AttributeDecl(Instance(),VarDecl(Id("friend"),ClassType(Id("Dog")),NullLiteral())),
                            AttributeDecl(Static(),VarDecl(Id("$parent"),ClassType(Id("Dog")),NullLiteral()))
                        ],
                        Id("Animal")
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input,expect,303))

    def test_array_attribute(self):
        input = """
        Class Square {
            Val dots : Array[Float, 4];
            Var $dots : Array[Float, 4] = Array(1.2, 3.4, 5.6, 7.8);
        }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Square"),
                        [
                            AttributeDecl(Instance(),ConstDecl(Id("dots"),ArrayType(4,FloatType()),None)),
                            AttributeDecl(Static(),VarDecl(Id("$dots"),ArrayType(4,FloatType()),ArrayLiteral([FloatLiteral(1.2),FloatLiteral(3.4),FloatLiteral(5.6),FloatLiteral(7.8)])))
                        ],
                        None
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input,expect,304))

    def test_nested_array(self):
        input = """
        Class Square {
            Var $dots : Array[Array[Float, 2], 2] = Array(Array(1.2, 3.4), Array(5.6, 7.8));
        }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Square"),
                        [
                            AttributeDecl(
                                Static(),
                                VarDecl(
                                    Id("$dots"),
                                    ArrayType(2,ArrayType(2,FloatType())),
                                    ArrayLiteral(
                                        [
                                            ArrayLiteral([FloatLiteral(1.2),FloatLiteral(3.4)]),
                                            ArrayLiteral([FloatLiteral(5.6),FloatLiteral(7.8)])
                                        ])
                                )
                            )
                        ],
                        None
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input,expect,305))

    def test_method_declaration(self):
        input = """
        Class Shape {
            Val $numOfShape: Int = 0;

            $getNumOfShape() {

            }
        }
        """
        expect = str(
            Program(
                [ClassDecl(Id("Shape"), [
                    AttributeDecl(Static(),ConstDecl(Id("$numOfShape"),IntType(),IntLiteral(0))),
                    MethodDecl(Static(),Id("$getNumOfShape"),[],Block([]))
                ], None)]
            )
        )
        self.assertTrue(TestAST.test(input,expect,306))

    def test_method_with_params(self):
        input = """
        Class Shape {
            $getNumOfShape(size : Float; dotNum, lineNum : Int; type : Shape) {

            }
        }
        """
        expect = str(
            Program(
                [ClassDecl(Id("Shape"), [
                    MethodDecl(
                        Static(),
                        Id("$getNumOfShape"),
                        [
                            VarDecl(Id("size"),FloatType()),
                            VarDecl(Id("dotNum"),IntType()),
                            VarDecl(Id("lineNum"),IntType()),
                            VarDecl(Id("type"),ClassType(Id("Shape")))
                        ],Block([]))
                ], None)]
            )
        )
        self.assertTrue(TestAST.test(input,expect,307))

    def test_many_method(self):
        input = """
        Class Shape {
            $getNumOfShape(size : Float; dotNum, lineNum : Int; type : Shape) {

            }

            getArea() {

            }
        }
        """
        expect = str(
            Program([ClassDecl(Id("Shape"),[
                MethodDecl(Static(),Id("$getNumOfShape"),[VarDecl(Id("size"),FloatType()),VarDecl(Id("dotNum"),IntType()),VarDecl(Id("lineNum"),IntType()),VarDecl(Id("type"),ClassType(Id("Shape")))],Block([])),
                MethodDecl(Instance(),Id("getArea"),[],Block([]))])])
        )
        self.assertTrue(TestAST.test(input,expect,308))

    def test_mixed_declaration(self):
        input = """
        Class Shape {
            $getNumOfShape() {

            }

            Val dots : Array[Float, 4];

            getArea() {

            }

            Var $dots : Array[Float, 4] = Array(1.2, 3.4, 5.6, 7.8);
        }
        """
        expect = str(
            Program([ClassDecl(Id("Shape"),
            [
                MethodDecl(Static(),Id("$getNumOfShape"),[],Block([])),
                AttributeDecl(Instance(),ConstDecl(Id("dots"),ArrayType(4,FloatType()),None)),
                MethodDecl(Instance(),Id("getArea"),[],Block([])),
                AttributeDecl(Static(),VarDecl(Id("$dots"),ArrayType(4,FloatType()),ArrayLiteral([FloatLiteral(1.2),FloatLiteral(3.4),FloatLiteral(5.6),FloatLiteral(7.8)])))
            ])])
        )
        self.assertTrue(TestAST.test(input,expect,309))

    def test_declaration_statement(self):
        input = """
        Class Shape {
            getArea() {
                Val dotNum : Int;
                Var line : Array[Float, 4] = Array(1.2, 3.4, 5.6, 7.8);
                Val name, color, nickname : String = "Mimi", "Brown", "Davis"; 
                Var age, leg : Int = 5, 4;
                Val height : Float = 12.5;
                Var isGerman : Boolean = True;
                Var friend, parent : Dog;
            }
        }
        """
        expect = str(
            Program([
                ClassDecl(
                    Id("Shape"),[
                        MethodDecl(
                            Instance(),
                            Id("getArea"),
                            [],
                            Block([
                                ConstDecl(Id("dotNum"),IntType(),None),
                                VarDecl(Id("line"),ArrayType(4,FloatType()),ArrayLiteral([FloatLiteral(1.2),FloatLiteral(3.4),FloatLiteral(5.6),FloatLiteral(7.8)])),
                                ConstDecl(Id("name"),StringType(),StringLiteral("Mimi")),
                                ConstDecl(Id("color"),StringType(),StringLiteral("Brown")),
                                ConstDecl(Id("nickname"),StringType(),StringLiteral("Davis")),
                                VarDecl(Id("age"),IntType(),IntLiteral(5)),
                                VarDecl(Id("leg"),IntType(),IntLiteral(4)),
                                ConstDecl(Id("height"),FloatType(),FloatLiteral(12.5)),
                                VarDecl(Id("isGerman"),BoolType(),BooleanLiteral(True)),
                                VarDecl(Id("friend"),ClassType(Id("Dog")),NullLiteral()),
                                VarDecl(Id("parent"),ClassType(Id("Dog")),NullLiteral())]))])])
        )
        self.assertTrue(TestAST.test(input,expect,310))

    def test_assign_statement(self):
        input = """
        Class Person {
            update_info() {
                age = 45;
                Self.height = 175;
                Person::$name = "Andy";
                Self.isMarried = True;
                limb[0][1] = Leg;
            }
        }
        """
        expect = str(
            Program([ClassDecl(Id("Person"),[MethodDecl(Instance(),Id("update_info"),[],Block([
                Assign(Id("age"),IntLiteral(45)),
                Assign(FieldAccess(SelfLiteral(),Id("height")),IntLiteral(175)),
                Assign(FieldAccess(Id("Person"),Id("$name")),StringLiteral("Andy")),
                Assign(FieldAccess(SelfLiteral(),Id("isMarried")),BooleanLiteral(True)),
                Assign(ArrayCell(Id("limb"),[IntLiteral(0),IntLiteral(1)]),Id("Leg"))
                ]))])])
        )
        self.assertTrue(TestAST.test(input,expect,311))

    def test_if_statement(self):
        input = """
        Class Person {
            isMarried() {
                If(a){
                    age = 1;
                }
            }
        }
        """
        expect = str(
            Program([ClassDecl(Id("Person"),[MethodDecl(Instance(),Id("isMarried"),[],Block([If(Id("a"),Block([Assign(Id("age"),IntLiteral(1))]))]))])])
        )
        self.assertTrue(TestAST.test(input,expect,312))

    def test_elseif_declaration(self):
        input = """
        Class Person {
            isMarried() {
                If(a){
                    age = 1;
                }
                Elseif(b){
                    age = 2;
                }
            }
        }
        """
        expect = str(
            Program([ClassDecl(Id("Person"),[MethodDecl(Instance(),Id("isMarried"),[],Block([If(Id("a"),Block([Assign(Id("age"),IntLiteral(1))]),If(Id("b"),Block([Assign(Id("age"),IntLiteral(2))])))]))])])
        )
        self.assertTrue(TestAST.test(input,expect,313))

    def test_else_declaration(self):
        input = """
        Class Shape {
            isMarried() {
                If(a){
                    age = 1;
                }
                Elseif(b){
                    age = 2;
                }
                Else{
                    age = 3;
                }
            }
        }
        """
        expect = str(
            Program([ClassDecl(Id("Shape"),[MethodDecl(Instance(),Id("isMarried"),[],Block([If(Id("a"),Block([Assign(Id("age"),IntLiteral(1))]),If(Id("b"),Block([Assign(Id("age"),IntLiteral(2))]),Block([Assign(Id("age"),IntLiteral(3))])))]))])])
        )
        self.assertTrue(TestAST.test(input,expect,314))

    def test_for_statement(self):
        input = """
        Class Shape {
            loop(){
                Foreach (i In 1 .. 100) {
                    age = 1;
                }
            }
        }
        """
        expect = str(
            Program([ClassDecl(Id("Shape"),[MethodDecl(Instance(),Id("loop"),[],Block([
                For(
                    Id("i"),
                    IntLiteral(1),
                    IntLiteral(100),
                    Block([Assign(Id("age"),IntLiteral(1))]),
                    IntLiteral(1))
                ]))])])
        )
        self.assertTrue(TestAST.test(input,expect,315))

    def test_for_Statement_again(self):
        input = """
        Class Shape {
            loop(){
                Foreach (i In 1 .. 100 By 2) {
                    age = 1;
                }
            }
        }
        """
        expect = str(
            Program([ClassDecl(Id("Shape"),[MethodDecl(Instance(),Id("loop"),[],Block([
                For(
                    Id("i"),
                    IntLiteral(1),
                    IntLiteral(100),
                    Block([Assign(Id("age"),IntLiteral(1))]),
                    IntLiteral(2))
                ]))])])
        )
        self.assertTrue(TestAST.test(input,expect,316))

    def test_break_statement(self):
        input = """
        Class Shape {
            loop(){
                Foreach (i In 1 .. 100 By 2) {
                    Break;
                }
            }
        }
        """
        expect = str(
            Program([ClassDecl(Id("Shape"),[MethodDecl(Instance(),Id("loop"),[],Block([For(Id("i"),IntLiteral(1),IntLiteral(100),Block([Break()]),IntLiteral(2))]))])])
        )
        self.assertTrue(TestAST.test(input,expect,317))

    def test_continue_statement(self):
        input = """
        Class Shape {
            loop(){
                Foreach (i In 1 .. 100 By 2) {
                    Continue;
                }
            }
        }
        """
        expect = str(
            Program([ClassDecl(Id("Shape"),[MethodDecl(Instance(),Id("loop"),[],Block([For(Id("i"),IntLiteral(1),IntLiteral(100),Block([Continue()]),IntLiteral(2))]))])])
        )
        self.assertTrue(TestAST.test(input,expect,318))

    def test_return_statement(self):
        input = """
        Class Shape {
            getArea(){
                Return;
            }
        }
        """
        expect = str(
            Program([ClassDecl(Id("Shape"),[MethodDecl(Instance(),Id("getArea"),[],Block([Return()]))])])
        )
        self.assertTrue(TestAST.test(input,expect,319))

    def test_return_statement_again(self):
        input = """
        Class Shape {
            getArea(){
                Return area;
            }
        }
        """
        expect = str(
            Program([ClassDecl(Id("Shape"),[MethodDecl(Instance(),Id("getArea"),[],Block([Return(Id("area"))]))])])
        )
        self.assertTrue(TestAST.test(input,expect,320))

    def test_call_statement(self):
        input = """
        Class Shape {
            getArea(area: Float){
                Return area;
            }

            $getArea(area: Float){
                Return area;
            }

            getName(){
                Return Self.name;
            }

            $getName(){
                Return Self.name;
            }

            displayInfo(){
                Self.getArea(5.2);
                Self.getName();
                Shape::$getArea(6.2);
                Shape::$getName();
            }
        }
        """
        expect = str(
            Program([ClassDecl(Id("Shape"),[MethodDecl(Instance(),Id("getArea"),[VarDecl(Id("area"),FloatType())],Block([Return(Id("area"))])),MethodDecl(Static(),Id("$getArea"),[VarDecl(Id("area"),FloatType())],Block([Return(Id("area"))])),MethodDecl(Instance(),Id("getName"),[],Block([Return(FieldAccess(SelfLiteral(),Id("name")))])),MethodDecl(Static(),Id("$getName"),[],Block([Return(FieldAccess(SelfLiteral(),Id("name")))])),MethodDecl(Instance(),Id("displayInfo"),[],Block([CallStmt(SelfLiteral(),Id("getArea"),[FloatLiteral(5.2)]),CallStmt(SelfLiteral(),Id("getName"),[]),CallStmt(Id("Shape"),Id("$getArea"),[FloatLiteral(6.2)]),CallStmt(Id("Shape"),Id("$getName"),[])]))])])
        )
        self.assertTrue(TestAST.test(input,expect,321))

    def test_block_statement(self):
        input = """
        Class Shape {
            loop(){
                Val numOfShape: Int = 0;
                {
                    {
                        Var Area: Float;
                    }
                    {

                    }
                }
            }
        }
        """
        expect = str(
            Program([ClassDecl(Id("Shape"),[MethodDecl(Instance(),Id("loop"),[],Block([ConstDecl(Id("numOfShape"),IntType(),IntLiteral(0)),Block([Block([VarDecl(Id("Area"),FloatType())]),Block([])])]))])])
        )
        self.assertTrue(TestAST.test(input,expect,322))
    def test_expressions1(self):
        input = """
        Class A {
            Var a : Int = 1 + 1 * 2;
        }
        """
        expect = str(
            Program([ClassDecl(Id("A"),[AttributeDecl(Instance(),VarDecl(Id("a"),IntType(),BinaryOp("+",IntLiteral(1),BinaryOp("*",IntLiteral(1),IntLiteral(2)))))])])
        )
        self.assertTrue(TestAST.test(input,expect,323))
    def test_expressions2(self):
        input = """
        Class A {
            Var a : Float = (1 + 2) * 3 / 4;
            Var a : Float = ((1 + 2) * 3) / 4;
            Var a : Float = (1 + 2) * (3 / 4);
            Var a : Float = 1 + (2 * 3) / 4;
        }
        """
        expect = str(
            Program([ClassDecl(Id("A"),[
                AttributeDecl(Instance(),VarDecl(Id("a"),FloatType(),BinaryOp("/",BinaryOp("*",BinaryOp("+",IntLiteral(1),IntLiteral(2)),IntLiteral(3)),IntLiteral(4)))),
                AttributeDecl(Instance(),VarDecl(Id("a"),FloatType(),BinaryOp("/",BinaryOp("*",BinaryOp("+",IntLiteral(1),IntLiteral(2)),IntLiteral(3)),IntLiteral(4)))),
                AttributeDecl(Instance(),VarDecl(Id("a"),FloatType(),BinaryOp("*",BinaryOp("+",IntLiteral(1),IntLiteral(2)),BinaryOp("/",IntLiteral(3),IntLiteral(4))))),
                AttributeDecl(Instance(),VarDecl(Id("a"),FloatType(),BinaryOp("+",IntLiteral(1),BinaryOp("/",BinaryOp("*",IntLiteral(2),IntLiteral(3)),IntLiteral(4)))))
                ])])
        )
        self.assertTrue(TestAST.test(input,expect,324))
    def test_expressions3(self):
        """Simple program: int main() {} """
        input = """
        Class A {
            Var a : Int = !!a - --2 * ---3;
        }
        """
        expect = str(
            Program([ClassDecl(Id("A"),[AttributeDecl(Instance(),VarDecl(Id("a"),IntType(),BinaryOp("-",UnaryOp("!",UnaryOp("!",Id("a"))),BinaryOp("*",UnaryOp("-",UnaryOp("-",IntLiteral(2))),UnaryOp("-",UnaryOp("-",UnaryOp("-",IntLiteral(3))))))))])])
        )
        self.assertTrue(TestAST.test(input,expect,325))
    def test_arraycell(self):
        input = """
        Class A {
            Val a : String = b[1][21][0x54][0b101][045];
        }
        """
        expect = str(
            Program([ClassDecl(Id("A"),[AttributeDecl(Instance(),ConstDecl(Id("a"),StringType(),ArrayCell(Id("b"),[IntLiteral(1),IntLiteral(21),IntLiteral(84),IntLiteral(5),IntLiteral(37)])))])])
        )
        self.assertTrue(TestAST.test(input,expect,326))
    def test_class_init(self):
        """Simple program: int main() {} """
        input = """
        Class A {
            Var a : Dog = New Dog();
            Var b : Cat;
            Var c : Owner = New Person("Davis", 22, Null);
        }
        """
        expect = str(
            Program([ClassDecl(Id("A"),[
                AttributeDecl(Instance(),VarDecl(Id("a"),ClassType(Id("Dog")),NewExpr(Id("Dog"),[]))),
                AttributeDecl(Instance(),VarDecl(Id("b"),ClassType(Id("Cat")),NullLiteral())),
                AttributeDecl(Instance(),VarDecl(Id("c"),ClassType(Id("Owner")),NewExpr(Id("Person"),[StringLiteral("Davis"),IntLiteral(22),NullLiteral()])))])])
        )
        self.assertTrue(TestAST.test(input,expect,327))
    def test_arraycell_lhs(self):
        input = """
        Class A {
            $foo(){
                a[1][3+4] = 1;
                a[1][b[3]] = "abc";
            }
        }
        """
        expect = str(
            Program([ClassDecl(Id("A"),[MethodDecl(Static(),Id("$foo"),[],Block([
                Assign(
                    ArrayCell(Id("a"),[IntLiteral(1),BinaryOp("+",IntLiteral(3),IntLiteral(4))]),
                    IntLiteral(1)),
                Assign(
                    ArrayCell(Id("a"),[IntLiteral(1),ArrayCell(Id("b"),[IntLiteral(3)])]),
                    StringLiteral("abc"))]))])])
        )
        self.assertTrue(TestAST.test(input, expect, 328))
    def test_field_access(self):
        input = """
        Class A {
            foo(){
                Person.name.first = "Davis";
            }
        }
        """
        expect = str(
            Program([ClassDecl(Id("A"),[MethodDecl(Instance(),Id("foo"),[],Block([Assign(FieldAccess(FieldAccess(Id("Person"),Id("name")),Id("first")),StringLiteral("Davis"))]))])])
        )
        self.assertTrue(TestAST.test(input, expect, 329))
    def test_field_access_function_call(self):
        input = """
        Class A {
            foo(){
                Var person : Person = Person.pet.getName(4, Dog) + Person.house.getAddress();
            }
        }
        """
        expect = str(
            Program([ClassDecl(Id("A"),[MethodDecl(Instance(),Id("foo"),[],Block([VarDecl(Id("person"),ClassType(Id("Person")),BinaryOp("+",CallExpr(FieldAccess(Id("Person"),Id("pet")),Id("getName"),[IntLiteral(4),Id("Dog")]),CallExpr(FieldAccess(Id("Person"),Id("house")),Id("getAddress"),[])))]))])])
        )
        self.assertTrue(TestAST.test(input, expect, 330))
    def test_object_call_init(self):
        input = """
        Class A:B{
            foo(){
                person = New Person("Anthony" +. "Davis" + 153).pet.getName();
            }
        }
        """
        expect = str(
            Program([ClassDecl(Id("A"),[MethodDecl(Instance(),Id("foo"),[],Block([Assign(Id("person"),CallExpr(FieldAccess(NewExpr(Id("Person"),[BinaryOp("+.",StringLiteral("Anthony"),BinaryOp("+",StringLiteral("Davis"),IntLiteral(153)))]),Id("pet")),Id("getName"),[]))]))],Id("B"))])
        )
        self.assertTrue(TestAST.test(input, expect, 331))
    def test_mixed_method(self):
        input = """
        Class A:B{
            foo(){
                Return Self.foo();
            }
            Constructor (a,b:J){

            }
            Destructor (){

            }
        }
        """
        expect = str(
            Program([ClassDecl(Id("A"),[MethodDecl(Instance(),Id("foo"),[],Block([Return(CallExpr(SelfLiteral(),Id("foo"),[]))])),MethodDecl(Instance(),Id("Constructor"),[VarDecl(Id("a"),ClassType(Id("J"))),VarDecl(Id("b"),ClassType(Id("J")))],Block([])),MethodDecl(Instance(),Id("Destructor"),[],Block([]))],Id("B"))])
        )
        self.assertTrue(TestAST.test(input, expect, 332))
    def test_array_init(self):
        input = """
        Class A:B{
            Var $a:Array[Array[Int,1],3] = Array(Array(1),Array(1),Array(1));
        }
        """
        expect = str(
            Program([ClassDecl(Id("A"),[AttributeDecl(Static(),VarDecl(Id("$a"),ArrayType(3,ArrayType(1,IntType())),ArrayLiteral([ArrayLiteral([IntLiteral(1)]),ArrayLiteral([IntLiteral(1)]),ArrayLiteral([IntLiteral(1)])])))],Id("B"))])
        )
        self.assertTrue(TestAST.test(input, expect, 333))
    def test_for_each(self):
        line = """
                Class Shape{
                    foo(){
                        Foreach (x In 1+1 .. 100+100 By a.foo(1+2*3,"abc"+.1+2)){}
                    }
                }
            """
        expect = str(
            Program([ClassDecl(Id("Shape"),[MethodDecl(Instance(),Id("foo"),[],Block([For(Id("x"),BinaryOp("+",IntLiteral(1),IntLiteral(1)),BinaryOp("+",IntLiteral(100),IntLiteral(100)),Block([]),CallExpr(Id("a"),Id("foo"),[BinaryOp("+",IntLiteral(1),BinaryOp("*",IntLiteral(2),IntLiteral(3))),BinaryOp("+.",StringLiteral("abc"),BinaryOp("+",IntLiteral(1),IntLiteral(2)))]))]))])])
        )
        self.assertTrue(TestAST.test(line, expect, 334))
    def test_for_each2(self):
        line = """
                Class Shape{
                    foo(){
                        Foreach (x In a::$b() .. a.c.c.c By a::$foo){
                            Foreach (x In a::$b() .. a.c.c.c By a::$foo){}
                        }
                    }
                }
                """
        expect = str(
            Program([ClassDecl(Id("Shape"),[MethodDecl(Instance(),Id("foo"),[],Block([For(Id("x"),CallExpr(Id("a"),Id("$b"),[]),FieldAccess(FieldAccess(FieldAccess(Id("a"),Id("c")),Id("c")),Id("c")),Block([For(Id("x"),CallExpr(Id("a"),Id("$b"),[]),FieldAccess(FieldAccess(FieldAccess(Id("a"),Id("c")),Id("c")),Id("c")),Block([]),FieldAccess(Id("a"),Id("$foo")))]),FieldAccess(Id("a"),Id("$foo")))]))])])
        )
        self.assertTrue(TestAST.test(line, expect, 335))
    def test_if_and_for(self):
        line = """
                Class Shape{
                    foo(){
                        If ( a == -1--1){
                            Foreach(x In 1 .. 100 By 2){
                                If ( a == -1--1){
                                    Foreach(x In 1 .. 100 By 2){

                                    }
                                }
                            }
                        }
                    }
                }
                """

        expect = str(
            Program([ClassDecl(Id("Shape"),[MethodDecl(Instance(),Id("foo"),[],Block([If(BinaryOp("==",Id("a"),BinaryOp("-",UnaryOp("-",IntLiteral(1)),UnaryOp("-",IntLiteral(1)))),Block([For(Id("x"),IntLiteral(1),IntLiteral(100),Block([If(BinaryOp("==",Id("a"),BinaryOp("-",UnaryOp("-",IntLiteral(1)),UnaryOp("-",IntLiteral(1)))),Block([For(Id("x"),IntLiteral(1),IntLiteral(100),Block([]),IntLiteral(2))]))]),IntLiteral(2))]))]))])])
        )
        self.assertTrue(TestAST.test(line, expect, 336))
    def test_main_method(self):
        line = """
        Class Program{
            main(a,b,c:Int){}
            main(){}
        }
        Class AnotherProgram{
            main(){}
        }
        """

        expect = str(
            Program([ClassDecl(Id("Program"),[MethodDecl(Instance(),Id("main"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),VarDecl(Id("c"),IntType())],Block([])),MethodDecl(Static(),Id("main"),[],Block([]))]),ClassDecl(Id("AnotherProgram"),[MethodDecl(Instance(),Id("main"),[],Block([]))])])
        )
        self.assertTrue(TestAST.test(line, expect, 337))
    def test_integer(self):
        input = """
        Class Program {
            Val b : Int = ClassABC::$a.a.c.b[1][2][3][(0 + 012 + 0xA2 + 0XA2 +0b101+0B101)];
            Var c : Int = 0x0 + 0X0 + 0b0 + 0B0 + 00 + 0;
        }"""
        expect = str(
            Program([ClassDecl(Id("Program"),[AttributeDecl(Instance(),ConstDecl(Id("b"),IntType(),ArrayCell(FieldAccess(FieldAccess(FieldAccess(FieldAccess(Id("ClassABC"),Id("$a")),Id("a")),Id("c")),Id("b")),[IntLiteral(1),IntLiteral(2),IntLiteral(3),BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",IntLiteral(0),IntLiteral(10)),IntLiteral(162)),IntLiteral(162)),IntLiteral(5)),IntLiteral(5))]))),AttributeDecl(Instance(),VarDecl(Id("c"),IntType(),BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",IntLiteral(0),IntLiteral(0)),IntLiteral(0)),IntLiteral(0)),IntLiteral(0)),IntLiteral(0))))])])
        )
        self.assertTrue(TestAST.test(input, expect, 338))
    def test_function_calls(self):
        input = """
        Class Program {
            main() {
                (a[1]).func();
                a[1] = 1;
                Out.println(a.a[1]);
                ((((a[1][2]).a[1]).func()[0]).a[1]).func();
                Return;
            }
        }"""
        expect = str(
            Program([ClassDecl(Id("Program"),[MethodDecl(Static(),Id("main"),[],Block([
                CallStmt(ArrayCell(Id("a"),[IntLiteral(1)]),Id("func"),[]),
                Assign(ArrayCell(Id("a"),[IntLiteral(1)]),IntLiteral(1)),
                CallStmt(Id("Out"),Id("println"),[ArrayCell(FieldAccess(Id("a"),Id("a")),[IntLiteral(1)])]),
                CallStmt(ArrayCell(FieldAccess(ArrayCell(CallExpr(ArrayCell(FieldAccess(ArrayCell(Id("a"),[IntLiteral(1),IntLiteral(2)]),Id("a")),[IntLiteral(1)]),Id("func"),[]),[IntLiteral(0)]),Id("a")),[IntLiteral(1)]),Id("func"),[]),
                Return()]))])])
        )
        self.assertTrue(TestAST.test(input, expect, 339))
    def test_complex_array_cell(self):
        input = """
        Class Program {
            main() {
                a[1][exp::$b().c[exp::$b().c[exp::$b().c]]] = 1;
            }
        }"""
        expect = str(
            Program([ClassDecl(Id("Program"),[MethodDecl(Static(),Id("main"),[],Block([Assign(ArrayCell(Id("a"),[IntLiteral(1),ArrayCell(FieldAccess(CallExpr(Id("exp"),Id("$b"),[]),Id("c")),[ArrayCell(FieldAccess(CallExpr(Id("exp"),Id("$b"),[]),Id("c")),[FieldAccess(CallExpr(Id("exp"),Id("$b"),[]),Id("c"))])])]),IntLiteral(1))]))])])
        )
        self.assertTrue(TestAST.test(input, expect, 340))
    def test_complex_accesses(self):
        input = """
        Class Program {
            a() {
                A.a.a.foo();
                (a.a[1][2][3]).foo();
                MotorBike::$ab.foo();
                (MotorBike::$a.a[1][2]).foo();
            }
        }"""
        expect = str(
            Program([ClassDecl(Id("Program"),[MethodDecl(Instance(),Id("a"),[],Block([CallStmt(FieldAccess(FieldAccess(Id("A"),Id("a")),Id("a")),Id("foo"),[]),CallStmt(ArrayCell(FieldAccess(Id("a"),Id("a")),[IntLiteral(1),IntLiteral(2),IntLiteral(3)]),Id("foo"),[]),CallStmt(FieldAccess(Id("MotorBike"),Id("$ab")),Id("foo"),[]),CallStmt(ArrayCell(FieldAccess(FieldAccess(Id("MotorBike"),Id("$a")),Id("a")),[IntLiteral(1),IntLiteral(2)]),Id("foo"),[])]))])])
        )
        self.assertTrue(TestAST.test(input, expect, 341))
    def test_overall_data_type(self):
        input = """
        Class Dog {
            Val a : Int = 1;
            Val b : Float = 1.4;
            Val c : String = "abc";
            Val d : Boolean = True;
            Val e : Array[Int, 5] = Array(1, 5, 7, 12, 8);
            Val f : Animal = New Animal();
            Val g : Array[Array[Int, 5], 2] = Array(Array(1,2,3,4,5), Array(1,2,3,4,5));
        }
        """
        expect = str(
            Program([ClassDecl(Id("Dog"),[AttributeDecl(Instance(),ConstDecl(Id("a"),IntType(),IntLiteral(1))),AttributeDecl(Instance(),ConstDecl(Id("b"),FloatType(),FloatLiteral(1.4))),AttributeDecl(Instance(),ConstDecl(Id("c"),StringType(),StringLiteral("abc"))),AttributeDecl(Instance(),ConstDecl(Id("d"),BoolType(),BooleanLiteral(True))),AttributeDecl(Instance(),ConstDecl(Id("e"),ArrayType(5,IntType()),ArrayLiteral([IntLiteral(1),IntLiteral(5),IntLiteral(7),IntLiteral(12),IntLiteral(8)]))),AttributeDecl(Instance(),ConstDecl(Id("f"),ClassType(Id("Animal")),NewExpr(Id("Animal"),[]))),AttributeDecl(Instance(),ConstDecl(Id("g"),ArrayType(2,ArrayType(5,IntType())),ArrayLiteral([ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(5)]),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(5)])])))])])
        )
        self.assertTrue(TestAST.test(input, expect, 342))
    def test_integer_literal(self):
        input = """
        Class IntLit {
            Val a : Int = 1_234_567;
            Val b : Int = 1_2_3_4_5_6_7;
            Val c : Int = 0b110;
            Val d : Int = 0123456;
            Val e : Int = 0x123456789ABCDEF;
        }
        """
        expect = str(
            Program([ClassDecl(Id("IntLit"),[AttributeDecl(Instance(),ConstDecl(Id("a"),IntType(),IntLiteral(1234567))),AttributeDecl(Instance(),ConstDecl(Id("b"),IntType(),IntLiteral(1234567))),AttributeDecl(Instance(),ConstDecl(Id("c"),IntType(),IntLiteral(6))),AttributeDecl(Instance(),ConstDecl(Id("d"),IntType(),IntLiteral(42798))),AttributeDecl(Instance(),ConstDecl(Id("e"),IntType(),IntLiteral(81985529216486895)))])])
        )
        self.assertTrue(TestAST.test(input, expect, 343))
    def test_self_keyword(self):
        input = """
        Class ABC {
            Var w, h : Int;

            Constructor(w: Int; h: Int) {
                Self.w = w;
                Self.h = h;
                Return;
            }
        }
        """
        expect = str(
            Program([ClassDecl(Id("ABC"),[AttributeDecl(Instance(),VarDecl(Id("w"),IntType())),AttributeDecl(Instance(),VarDecl(Id("h"),IntType())),MethodDecl(Instance(),Id("Constructor"),[VarDecl(Id("w"),IntType()),VarDecl(Id("h"),IntType())],Block([Assign(FieldAccess(SelfLiteral(),Id("w")),Id("w")),Assign(FieldAccess(SelfLiteral(),Id("h")),Id("h")),Return()]))])])
        )
        self.assertTrue(TestAST.test(input, expect, 344))
    def test_calling_class_function(self):
        input = """
        Class Program {
            main(){
                Return New X().Y();
            }
        }
        """
        expect = str(
            Program([ClassDecl(Id("Program"),[MethodDecl(Static(),Id("main"),[],Block([Return(CallExpr(NewExpr(Id("X"),[]),Id("Y"),[]))]))])])
        )
        self.assertTrue(TestAST.test(input, expect, 345))
    def test_chain_object_creation(self):
        input = """
        Class Program {
            main(){
                Return New A(New B(New C()), 1+2, C::$x);
            }
        }
        """
        expect = str(
            Program([ClassDecl(Id("Program"),[MethodDecl(Static(),Id("main"),[],Block([Return(NewExpr(Id("A"),[NewExpr(Id("B"),[NewExpr(Id("C"),[])]),BinaryOp("+",IntLiteral(1),IntLiteral(2)),FieldAccess(Id("C"),Id("$x"))]))]))])])
        )
        self.assertTrue(TestAST.test(input, expect, 346))
    def test_more_arrays(self):
        input = """
        Class ArrayLit {
            Var a: Array[Int, 5] = Array(1,2,3,4,5);
            Var a1: Array[Int, 5];
            Var b: Array[Array[Int, 5], 2] = Array(Array(1,2,3,4,5), Array(6,7,8,9,10));
        }
        """
        expect = str(
            Program([ClassDecl(Id("ArrayLit"),[AttributeDecl(Instance(),VarDecl(Id("a"),ArrayType(5,IntType()),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(5)]))),AttributeDecl(Instance(),VarDecl(Id("a1"),ArrayType(5,IntType()))),AttributeDecl(Instance(),VarDecl(Id("b"),ArrayType(2,ArrayType(5,IntType())),ArrayLiteral([ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(5)]),ArrayLiteral([IntLiteral(6),IntLiteral(7),IntLiteral(8),IntLiteral(9),IntLiteral(10)])])))])])
        )
        self.assertTrue(TestAST.test(input, expect, 347))
    def test_array_with_exp(self):
        input = """
        Class ArrayLit {
            Var a: Array[Int, 3] = Array(1 + 2, 345, 6 * 8);
        }
        """
        expect = str(
            Program([ClassDecl(Id("ArrayLit"),[AttributeDecl(Instance(),VarDecl(Id("a"),ArrayType(3,IntType()),ArrayLiteral([BinaryOp("+",IntLiteral(1),IntLiteral(2)),IntLiteral(345),BinaryOp("*",IntLiteral(6),IntLiteral(8))])))])])
        )
        self.assertTrue(TestAST.test(input, expect, 348))
    def test_method_invocation(self):
        input = """
        Class Program {
            main(){
                a = Dog.bark() + Cat::$Meow() + Dog.name + Cat::$age + Animal.Dog[1] + Animal.type().name;
            }
        }
        """
        expect = str(
            Program([ClassDecl(Id("Program"),[MethodDecl(Static(),Id("main"),[],Block([Assign(Id("a"),BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",CallExpr(Id("Dog"),Id("bark"),[]),CallExpr(Id("Cat"),Id("$Meow"),[])),FieldAccess(Id("Dog"),Id("name"))),FieldAccess(Id("Cat"),Id("$age"))),ArrayCell(FieldAccess(Id("Animal"),Id("Dog")),[IntLiteral(1)])),FieldAccess(CallExpr(Id("Animal"),Id("type"),[]),Id("name"))))]))])])
        )
        self.assertTrue(TestAST.test(input, expect, 349))
    def test_multi_dim_array_decl(self):
        input = """
        Class Program {
            Var a: Array[Array[Array[Array[Int,2],2],2],2] = Array(Array(Array(Array(), Array()), Array(Array(), Array())),Array(Array(Array(), Array()), Array(Array(), Array())));
        }
        """
        expect = str(
            Program([ClassDecl(Id("Program"),[AttributeDecl(Instance(),VarDecl(Id("a"),ArrayType(2,ArrayType(2,ArrayType(2,ArrayType(2,IntType())))),ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([]),ArrayLiteral([])]),ArrayLiteral([ArrayLiteral([]),ArrayLiteral([])])]),ArrayLiteral([ArrayLiteral([ArrayLiteral([]),ArrayLiteral([])]),ArrayLiteral([ArrayLiteral([]),ArrayLiteral([])])])])))])])
        )
        self.assertTrue(TestAST.test(input, expect, 350))
    def test_normal_for_statement(self):
        input = """
        Class Program {
            main(){
                Foreach(index In 10 .. 100 By 1000){
                    Out.printInt(arr[x]);
                    If(index % 19 == 4){
                        Break;
                    }
                    Elseif(index % 20 == 1){
                        Continue;
                    }
                    Elseif(index % 9 == 2){
                        Return index;
                    }
                }
            }
        }
        """
        expect = str(
            Program([ClassDecl(Id("Program"),[MethodDecl(Static(),Id("main"),[],Block([For(Id("index"),IntLiteral(10),IntLiteral(100),Block([CallStmt(Id("Out"),Id("printInt"),[ArrayCell(Id("arr"),[Id("x")])]),If(BinaryOp("==",BinaryOp("%",Id("index"),IntLiteral(19)),IntLiteral(4)),Block([Break()]),If(BinaryOp("==",BinaryOp("%",Id("index"),IntLiteral(20)),IntLiteral(1)),Block([Continue()]),If(BinaryOp("==",BinaryOp("%",Id("index"),IntLiteral(9)),IntLiteral(2)),Block([Return(Id("index"))]))))]),IntLiteral(1000))]))])])
        )
        self.assertTrue(TestAST.test(input, expect, 351))
    def test_block(self):
        input = """
        Class Program {
            main(){
                Var r, s: Int;
                r = 2.0;
                Var a, b: Array[Int, 5];
                s = r * r * Self.myPI;
                a[0] = s;
            }
        }
        """
        expect = str(
            Program([ClassDecl(Id("Program"),[MethodDecl(Static(),Id("main"),[],Block([VarDecl(Id("r"),IntType()),VarDecl(Id("s"),IntType()),Assign(Id("r"),FloatLiteral(2.0)),VarDecl(Id("a"),ArrayType(5,IntType())),VarDecl(Id("b"),ArrayType(5,IntType())),Assign(Id("s"),BinaryOp("*",BinaryOp("*",Id("r"),Id("r")),FieldAccess(SelfLiteral(),Id("myPI")))),Assign(ArrayCell(Id("a"),[IntLiteral(0)]),Id("s"))]))])])
        )
        self.assertTrue(TestAST.test(input, expect, 352))
    def test_program_in_the_pdf(self):
        input = """
        Class Shape {
            Val $numOfShape: Int = 0;
            Val immutableAttribute: Int = 0;
            Var length, width: Int;
            $getNumOfShape() {
                Return Shape::$numOfShape;
            }
        }
        Class Rectangle: Shape {
            getArea() {
                Return Self.length * Self.width;
            }
        }
        Class Program {
            main() {
                Out.printInt(Shape::$numOfShape);
            }
        }
        """
        expect = str(
            Program([ClassDecl(Id("Shape"),[AttributeDecl(Static(),ConstDecl(Id("$numOfShape"),IntType(),IntLiteral(0))),AttributeDecl(Instance(),ConstDecl(Id("immutableAttribute"),IntType(),IntLiteral(0))),AttributeDecl(Instance(),VarDecl(Id("length"),IntType())),AttributeDecl(Instance(),VarDecl(Id("width"),IntType())),MethodDecl(Static(),Id("$getNumOfShape"),[],Block([Return(FieldAccess(Id("Shape"),Id("$numOfShape")))]))]),ClassDecl(Id("Rectangle"),[MethodDecl(Instance(),Id("getArea"),[],Block([Return(BinaryOp("*",FieldAccess(SelfLiteral(),Id("length")),FieldAccess(SelfLiteral(),Id("width"))))]))],Id("Shape")),ClassDecl(Id("Program"),[MethodDecl(Static(),Id("main"),[],Block([CallStmt(Id("Out"),Id("printInt"),[FieldAccess(Id("Shape"),Id("$numOfShape"))])]))])])
        )
        self.assertTrue(TestAST.test(input, expect, 353))
    def test_very_complex_array_cell_that_we_will_never_use(self):
        input = """
        Class Shape{
            foo(){
                a[b[c[d[e[f::$g]]]]][h::$i][j.k()][Lzzzzz::$m()]=0;
            }
        }
        """
        expect = str(
            Program([ClassDecl(Id("Shape"),[MethodDecl(Instance(),Id("foo"),[],Block([Assign(ArrayCell(Id("a"),[ArrayCell(Id("b"),[ArrayCell(Id("c"),[ArrayCell(Id("d"),[ArrayCell(Id("e"),[FieldAccess(Id("f"),Id("$g"))])])])]),FieldAccess(Id("h"),Id("$i")),CallExpr(Id("j"),Id("k"),[]),CallExpr(Id("Lzzzzz"),Id("$m"),[])]),IntLiteral(0))]))])])
        )
        self.assertTrue(TestAST.test(input, expect, 354))
    def test_return_stm_6(self):
        input = """Class Program {
            a() {
                Obj.doMany();
                Return Motor::$engihe;
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(a),Instance,[],Block([Call(Id(Obj),Id(doMany),[]),Return(FieldAccess(Id(Motor),Id($engihe)))]))])])"
        self.assertTrue(TestAST.test(input, expect, 355))

    def test_return_stm_7(self):
        input = """Class Program {
            a() {
                Obj.doMany();
                Return Motor::$engihe[1][2][3];
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(a),Instance,[],Block([Call(Id(Obj),Id(doMany),[]),Return(ArrayCell(FieldAccess(Id(Motor),Id($engihe)),[IntLit(1),IntLit(2),IntLit(3)]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 356))

    def test_return_stm_8(self):
        input = """Class Program {
            a() {
                Obj.doMany();
                Return a[1][2][3];
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(a),Instance,[],Block([Call(Id(Obj),Id(doMany),[]),Return(ArrayCell(Id(a),[IntLit(1),IntLit(2),IntLit(3)]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 357))

    def test_return_stm_9(self):
        input = """Class Program {
            a() {
                Obj.doMany();
                Return a.a()[1][2][3];
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(a),Instance,[],Block([Call(Id(Obj),Id(doMany),[]),Return(ArrayCell(CallExpr(Id(a),Id(a),[]),[IntLit(1),IntLit(2),IntLit(3)]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 358))

    def test_return_stm_10(self):
        input = """Class Program {
            a() {
                Obj.doMany();
                Return New X(1, 12, 10 * 20);
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(a),Instance,[],Block([Call(Id(Obj),Id(doMany),[]),Return(NewExpr(Id(X),[IntLit(1),IntLit(12),BinaryOp(*,IntLit(10),IntLit(20))]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 359))

    def test_return_stm_11(self):
        input = """Class Program {
            a() {
                Obj.doMany();
                Return (a == b) || (a > b);
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(a),Instance,[],Block([Call(Id(Obj),Id(doMany),[]),Return(BinaryOp(||,BinaryOp(==,Id(a),Id(b)),BinaryOp(>,Id(a),Id(b))))]))])])"
        self.assertTrue(TestAST.test(input, expect, 360))

    def test_destructor_body_2(self):
        input = """Class Program {
            Destructor() {
                Obj.doMany();
                Return Motor::$engihe[1][2][3];
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(Destructor),Instance,[],Block([Call(Id(Obj),Id(doMany),[]),Return(ArrayCell(FieldAccess(Id(Motor),Id($engihe)),[IntLit(1),IntLit(2),IntLit(3)]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 361))

    def test_constructor_body_2(self):
        input = """Class Program {
            Constructor() {
                Obj.doMany();
                Return Motor::$engihe[1][2][3];
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(Constructor),Instance,[],Block([Call(Id(Obj),Id(doMany),[]),Return(ArrayCell(FieldAccess(Id(Motor),Id($engihe)),[IntLit(1),IntLit(2),IntLit(3)]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 362))

    def test_random_for_each(self):
        line = """
                Class Shape{
                    foo(){
                        Foreach (x In a::$b() .. a.c.c.c By a::$foo){
                            Foreach (x In a::$b() .. a.c.c.c By a::$foo){}
                        }
                    }
                }
                """
        expect = '''Program([ClassDecl(Id(Shape),[MethodDecl(Id(foo),Instance,[],Block([For(Id(x),CallExpr(Id(a),Id($b),[]),FieldAccess(FieldAccess(FieldAccess(Id(a),Id(c)),Id(c)),Id(c)),FieldAccess(Id(a),Id($foo)),Block([For(Id(x),CallExpr(Id(a),Id($b),[]),FieldAccess(FieldAccess(FieldAccess(Id(a),Id(c)),Id(c)),Id(c)),FieldAccess(Id(a),Id($foo)),Block([])])])])]))])])'''
        self.assertTrue(TestAST.test(line, expect, 363))
    def test_for_each_random_again(self):
        line = """
                Class Shape{
                    foo(){
                        If ( a == -1--1){
                            Foreach(x In 1 .. 100 By 2){
                                If ( a == -1--1){
                                    Foreach(x In 1 .. 100 By 2){
                                    }
                                }
                            }
                        }
                    }
                }
                """

        expect = '''Program([ClassDecl(Id(Shape),[MethodDecl(Id(foo),Instance,[],Block([If(BinaryOp(==,Id(a),BinaryOp(-,UnaryOp(-,IntLit(1)),UnaryOp(-,IntLit(1)))),Block([For(Id(x),IntLit(1),IntLit(100),IntLit(2),Block([If(BinaryOp(==,Id(a),BinaryOp(-,UnaryOp(-,IntLit(1)),UnaryOp(-,IntLit(1)))),Block([For(Id(x),IntLit(1),IntLit(100),IntLit(2),Block([])])]))])])]))]))])])'''
        self.assertTrue(TestAST.test(line, expect, 364))

    def test_zero_initals(self):
        """Static access, instance and index combine"""
        input = """Class Program {
            Val b : Int = ClassABC::$a.a.c.b[1][2][3][(0 + 012 + 0xA2 + 0XA2 +0b101+0B101)];
            Var c : Int = 0x0 + 0X0 + 0b0 + 0B0 + 00 + 0;
        }"""
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(b),IntType,ArrayCell(FieldAccess(FieldAccess(FieldAccess(FieldAccess(Id(ClassABC),Id($a)),Id(a)),Id(c)),Id(b)),[IntLit(1),IntLit(2),IntLit(3),BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(+,IntLit(0),IntLit(10)),IntLit(162)),IntLit(162)),IntLit(5)),IntLit(5))]))),AttributeDecl(Instance,VarDecl(Id(c),IntType,BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(+,IntLit(0),IntLit(0)),IntLit(0)),IntLit(0)),IntLit(0)),IntLit(0))))])])"
        self.assertTrue(TestAST.test(input, expect, 365))

    def test_block_stm_1(self):
        input = """Class Program {
            aaa() {
                Self.print(a);
                {
                    Self.doSth();
                    Continue;
                }
                Return Self.Something();
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(aaa),Instance,[],Block([Call(Self(),Id(print),[Id(a)]),Block([Call(Self(),Id(doSth),[]),Continue]),Return(CallExpr(Self(),Id(Something),[]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 366))

    def test_val_decl_stm_1(self):
        input = """Class Program {
            a() {
                Val a : Int;
                Val b : String;
                Val c, d : Array[Float, 2];
                Self.print(a);
                Self.print(b +. Self.convertToString(a));
                Self.print(c * d);
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(a),Instance,[],Block([ConstDecl(Id(a),IntType,None),ConstDecl(Id(b),StringType,None),ConstDecl(Id(c),ArrayType(2,FloatType),None),ConstDecl(Id(d),ArrayType(2,FloatType),None),Call(Self(),Id(print),[Id(a)]),Call(Self(),Id(print),[BinaryOp(+.,Id(b),CallExpr(Self(),Id(convertToString),[Id(a)]))]),Call(Self(),Id(print),[BinaryOp(*,Id(c),Id(d))])]))])])"
        self.assertTrue(TestAST.test(input, expect, 367))

    def test_val_decl_stm_2(self):
        input = """Class Program {
            a() {
                Val a : Int = 10;
                Val b : String = "Hello World";
                Val c, d : Array[Float, 2] = Array(.e5, 1.0), Array(1e-1, 4.4);
                Self.print(a);
                Self.print(b +. Self.convertToString(a));
                Self.print(c * d);
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(a),Instance,[],Block([ConstDecl(Id(a),IntType,IntLit(10)),ConstDecl(Id(b),StringType,StringLit(Hello World)),ConstDecl(Id(c),ArrayType(2,FloatType),[FloatLit(0.0),FloatLit(1.0)]),ConstDecl(Id(d),ArrayType(2,FloatType),[FloatLit(0.1),FloatLit(4.4)]),Call(Self(),Id(print),[Id(a)]),Call(Self(),Id(print),[BinaryOp(+.,Id(b),CallExpr(Self(),Id(convertToString),[Id(a)]))]),Call(Self(),Id(print),[BinaryOp(*,Id(c),Id(d))])]))])])"
        self.assertTrue(TestAST.test(input, expect, 368))

    def test_val_decl_stm_3(self):
        input = """Class Program {
            a() {
                Val a : AClass = New X(1, 2, 3);
                Var b : Int = a + b + c;
                Var c : Float = 1.0;
                Var d : String = c +. " World";
                Self.print(a);
                Self.print(b +. Self.convertToString(a));
                Self.print(c * d);
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(a),Instance,[],Block([ConstDecl(Id(a),ClassType(Id(AClass)),NewExpr(Id(X),[IntLit(1),IntLit(2),IntLit(3)])),VarDecl(Id(b),IntType,BinaryOp(+,BinaryOp(+,Id(a),Id(b)),Id(c))),VarDecl(Id(c),FloatType,FloatLit(1.0)),VarDecl(Id(d),StringType,BinaryOp(+.,Id(c),StringLit( World))),Call(Self(),Id(print),[Id(a)]),Call(Self(),Id(print),[BinaryOp(+.,Id(b),CallExpr(Self(),Id(convertToString),[Id(a)]))]),Call(Self(),Id(print),[BinaryOp(*,Id(c),Id(d))])]))])])"
        self.assertTrue(TestAST.test(input, expect, 369))

    def test_assign_stm_1(self):
        input = """Class Program {
            a() {
                Val a : Int;
                a = 1 + 1 + a - 3 * b / 7 + d;
                Self.print(a);
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(a),Instance,[],Block([ConstDecl(Id(a),IntType,None),AssignStmt(Id(a),BinaryOp(+,BinaryOp(-,BinaryOp(+,BinaryOp(+,IntLit(1),IntLit(1)),Id(a)),BinaryOp(/,BinaryOp(*,IntLit(3),Id(b)),IntLit(7))),Id(d))),Call(Self(),Id(print),[Id(a)])]))])])"
        self.assertTrue(TestAST.test(input, expect, 370))

    def test_assign_stm_2(self):
        input = """Class Program {
            a() {
                Val a : ClassAC = Null;
                a = New X(1 + 1, a - 3 * b, 10 / 7 + d);
                Self.print(a.a);
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(a),Instance,[],Block([ConstDecl(Id(a),ClassType(Id(ClassAC)),NullLiteral()),AssignStmt(Id(a),NewExpr(Id(X),[BinaryOp(+,IntLit(1),IntLit(1)),BinaryOp(-,Id(a),BinaryOp(*,IntLit(3),Id(b))),BinaryOp(+,BinaryOp(/,IntLit(10),IntLit(7)),Id(d))])),Call(Self(),Id(print),[FieldAccess(Id(a),Id(a))])]))])])"
        self.assertTrue(TestAST.test(input, expect, 371))

    def test_assign_stm_3(self):
        input = """Class Program {
            a() {
                Val a : ClassAC = Null;
                a = New X(1 + 1, a - 3 * b, 10 / 7 + d);
                a.a = 10;
                a.b = -100.00 + a.foo();
                Self.print(a.a);
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(a),Instance,[],Block([ConstDecl(Id(a),ClassType(Id(ClassAC)),NullLiteral()),AssignStmt(Id(a),NewExpr(Id(X),[BinaryOp(+,IntLit(1),IntLit(1)),BinaryOp(-,Id(a),BinaryOp(*,IntLit(3),Id(b))),BinaryOp(+,BinaryOp(/,IntLit(10),IntLit(7)),Id(d))])),AssignStmt(FieldAccess(Id(a),Id(a)),IntLit(10)),AssignStmt(FieldAccess(Id(a),Id(b)),BinaryOp(+,UnaryOp(-,FloatLit(100.0)),CallExpr(Id(a),Id(foo),[]))),Call(Self(),Id(print),[FieldAccess(Id(a),Id(a))])]))])])"
        self.assertTrue(TestAST.test(input, expect, 372))

    def test_assign_stm_4(self):
        input = """Class Program {
            a() {
                Val a : ClassAC = Null;
                a = New X(1 + 1, a - 3 * b, 10 / 7 + d);
                a.a = 10;
                a.b = -100.00 + a.foo();
                a.a.b[1] = Array(1, 2, 3);
                Self.print(a.a);
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(a),Instance,[],Block([ConstDecl(Id(a),ClassType(Id(ClassAC)),NullLiteral()),AssignStmt(Id(a),NewExpr(Id(X),[BinaryOp(+,IntLit(1),IntLit(1)),BinaryOp(-,Id(a),BinaryOp(*,IntLit(3),Id(b))),BinaryOp(+,BinaryOp(/,IntLit(10),IntLit(7)),Id(d))])),AssignStmt(FieldAccess(Id(a),Id(a)),IntLit(10)),AssignStmt(FieldAccess(Id(a),Id(b)),BinaryOp(+,UnaryOp(-,FloatLit(100.0)),CallExpr(Id(a),Id(foo),[]))),AssignStmt(ArrayCell(FieldAccess(FieldAccess(Id(a),Id(a)),Id(b)),[IntLit(1)]),[IntLit(1),IntLit(2),IntLit(3)]),Call(Self(),Id(print),[FieldAccess(Id(a),Id(a))])]))])])"
        self.assertTrue(TestAST.test(input, expect, 373))

    def test_assign_stm_5(self):
        input = """Class Program {
            $a() {
                MotorBike::$eng = Array(1, 2+a, a * b);
                a[1][(i - j)][3] = c[i][k] + b[1][(j+1)][(k - 2)][3];

                Self.print(a.a);
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id($a),Static,[],Block([AssignStmt(FieldAccess(Id(MotorBike),Id($eng)),[IntLit(1),BinaryOp(+,IntLit(2),Id(a)),BinaryOp(*,Id(a),Id(b))]),AssignStmt(ArrayCell(Id(a),[IntLit(1),BinaryOp(-,Id(i),Id(j)),IntLit(3)]),BinaryOp(+,ArrayCell(Id(c),[Id(i),Id(k)]),ArrayCell(Id(b),[IntLit(1),BinaryOp(+,Id(j),IntLit(1)),BinaryOp(-,Id(k),IntLit(2)),IntLit(3)]))),Call(Self(),Id(print),[FieldAccess(Id(a),Id(a))])]))])])"
        self.assertTrue(TestAST.test(input, expect, 374))

    def test_assign_stm_6(self):
        input = """Class Program {
            $a() {
                a.f().a[1][23] = a.foo() +. AClass::$foo();
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id($a),Static,[],Block([AssignStmt(ArrayCell(FieldAccess(CallExpr(Id(a),Id(f),[]),Id(a)),[IntLit(1),IntLit(23)]),BinaryOp(+.,CallExpr(Id(a),Id(foo),[]),CallExpr(Id(AClass),Id($foo),[])))]))])])"
        self.assertTrue(TestAST.test(input, expect, 375))

    def test_foreach_stm_1(self):
        input = """Class Program {
            a() {
                Foreach (a In 1 .. 100 By 2) {
                    Self.print(a + 1);
                    b = a * 2;
                    Self.print(b.a.c);
                }
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(a),Instance,[],Block([For(Id(a),IntLit(1),IntLit(100),IntLit(2),Block([Call(Self(),Id(print),[BinaryOp(+,Id(a),IntLit(1))]),AssignStmt(Id(b),BinaryOp(*,Id(a),IntLit(2))),Call(Self(),Id(print),[FieldAccess(FieldAccess(Id(b),Id(a)),Id(c))])])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 376))

    
    def test_random_stuffs_that_I_do_not_know(self):
        input = """Class Program {
            main() {
                (a[1]).func();
                a[1] = 1;
                Out.println(a.a[1]);
                ((((a[1][2]).a[1]).func()[0]).a[1]).func();
                Return;
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(ArrayCell(Id(a),[IntLit(1)]),Id(func),[]),AssignStmt(ArrayCell(Id(a),[IntLit(1)]),IntLit(1)),Call(Id(Out),Id(println),[ArrayCell(FieldAccess(Id(a),Id(a)),[IntLit(1)])]),Call(ArrayCell(FieldAccess(ArrayCell(CallExpr(ArrayCell(FieldAccess(ArrayCell(Id(a),[IntLit(1),IntLit(2)]),Id(a)),[IntLit(1)]),Id(func),[]),[IntLit(0)]),Id(a)),[IntLit(1)]),Id(func),[]),Return()]))])])"
        self.assertTrue(TestAST.test(input, expect, 377))

    def test_foreach_stm_2(self):
        input = """Class Program {
            a() {
                Foreach (a In b + c .. b - c * 100) {
                    Self.print(a);
                }
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(a),Instance,[],Block([For(Id(a),BinaryOp(+,Id(b),Id(c)),BinaryOp(-,Id(b),BinaryOp(*,Id(c),IntLit(100))),IntLit(1),Block([Call(Self(),Id(print),[Id(a)])])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 378))

    def test_foreach_stm_3(self):
        input = """Class Program {
            a() {
                Foreach (a In New X(1, 2, 3) .. Self.foo().a.bar() By MotherBoard::$capacitor.foo()) {
                    Self.print(a);
                }
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(a),Instance,[],Block([For(Id(a),NewExpr(Id(X),[IntLit(1),IntLit(2),IntLit(3)]),CallExpr(FieldAccess(CallExpr(Self(),Id(foo),[]),Id(a)),Id(bar),[]),CallExpr(FieldAccess(Id(MotherBoard),Id($capacitor)),Id(foo),[]),Block([Call(Self(),Id(print),[Id(a)])])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 379))

    def test_if_stm_1(self):
        input = """Class Program {
            a() {
                If (a == b) {
                    Self.print("Hurray");
                } Else {
                    Self.print("Oh no");
                }
            }    
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(a),Instance,[],Block([If(BinaryOp(==,Id(a),Id(b)),Block([Call(Self(),Id(print),[StringLit(Hurray)])]),Block([Call(Self(),Id(print),[StringLit(Oh no)])]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 380))

    def test_if_stm_2(self):
        input = """Class Program {
            a() {
                If (a == b) {
                    Self.print("Hurray");
                } Elseif (a > b) {
                    Self.print("Greater");
                } Else {
                    Self.print("Oh no");
                }
            }    
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(a),Instance,[],Block([If(BinaryOp(==,Id(a),Id(b)),Block([Call(Self(),Id(print),[StringLit(Hurray)])]),If(BinaryOp(>,Id(a),Id(b)),Block([Call(Self(),Id(print),[StringLit(Greater)])]),Block([Call(Self(),Id(print),[StringLit(Oh no)])])))]))])])"
        self.assertTrue(TestAST.test(input, expect, 381))

    def test_if_stm_3(self):
        input = """Class Program {
            a() {
                If (a == b) {
                    Self.print("Hurray");
                } Elseif (a > b) {
                    Self.print("Greater");
                } Elseif (a < b) {
                    Self.print("Less");
                } Else {
                    Self.print("Oh no");
                }
            }    
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(a),Instance,[],Block([If(BinaryOp(==,Id(a),Id(b)),Block([Call(Self(),Id(print),[StringLit(Hurray)])]),If(BinaryOp(>,Id(a),Id(b)),Block([Call(Self(),Id(print),[StringLit(Greater)])]),If(BinaryOp(<,Id(a),Id(b)),Block([Call(Self(),Id(print),[StringLit(Less)])]),Block([Call(Self(),Id(print),[StringLit(Oh no)])]))))]))])])"
        self.assertTrue(TestAST.test(input, expect, 382))

    def test_if_stm_4(self):
        input = """Class Program {
            a() {
                If (a == b) {
                    Self.print("Hurray");
                } Elseif (a > b) {
                    Self.print("Greater");
                } Elseif (a < b) {
                    Self.print("Less");
                }
            }    
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(a),Instance,[],Block([If(BinaryOp(==,Id(a),Id(b)),Block([Call(Self(),Id(print),[StringLit(Hurray)])]),If(BinaryOp(>,Id(a),Id(b)),Block([Call(Self(),Id(print),[StringLit(Greater)])]),If(BinaryOp(<,Id(a),Id(b)),Block([Call(Self(),Id(print),[StringLit(Less)])]))))]))])])"
        self.assertTrue(TestAST.test(input, expect, 383))

    def test_if_stm_5(self):
        input = """Class Program {
            a() {
                If (a == b) {
                    Self.print("Hurray");
                }
            }    
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(a),Instance,[],Block([If(BinaryOp(==,Id(a),Id(b)),Block([Call(Self(),Id(print),[StringLit(Hurray)])]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 384))

    def test_if_stm_6(self):
        input = """Class Program {
            a() {
                If (a == b) {
                    Foreach (i In j .. b By a/2) {
                        b = b + 1;
                        c = b * a;
                        d = c / 2;
                        Self.print(d.foo().a.bar());
                    }
                } Elseif ((a < b) || (b < d) && (i == (j + 1))) {
                    If (a == b) {
                        Self.print("Index out of bound");
                    } Else {
                        a[1][2][(b+1)] = c[(b+2)][(b*2)];
                    }
                } Else {
                    Out.println("An error has occured");
                }
            }    
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(a),Instance,[],Block([If(BinaryOp(==,Id(a),Id(b)),Block([For(Id(i),Id(j),Id(b),BinaryOp(/,Id(a),IntLit(2)),Block([AssignStmt(Id(b),BinaryOp(+,Id(b),IntLit(1))),AssignStmt(Id(c),BinaryOp(*,Id(b),Id(a))),AssignStmt(Id(d),BinaryOp(/,Id(c),IntLit(2))),Call(Self(),Id(print),[CallExpr(FieldAccess(CallExpr(Id(d),Id(foo),[]),Id(a)),Id(bar),[])])])])]),If(BinaryOp(&&,BinaryOp(||,BinaryOp(<,Id(a),Id(b)),BinaryOp(<,Id(b),Id(d))),BinaryOp(==,Id(i),BinaryOp(+,Id(j),IntLit(1)))),Block([If(BinaryOp(==,Id(a),Id(b)),Block([Call(Self(),Id(print),[StringLit(Index out of bound)])]),Block([AssignStmt(ArrayCell(Id(a),[IntLit(1),IntLit(2),BinaryOp(+,Id(b),IntLit(1))]),ArrayCell(Id(c),[BinaryOp(+,Id(b),IntLit(2)),BinaryOp(*,Id(b),IntLit(2))]))]))]),Block([Call(Id(Out),Id(println),[StringLit(An error has occured)])])))]))])])"
        self.assertTrue(TestAST.test(input, expect, 385))

    def test_if_stm_7(self):
        input = """Class Program {
            a() {
                Foreach (i In 0 .. 1000 By a) {
                    If (i == 100) {
                        Break;
                    } Else {
                        i = i + 1;
                    }
                }
                Self.print(a.a.foo());
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(a),Instance,[],Block([For(Id(i),IntLit(0),IntLit(1000),Id(a),Block([If(BinaryOp(==,Id(i),IntLit(100)),Block([Break]),Block([AssignStmt(Id(i),BinaryOp(+,Id(i),IntLit(1)))]))])]),Call(Self(),Id(print),[CallExpr(FieldAccess(Id(a),Id(a)),Id(foo),[])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 386))

    def test_if_stm_8(self):
        input = """Class Program {
            a() {
                Foreach (i In 0 .. 1000 By a) {
                    If (i == 100) {
                        Continue;
                    } Else {
                        i = i + 1;
                    }
                }
                Self.print(a.a.foo());
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(a),Instance,[],Block([For(Id(i),IntLit(0),IntLit(1000),Id(a),Block([If(BinaryOp(==,Id(i),IntLit(100)),Block([Continue]),Block([AssignStmt(Id(i),BinaryOp(+,Id(i),IntLit(1)))]))])]),Call(Self(),Id(print),[CallExpr(FieldAccess(Id(a),Id(a)),Id(foo),[])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 387))

    def test_if_stm_9(self):
        input = """Class Program {
            a() {
                Foreach (i In 0 .. 1000 By a) {
                    If (i == 100) {
                        Return New X();
                    } Else {
                        i = i + 1;
                    }
                }
                Self.print(a.a.foo());
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(a),Instance,[],Block([For(Id(i),IntLit(0),IntLit(1000),Id(a),Block([If(BinaryOp(==,Id(i),IntLit(100)),Block([Return(NewExpr(Id(X),[]))]),Block([AssignStmt(Id(i),BinaryOp(+,Id(i),IntLit(1)))]))])]),Call(Self(),Id(print),[CallExpr(FieldAccess(Id(a),Id(a)),Id(foo),[])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 388))

    def test_main_func_1(self):
        """main inside Program class -> static, not Program -> instance"""
        input = """Class Program {
            main() {}
        }
        Class ABC {
            main() {}
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([]))]),ClassDecl(Id(ABC),[MethodDecl(Id(main),Instance,[],Block([]))])])"
        self.assertTrue(TestAST.test(input, expect, 389))

    def test_main_func_2(self):
        """main() inside Program class -> static, main(params) -> instance"""
        input = """Class Program {
            main() {}
            main(w, h: Int) {}
        }
        Class ABC {
            main() {}
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([])),MethodDecl(Id(main),Instance,[param(Id(w),IntType),param(Id(h),IntType)],Block([]))]),ClassDecl(Id(ABC),[MethodDecl(Id(main),Instance,[],Block([]))])])"
        self.assertTrue(TestAST.test(input, expect, 390))

    def test_simple_program_4(self):
        input = """Class Program {
            main() {
                Val a : Int;
                Foreach (i In 1 .. 100 By 1)
                {
                    Clib.printf("enter the number:");
                    Clib.scanf("%d", a);
                    If ( a == 0 ) {
                        Break;
                    }
                }
                Return 0;
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([ConstDecl(Id(a),IntType,None),For(Id(i),IntLit(1),IntLit(100),IntLit(1),Block([Call(Id(Clib),Id(printf),[StringLit(enter the number:)]),Call(Id(Clib),Id(scanf),[StringLit(%d),Id(a)]),If(BinaryOp(==,Id(a),IntLit(0)),Block([Break]))])]),Return(IntLit(0))]))])])"
        self.assertTrue(TestAST.test(input, expect, 391))

    def test_matrix_mul_2(self):
        input = """Class So : A {
            Val a : Array[Array[Int, 5], 5];
            main() {
                c[i][j] = c[i][j] + a[i][k] * b[k][j];
            }
        }"""
        expect = "Program([ClassDecl(Id(So),Id(A),[AttributeDecl(Instance,ConstDecl(Id(a),ArrayType(5,ArrayType(5,IntType)),None)),MethodDecl(Id(main),Instance,[],Block([AssignStmt(ArrayCell(Id(c),[Id(i),Id(j)]),BinaryOp(+,ArrayCell(Id(c),[Id(i),Id(j)]),BinaryOp(*,ArrayCell(Id(a),[Id(i),Id(k)]),ArrayCell(Id(b),[Id(k),Id(j)]))))]))])])"
        self.assertTrue(TestAST.test(input, expect, 392))

    def test_simple_program_5(self):
        input = """Class Program {
                    main() {
                        (a[1]).func();
                        a[1] = 1;
                        Out.println(a.a[1]);
                        ((((a[1][2]).a[1]).func()[0]).a[1]).func();
                        Return;
                    }
                }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(ArrayCell(Id(a),[IntLit(1)]),Id(func),[]),AssignStmt(ArrayCell(Id(a),[IntLit(1)]),IntLit(1)),Call(Id(Out),Id(println),[ArrayCell(FieldAccess(Id(a),Id(a)),[IntLit(1)])]),Call(ArrayCell(FieldAccess(ArrayCell(CallExpr(ArrayCell(FieldAccess(ArrayCell(Id(a),[IntLit(1),IntLit(2)]),Id(a)),[IntLit(1)]),Id(func),[]),[IntLit(0)]),Id(a)),[IntLit(1)]),Id(func),[]),Return()]))])])"
        self.assertTrue(TestAST.test(input, expect, 393))

    def test_complex_array_cells(self):
        input = """
        Class Program {
            main() {
                a[1][exp::$b().c[exp::$b().c[exp::$b().c]]] = 1;
            }
        }"""
        expect = str(
            Program([ClassDecl(Id("Program"),[MethodDecl(Static(),Id("main"),[],Block([Assign(ArrayCell(Id("a"),[IntLiteral(1),ArrayCell(FieldAccess(CallExpr(Id("exp"),Id("$b"),[]),Id("c")),[ArrayCell(FieldAccess(CallExpr(Id("exp"),Id("$b"),[]),Id("c")),[FieldAccess(CallExpr(Id("exp"),Id("$b"),[]),Id("c"))])])]),IntLiteral(1))]))])])
        )
        self.assertTrue(TestAST.test(input, expect, 394))
    def test_complex_accesse(self):
        input = """
        Class Program {
            a() {
                A.a.a.foo();
                (a.a[1][2][3]).foo();
                MotorBike::$ab.foo();
                (MotorBike::$a.a[1][2]).foo();
            }
        }"""
        expect = str(
            Program([ClassDecl(Id("Program"),[MethodDecl(Instance(),Id("a"),[],Block([CallStmt(FieldAccess(FieldAccess(Id("A"),Id("a")),Id("a")),Id("foo"),[]),CallStmt(ArrayCell(FieldAccess(Id("a"),Id("a")),[IntLiteral(1),IntLiteral(2),IntLiteral(3)]),Id("foo"),[]),CallStmt(FieldAccess(Id("MotorBike"),Id("$ab")),Id("foo"),[]),CallStmt(ArrayCell(FieldAccess(FieldAccess(Id("MotorBike"),Id("$a")),Id("a")),[IntLiteral(1),IntLiteral(2)]),Id("foo"),[])]))])])
        )
        self.assertTrue(TestAST.test(input, expect, 395))
    def test_overall_data_types(self):
        input = """
        Class Dog {
            Val a : Int = 1;
            Val b : Float = 1.4;
            Val c : String = "abc";
            Val d : Boolean = True;
            Val e : Array[Int, 5] = Array(1, 5, 7, 12, 8);
            Val f : Animal = New Animal();
            Var g : Animal;
            Val h : Animal;
            Val i : Array[Array[Int, 5], 2] = Array(Array(1,2,3,4,5), Array(1,2,3,4,5));
        }
        """
        expect = str(
            Program([ClassDecl(Id("Dog"),[
                AttributeDecl(Instance(),ConstDecl(Id("a"),IntType(),IntLiteral(1))),
                AttributeDecl(Instance(),ConstDecl(Id("b"),FloatType(),FloatLiteral(1.4))),
                AttributeDecl(Instance(),ConstDecl(Id("c"),StringType(),StringLiteral("abc"))),
                AttributeDecl(Instance(),ConstDecl(Id("d"),BoolType(),BooleanLiteral(True))),
                AttributeDecl(Instance(),ConstDecl(Id("e"),ArrayType(5,IntType()),ArrayLiteral([IntLiteral(1),IntLiteral(5),IntLiteral(7),IntLiteral(12),IntLiteral(8)]))),
                AttributeDecl(Instance(),ConstDecl(Id("f"),ClassType(Id("Animal")),NewExpr(Id("Animal"),[]))),
                AttributeDecl(Instance(),VarDecl(Id("g"),ClassType(Id("Animal")),NullLiteral())),
                AttributeDecl(Instance(),ConstDecl(Id("h"),ClassType(Id("Animal")),None)),
                AttributeDecl(Instance(),ConstDecl(Id("i"),ArrayType(2,ArrayType(5,IntType())),ArrayLiteral([ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(5)]),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(5)])])))])])
        )
        self.assertTrue(TestAST.test(input, expect, 396))
    def test_integer_literals(self):
        input = """
        Class IntLit {
            Val a : Int = 1_234_567;
            Val b : Int = 1_2_3_4_5_6_7;
            Val c : Int = 0b110;
            Val d : Int = 0123456;
            Val e : Int = 0x123456789ABCDEF;
        }
        """
        expect = str(
            Program([ClassDecl(Id("IntLit"),[AttributeDecl(Instance(),ConstDecl(Id("a"),IntType(),IntLiteral(1234567))),AttributeDecl(Instance(),ConstDecl(Id("b"),IntType(),IntLiteral(1234567))),AttributeDecl(Instance(),ConstDecl(Id("c"),IntType(),IntLiteral(6))),AttributeDecl(Instance(),ConstDecl(Id("d"),IntType(),IntLiteral(42798))),AttributeDecl(Instance(),ConstDecl(Id("e"),IntType(),IntLiteral(81985529216486895)))])])
        )
        self.assertTrue(TestAST.test(input, expect, 397))
    def test_self_keywords(self):
        input = """
        Class ABC {
            Var w, h : Int;

            Constructor(w: Int; h: Int) {
                Self.w = w;
                Self.h = h;
                Return;
            }
        }
        """
        expect = str(
            Program([ClassDecl(Id("ABC"),[AttributeDecl(Instance(),VarDecl(Id("w"),IntType())),AttributeDecl(Instance(),VarDecl(Id("h"),IntType())),MethodDecl(Instance(),Id("Constructor"),[VarDecl(Id("w"),IntType()),VarDecl(Id("h"),IntType())],Block([Assign(FieldAccess(SelfLiteral(),Id("w")),Id("w")),Assign(FieldAccess(SelfLiteral(),Id("h")),Id("h")),Return()]))])])
        )
        self.assertTrue(TestAST.test(input, expect, 398))
    def test_calling_class_functions(self):
        input = """
        Class Program {
            main(){
                Return New X().Y();
            }
        }
        """
        expect = str(
            Program([ClassDecl(Id("Program"),[MethodDecl(Static(),Id("main"),[],Block([Return(CallExpr(NewExpr(Id("X"),[]),Id("Y"),[]))]))])])
        )
        self.assertTrue(TestAST.test(input, expect, 399))