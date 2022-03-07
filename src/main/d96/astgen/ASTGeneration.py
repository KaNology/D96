from D96Visitor import D96Visitor
from D96Parser import D96Parser
from AST import *
from functools import reduce


class ASTGeneration(D96Visitor):
    def __init__(self):
        self.attr_list = []
        self.attr_exp_list = []
        self.attr_type = None
        self.decl_list = []
        self.decl_exp_list = []
        self.decl_type = None
        self.current_class = None


    def visitProgram(self, ctx: D96Parser.ProgramContext):
        return Program([self.visit(decl) for decl in ctx.classDeclaration()])

    def visitClassDeclaration(self, ctx: D96Parser.ClassDeclarationContext):
        # ClassDecl(classname: Id , memlist: List[MemDecl] , parentname?: Id)
        class_name = Id(ctx.ID(0).getText())
        self.current_class = ctx.ID(0).getText()
        class_body = self.visit(ctx.classBody())
        self.current_class = None
        class_parent = Id(ctx.ID(1).getText()) if ctx.ID(1) else None

        return ClassDecl(
            class_name, class_body, class_parent
        )

    def visitClassBody(self, ctx: D96Parser.ClassBodyContext):
        size = ctx.getChildCount()
        declList = []
        for i in range(size):
            declList += self.visit(ctx.getChild(i))

        return declList

    # def visitAttrDeclaration(self, ctx: D96Parser.AttrDeclarationContext):
    #     attrList = self.visit(ctx.attrList()) # type and id
    #     type = self.visit(ctx.typeName()) # literal type
    #     exp = [self.visit(exp) for exp in ctx.exp()] if ctx.exp() else None # exp

    #     if(ctx.exp()):
            # return reduce(
            #     lambda acc, ele:
            #     acc + [AttributeDecl(
            #         ele[0][0],
            #         ConstDecl(ele[0][1], type, ele[1]) if ctx.VAL() else VarDecl(ele[0][1], type, ele[1])
            #     )],
            #     zip(attrList, exp),
            #     []
            # )
    #     return reduce(
    #             lambda acc, ele:
    #             acc + [AttributeDecl(
    #                 ele[0],
    #                 ConstDecl(ele[1], type, None) if ctx.VAL() else VarDecl(ele[1], type, None)
    #             )],
    #             attrList,
    #             []
    #         )

    def visitAttrDeclaration(self, ctx: D96Parser.AttrDeclarationContext):
        if(ctx.attrWithoutAssign()):
            attrList = self.visit(ctx.attrWithoutAssign()) # [(Id, type), (Id, type), ..., literal_type]
            type = attrList[-1]
            init = NullLiteral() if isinstance(type, ClassType) and ctx.VAR() else None
            return reduce(
                lambda acc, ele:
                acc + [AttributeDecl(
                    ele[0],
                    ConstDecl(Id(ele[1]), type, init) if ctx.VAL() else VarDecl(Id(ele[1]), type, init)
                )],
                attrList[:-1],
                []
            )
        elif(ctx.attrWithAssign()):
            self.visit(ctx.attrWithAssign())
            attrList = self.attr_list
            exp = self.attr_exp_list[::-1]

            finalList = zip(attrList, exp)
            self.attr_list = []
            self.attr_exp_list = []
            type = self.attr_type

            return reduce(
                lambda acc, ele:
                acc + [AttributeDecl(
                    ele[0][0],
                    ConstDecl(Id(ele[0][1]), type, ele[1]) if ctx.VAL() else VarDecl(Id(ele[0][1]), type, ele[1])
                )],
                finalList,
                []
            )

    def visitAttrWithAssign(self, ctx: D96Parser.AttrWithAssignContext):
        self.attr_list.append(self.visit(ctx.identifier()))
        self.attr_exp_list.append(self.visit(ctx.exp()))
        if(ctx.attrPair()):
            self.visit(ctx.attrPair())
        return None

    def visitAttrPair(self, ctx: D96Parser.AttrPairContext):
        if(ctx.COMMA()):
            self.attr_list.append(self.visit(ctx.identifier()))
            self.attr_exp_list.append(self.visit(ctx.exp()))
            self.visit(ctx.attrPair())
            return None
        elif(ctx.ASSIGN()):
            self.attr_type = self.visit(ctx.typeName())

    def visitAttrWithoutAssign(self, ctx: D96Parser.AttrWithoutAssignContext):
        attrList = self.visit(ctx.attrList()) # [(type, Id), (type, Id)]
        typeName = [self.visit(ctx.typeName())]
        return attrList + typeName

    def visitAttrList(self, ctx: D96Parser.AttrListContext):
        return [self.visit(id) for id in ctx.identifier()]

    def visitIdentifier(self, ctx: D96Parser.IdentifierContext):
        if(ctx.ID()):
            return (Instance(), ctx.ID().getText())
        else:
            return (Static(), ctx.DOLLAR_ID().getText())

    def visitTypeName(self, ctx: D96Parser.TypeNameContext):
        if(ctx.primitiveType()):
            return self.visit(ctx.primitiveType())
        elif(ctx.arrayType()):
            return self.visit(ctx.arrayType())
        else:
            return self.visit(ctx.classType())

    def visitMethodDeclaration(self, ctx: D96Parser.MethodDeclarationContext):
        # MethodDecl(kind: SIKind , name: Id , param: List[VarDecl] , body: Block)
        method = self.visit(ctx.identifier()) if ctx.identifier() else None  # method type and method ID
        if(ctx.CONSTRUCTOR()):
            method = (Instance(), ctx.CONSTRUCTOR().getText())
        elif(ctx.DESTRUCTOR()):
            method = (Instance(), ctx.DESTRUCTOR().getText())

        param = self.visit(ctx.paraList()) if ctx.paraList() else []
        block = self.visit(ctx.blockStmt())

        if(method[1] == "main" and param == [] and self.current_class == "Program"):
            method = (Static(), method[1])

        return [MethodDecl(method[0], Id(method[1]), param, block)]

    def visitParaList(self, ctx: D96Parser.ParaListContext):
        para_list = [self.visit(decl) for decl in ctx.paraDeclaration()]
        return [decl for para in para_list for decl in para]

    def visitParaDeclaration(self, ctx: D96Parser.ParaDeclarationContext):
        id_list = self.visit(ctx.idList())
        type = self.visit(ctx.typeName())
        para_list = []

        for id in id_list:
            para_list.append(VarDecl(id, type, None))
        return para_list

    def visitIdList(self, ctx: D96Parser.IdListContext):
        return [Id(id.getText()) for id in ctx.ID()]

    def visitPrimitiveType(self, ctx: D96Parser.PrimitiveTypeContext):
        if(ctx.BOOLEAN()):
            return BoolType()
        elif(ctx.INT()):
            return IntType()
        elif(ctx.FLOAT()):
            return FloatType()
        else:
            return StringType()

    def visitArrayType(self, ctx: D96Parser.ArrayTypeContext):
        return ArrayType(
            self.visit(ctx.intLit()),
            self.visit(ctx.elementType())
        )

    def visitElementType(self, ctx: D96Parser.ElementTypeContext):
        if(ctx.primitiveType()):
            return self.visit(ctx.primitiveType())
        else:
            return self.visit(ctx.arrayType())

    def visitClassType(self, ctx: D96Parser.ClassTypeContext):
        return ClassType(Id(ctx.ID().getText()))

    def visitStmt(self, ctx: D96Parser.StmtContext):
        if(ctx.blockStmt()):
            return self.visit(ctx.blockStmt())
        elif(ctx.assignStmt()):
            return self.visit(ctx.assignStmt())
        elif(ctx.ifStmt()):
            return self.visit(ctx.ifStmt())
        elif(ctx.forInStmt()):
            return self.visit(ctx.forInStmt())
        elif(ctx.breakStmt()):
            return self.visit(ctx.breakStmt())
        elif(ctx.continueStmt()):
            return self.visit(ctx.continueStmt())
        elif(ctx.returnStmt()):
            return self.visit(ctx.returnStmt())
        elif(ctx.instanceCall()):
            return self.visit(ctx.instanceCall())
        elif(ctx.declarationStmt()):
            return self.visit(ctx.declarationStmt())
        elif(ctx.staticCall()):
            return self.visit(ctx.staticCall())

    # def visitDeclarationStmt(self, ctx: D96Parser.DeclarationStmtContext):
    #     varList = self.visit(ctx.varList())  # id
    #     type = self.visit(ctx.typeName())  # literal type
    #     exp = [self.visit(exp)
    #            for exp in ctx.exp()] if ctx.exp() else None  # exp

    #     if(ctx.exp()):
            # return reduce(
            #     lambda acc, ele:
            #     acc + [
            #         ConstDecl(ele[0], type, ele[1]) if ctx.VAL(
            #         ) else VarDecl(ele[0], type, ele[1])
            #     ],
            #     zip(varList, exp),
            #     []
            # )
        # return reduce(
        #     lambda acc, ele:
        #     acc + [
        #         ConstDecl(ele, type, None) if ctx.VAL(
        #         ) else VarDecl(ele, type, None)
        #     ],
        #     varList,
        #     []
        # )

    def visitDeclarationStmt(self, ctx: D96Parser.DeclarationStmtContext):
        if(ctx.declarationWithoutAssign()):
            varList = self.visit(ctx.declarationWithoutAssign()) # [Id, Id, ..., literal_type]
            type = varList[-1]
            init = NullLiteral() if isinstance(type, ClassType) and ctx.VAR() else None
            return reduce(
                lambda acc, ele:
                acc + [
                    ConstDecl(ele, type, init) if ctx.VAL(
                    ) else VarDecl(ele, type, init)
                ],
                varList[:-1],
                []
            )
        elif(ctx.declarationWithAssign()):
            self.visit(ctx.declarationWithAssign())
            varList = self.decl_list
            exp = self.decl_exp_list[::-1]

            finalList = zip(varList, exp)
            self.decl_list = []
            self.decl_exp_list = []
            type = self.decl_type

            return reduce(
                lambda acc, ele:
                acc + [
                    ConstDecl(ele[0], type, ele[1]) if ctx.VAL(
                    ) else VarDecl(ele[0], type, ele[1])
                ],
                finalList,
                []
            )

    def visitDeclarationWithAssign(self, ctx: D96Parser.DeclarationWithAssignContext):
        self.decl_list.append(Id(ctx.ID().getText()))
        self.decl_exp_list.append(self.visit(ctx.exp()))
        if(ctx.declarationPair()):
            self.visit(ctx.declarationPair())
        return None

    def visitDeclarationPair(self, ctx: D96Parser.DeclarationPairContext):
        if(ctx.COMMA()):
            self.decl_list.append(Id(ctx.ID().getText()))
            self.decl_exp_list.append(self.visit(ctx.exp()))
            self.visit(ctx.declarationPair())
            return None
        elif(ctx.ASSIGN()):
            self.decl_type = self.visit(ctx.typeName())

    def visitDeclarationWithoutAssign(self, ctx: D96Parser.DeclarationWithoutAssignContext):
        varList = self.visit(ctx.varList()) # [Id, Id]
        typeName = [self.visit(ctx.typeName())]
        return varList + typeName

    def visitVarList(self, ctx: D96Parser.VarListContext):
        return [Id(id.getText()) for id in ctx.ID()]

    def visitAssignStmt(self, ctx: D96Parser.AssignStmtContext):
        return Assign(self.visit(ctx.assignLHS()), self.visit(ctx.exp()))

    def visitAssignLHS(self, ctx: D96Parser.AssignLHSContext):
        if(ctx.indexOperation()):
            return self.visit(ctx.indexOperation())
        else:
            return self.visit(ctx.scalar())

    def visitScalar(self, ctx: D96Parser.ScalarContext):
        if(ctx.DOT()):
            return FieldAccess(self.visit(ctx.exp()), Id(ctx.ID().getText()))
        elif(ctx.DOUBLECOLON()):
            return FieldAccess(Id(ctx.ID().getText()), Id(ctx.DOLLAR_ID().getText()))
        else:
            return Id(ctx.ID().getText())

    def visitIndexOperation(self, ctx: D96Parser.IndexOperationContext):
        # return ArrayCell(
        #     self.visit(ctx.indexHead()),
        #     [self.visit(exp) for exp in ctx.exp()]
        # )
        return self.visit(ctx.exp7())

    def visitIndexHead(self, ctx: D96Parser.IndexHeadContext):
        return self.visit(ctx.exp())

    def visitIfStmt(self, ctx: D96Parser.IfStmtContext):
        # If(expr: Expr , thenStmt: Stmt , elseStmt?: Stmt)
        # [(exp, if_block), (exp, if_block),...]
        if_stmt = [self.visit(body) for body in ctx.ifBody()]
        else_stmt = [self.visit(ctx.blockStmt())
                     ] if ctx.blockStmt() else None  # [else_block]
        # ((exp, if_block), else_block)
        last_pair = zip(
            [if_stmt[-1]], else_stmt) if ctx.blockStmt() else [if_stmt[-1]]
        # [(exp, if_block), (exp, if_block),..., ((exp, if_block), else_block)]
        final_list = if_stmt[0:-1] + list(last_pair)
        final_list = final_list[::-1]  # reverse list

        return reduce(lambda acc, ele:
                      If(ele[0], ele[1], acc),
                      final_list[1:],
                      If(final_list[0][0][0], final_list[0][0][1], final_list[0][1]) if ctx.blockStmt(
                      ) else If(final_list[0][0], final_list[0][1], None)
                      )

    def visitIfBody(self, ctx: D96Parser.IfBodyContext):
        return (self.visit(ctx.exp()), self.visit(ctx.blockStmt()))

    def visitForInStmt(self, ctx: D96Parser.ForInStmtContext):
        # For(id: Id , expr1: Expr , expr2: Expr, loop: Stmt, expr3?: Expr)
        id = self.visit(ctx.scalar())
        expr1 = self.visit(ctx.exp(0))
        expr2 = self.visit(ctx.exp(1))
        expr3 = self.visit(ctx.exp(2)) if ctx.BY() else IntLiteral(1)
        loop = self.visit(ctx.blockStmt())
        return For(id, expr1, expr2, loop, expr3)

    def visitBreakStmt(self, ctx: D96Parser.BreakStmtContext):
        return Break()

    def visitContinueStmt(self, ctx: D96Parser.ContinueStmtContext):
        return Continue()

    def visitReturnStmt(self, ctx: D96Parser.ReturnStmtContext):
        # Return(expr?: Expr)
        expr = self.visit(ctx.exp()) if ctx.exp() else None
        return Return(expr)

    def visitInstanceCall(self, ctx: D96Parser.InstanceCallContext):
        # CallStmt(obj: Expr , method: Id , param: List[Expr])
        obj = self.visit(ctx.exp())
        method = Id(ctx.ID().getText())
        param = self.visit(ctx.expList()) if ctx.expList() else []
        return CallStmt(obj, method, param)

    def visitStaticCall(self, ctx: D96Parser.StaticCallContext):
        # CallStmt(obj: Expr , method: Id , param: List[Expr])
        obj = Id(ctx.ID().getText())
        method = Id(ctx.DOLLAR_ID().getText())
        param = self.visit(ctx.expList()) if ctx.expList() else []
        return CallStmt(obj, method, param)

    def visitBlockStmt(self, ctx: D96Parser.BlockStmtContext):
        # Block(inst: List[Inst])
        inst = []
        for statement in ctx.stmt():
            stmt = self.visit(statement)
            if(isinstance(stmt, list)):
                inst += stmt
            else:
                inst.append(stmt)
        return Block(inst)

    def visitExp(self, ctx: D96Parser.ExpContext):
        if(ctx.STRADD()):
            return BinaryOp(
                ctx.STRADD().getText(),
                self.visit(ctx.exp(0)),
                self.visit(ctx.exp(1))
            )
        elif(ctx.STREQ()):
            return BinaryOp(
                ctx.STREQ().getText(),
                self.visit(ctx.exp(0)),
                self.visit(ctx.exp(1))
            )
        else:
            return self.visit(ctx.exp1())

    def visitExp1(self, ctx: D96Parser.Exp1Context):
        if(ctx.EQUAL()):
            return BinaryOp(
                ctx.EQUAL().getText(),
                self.visit(ctx.exp1(0)),
                self.visit(ctx.exp1(1))
            )
        elif(ctx.DIFF()):
            return BinaryOp(
                ctx.DIFF().getText(),
                self.visit(ctx.exp1(0)),
                self.visit(ctx.exp1(1))
            )
        elif(ctx.LT()):
            return BinaryOp(
                ctx.LT().getText(),
                self.visit(ctx.exp1(0)),
                self.visit(ctx.exp1(1))
            )
        elif(ctx.LTE()):
            return BinaryOp(
                ctx.LTE().getText(),
                self.visit(ctx.exp1(0)),
                self.visit(ctx.exp1(1))
            )
        elif(ctx.GT()):
            return BinaryOp(
                ctx.GT().getText(),
                self.visit(ctx.exp1(0)),
                self.visit(ctx.exp1(1))
            )
        elif(ctx.GTE()):
            return BinaryOp(
                ctx.GTE().getText(),
                self.visit(ctx.exp1(0)),
                self.visit(ctx.exp1(1))
            )
        else:
            return self.visit(ctx.exp2())

    def visitExp2(self, ctx: D96Parser.Exp2Context):
        if(ctx.AND()):
            return BinaryOp(
                ctx.AND().getText(),
                self.visit(ctx.exp2()),
                self.visit(ctx.exp3())
            )
        elif(ctx.OR()):
            return BinaryOp(
                ctx.OR().getText(),
                self.visit(ctx.exp2()),
                self.visit(ctx.exp3())
            )
        else:
            return self.visit(ctx.exp3())

    def visitExp3(self, ctx: D96Parser.Exp3Context):
        if(ctx.ADD()):
            return BinaryOp(
                ctx.ADD().getText(),
                self.visit(ctx.exp3()),
                self.visit(ctx.exp4())
            )
        elif(ctx.MINUS()):
            return BinaryOp(
                ctx.MINUS().getText(),
                self.visit(ctx.exp3()),
                self.visit(ctx.exp4())
            )
        else:
            return self.visit(ctx.exp4())

    def visitExp4(self, ctx: D96Parser.Exp4Context):
        if(ctx.MUL()):
            return BinaryOp(
                ctx.MUL().getText(),
                self.visit(ctx.exp4()),
                self.visit(ctx.exp5())
            )
        elif(ctx.DIV()):
            return BinaryOp(
                ctx.DIV().getText(),
                self.visit(ctx.exp4()),
                self.visit(ctx.exp5())
            )
        elif(ctx.MOD()):
            return BinaryOp(
                ctx.MOD().getText(),
                self.visit(ctx.exp4()),
                self.visit(ctx.exp5())
            )
        else:
            return self.visit(ctx.exp5())

    def visitExp5(self, ctx: D96Parser.Exp5Context):
        if(ctx.NOT()):
            return UnaryOp(
                ctx.NOT().getText(),
                self.visit(ctx.exp5())
            )
        else:
            return self.visit(ctx.exp6())

    def visitExp6(self, ctx: D96Parser.Exp6Context):
        if(ctx.MINUS()):
            return UnaryOp(
                ctx.MINUS().getText(),
                self.visit(ctx.exp6())
            )
        else:
            return self.visit(ctx.exp7())

    def visitExp7(self, ctx: D96Parser.Exp7Context):
        if(ctx.LS()):
            return ArrayCell(
                self.visit(ctx.exp7()),
                [self.visit(expr) for expr in ctx.exp()]
            )
        else:
            return self.visit(ctx.exp8())

    def visitExp8(self, ctx: D96Parser.Exp8Context):
        if(ctx.DOT()):
            if(ctx.LB()):
                return CallExpr(
                    self.visit(ctx.exp8()),
                    Id(ctx.ID().getText()),
                    self.visit(ctx.expList()) if ctx.expList() else []
                )
            else:
                return FieldAccess(
                    self.visit(ctx.exp8()),
                    Id(ctx.ID().getText())
                )
        else:
            return self.visit(ctx.exp9())

    def visitExp9(self, ctx: D96Parser.Exp9Context):
        if(ctx.DOUBLECOLON()):
            if(ctx.LB()):
                return CallExpr(
                    Id(ctx.ID().getText()),
                    Id(ctx.DOLLAR_ID().getText()),
                    self.visit(ctx.expList()) if ctx.expList() else []
                )
            else:
                return FieldAccess(
                    Id(ctx.ID().getText()),
                    Id(ctx.DOLLAR_ID().getText())
                )
        else:
            return self.visit(ctx.exp10())

    def visitExp10(self, ctx: D96Parser.Exp10Context):
        if(ctx.NEW()):
            return NewExpr(
                Id(ctx.ID().getText()),
                self.visit(ctx.expList()) if ctx.expList() else []
            )
        else:
            return self.visit(ctx.exp11())

    def visitExp11(self, ctx: D96Parser.Exp11Context):
        if(ctx.exp()):
            return self.visit(ctx.exp())
        else:
            return self.visit(ctx.operand())

    def visitExpList(self, ctx: D96Parser.ExpListContext):
        return [self.visit(expr) for expr in ctx.exp()]

    def visitOperand(self, ctx: D96Parser.OperandContext):
        if(ctx.ID()):
            return Id(ctx.ID().getText())
        elif(ctx.ZERO()):
            return IntLiteral(int(ctx.ZERO().getText(), 0))
        elif(ctx.intLit()):
            return IntLiteral(self.visit(ctx.intLit()))
        elif(ctx.FLOATLIT()):
            if ctx.getText()[:2] == ".e":
                return FloatLiteral(float(0))
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif(ctx.STRINGLIT()):
            return StringLiteral(str(ctx.STRINGLIT().getText()))
        elif(ctx.booleanLit()):
            return self.visit(ctx.booleanLit())
        elif(ctx.indexArray()):
            return self.visit(ctx.indexArray())
        elif(ctx.SELF()):
            return SelfLiteral()
        else:
            return NullLiteral()

    def visitIntLit(self, ctx: D96Parser.IntLitContext):
        if(ctx.DECINT()):
            return int(ctx.getChild(0).getText(), 10)
        elif(ctx.OCTINT()):
            return int(ctx.getChild(0).getText(), 8)
        elif(ctx.HEXINT()):
            return int(ctx.getChild(0).getText(), 16)
        else:
            return int(ctx.getChild(0).getText(), 2)

    def visitBooleanLit(self, ctx: D96Parser.BooleanLitContext):
        if(ctx.TRUE()):
            return BooleanLiteral(bool(ctx.TRUE().getText()))
        else:
            return BooleanLiteral(bool(ctx.FALSE().getText() == "True"))

    def visitIndexArray(self, ctx: D96Parser.IndexArrayContext):
        # ArrayLiteral(value: List[Literal])
        return ArrayLiteral(
            self.visit(ctx.arrayBody()) if ctx.arrayBody() else []
        )

    def visitArrayBody(self, ctx: D96Parser.ArrayBodyContext):
        return [self.visit(lit) for lit in ctx.arrayLit()]

    def visitArrayLit(self, ctx: D96Parser.ArrayLitContext):
        return self.visit(ctx.exp()) if ctx.exp() else self.visit(ctx.indexArray())
