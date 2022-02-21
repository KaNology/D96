from this import d
from xmlrpc.client import Boolean
from D96Visitor import D96Visitor
from D96Parser import D96Parser
from AST import *
from main.d96.utils.AST import ArrayCell, Assign, Block, BooleanLiteral, CallExpr, FieldAccess, FloatLiteral, Id, IntLiteral, MethodDecl, NewExpr, NullLiteral, SelfLiteral, StringLiteral, VarDecl


class ASTGeneration(D96Visitor):
    def visitProgram(self, ctx: D96Parser.ProgramContext):
        return Program([self.visit(decl) for decl in ctx.classDeclaration()])

    def visitClassDeclaration(self, ctx: D96Parser.ClassDeclarationContext):
        class_name = Id(ctx.ID(0).getText())
        class_body = self.visit(ctx.classBody())
        class_parent = Id(ctx.ID(1).getText()) if ctx.ID(1) else ""

        return ClassDecl(
            class_name, class_body, class_parent
        )

    def visitClassBody(self, ctx: D96Parser.ClassBodyContext):
        if (ctx.attrDeclaration()):
            attrDecl = [self.visit(decl) for decl in ctx.attrDeclaration()]
            return [attr for decl in attrDecl for attr in decl]
        else:
            return [self.visit(decl) for decl in ctx.methodDeclaration()]

    def visitAttrDeclaration(self, ctx: D96Parser.AttrDeclarationContext):
        attrList = self.visit(ctx.attrList()) # type and id
        type = self.visit(ctx.typeName()) # literal type
        exp = [self.visit(exp) for exp in ctx.exp()] # exp
        attrDecl = []

        for i in range(len(attrList)):
            attrDecl.append(
                AttributeDecl(
                    attrList[i][0], # type
                    ConstDecl(attrList[i][1], type, exp[i]) if ctx.VAL() else 
                    VarDecl(attrList[i][1], type, exp[i])
                )
            )

        return attrDecl

    def visitAttrList(self, ctx: D96Parser.AttrListContext):
        return [self.visit(id) for id in ctx.identifier()]

    def visitIdentifier(self, ctx: D96Parser.IdentifierContext):
        if(ctx.ID()):
            return (Instance(), Id(ctx.ID().getText()))
        else:
            return (Static(), Id(ctx.DOLLAR_ID().getText()))

    def visitTypeName(self, ctx: D96Parser.TypeNameContext):
        if(ctx.primitiveType()):
            return self.visit(ctx.primitiveType())
        elif(ctx.arrayType()):
            return self.visit(ctx.arrayType())
        else:
            return self.visit(ctx.classType())
    
    def visitMethodDeclaration(self, ctx: D96Parser.MethodDeclarationContext):
        # MethodDecl(kind: SIKind , name: Id , param: List[VarDecl] , body: Block)
        method = self.visit(ctx.identifier()) # method type and method ID
        param = self.visit(ctx.paraList()) if ctx.paraList() else []
        block = self.visit(ctx.blockStmt())
        return MethodDecl(method[0], method[1], param, block)

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
        return [Id(id) for id in ctx.ID()]

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
            int(ctx.INTLIT().getText()),
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
        else:
            return self.visit(ctx.staticCall())

    def visitDeclarationStmt(self, ctx: D96Parser.DeclarationStmtContext):
        varList = self.visit(ctx.varList()) # id
        type = self.visit(ctx.typeName()) # literal type
        exp = [self.visit(exp) for exp in ctx.exp()] # exp
        attrDecl = []

        for i in range(len(attrList)):
            attrDecl.append(
                ConstDecl(attrList[i], type, exp[i]) if ctx.VAL() else VarDecl(attrList[i], type, exp[i])
            )

        return attrDecl

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
        return ArrayCell(
            Id(ctx.ID().getText()),
            [self.visit(exp) for exp in ctx.exp()]
            )

    # if_stmt: IF LP exp RP LCB stmt* RCB elif_part* else_part?;

    # elif_part: ELSEIF LP exp RP LCB stmt* RCB;

    # else_part: ELSE LCB stmt* RCB;

    # def visitIf_stmt(self, ctx: D95Parser.If_stmtContext):
    #     exp1 = self.visit(ctx.exp())
    #     stmt1 = [self.visit(stmt) for stmt in ctx.stmt()]
    #     if ctx.elif_part() and ctx.else_part():
    #         elseif_part = list(reduce(lambda x,y: x+y, [self.visit(part) for part in ctx.elif_part()], []))
    #         return If([(exp1,stmt1)] + elseif_part, self.visit(ctx.else_part()))
    #     elif ctx.elif_part():
    #         elseif_part = list(reduce(lambda x, y: x + y, [self.visit(part) for part in ctx.elif_part()], []))
    #         return If([(exp1,stmt1)] + elseif_part, [])
    #     elif ctx.else_part():
    #         return If([(exp1,stmt1)], self.visit(ctx.else_part()))
    #     return If([(exp1,stmt1)], [])

    # def visitElif_part(self, ctx: D95Parser.Elif_partContext):
    #     exp = self.visit(ctx.exp())
    #     stmts = [self.visit(stmt) for stmt in ctx.stmt()]
    #     return [(exp, stmts)]

    # def visitElse_part(self, ctx: D95Parser.Else_partContext):
    #     return [self.visit(stmt) for stmt in ctx.stmt()]

    def visitIfStmt(self, ctx: D96Parser.IfStmtContext):
        # If(expr: Expr , thenStmt: Stmt , elseStmt?: Stmt)
        return None

    def visitIfBody(self, ctx: D96Parser.IfBodyContext):
        return None

    def visitForInStmt(self, ctx: D96Parser.ForInStmtContext):
        return None

    def visitBreakStmt(self, ctx: D96Parser.BreakStmtContext):
        return None

    def visitContinueStmt(self, ctx: D96Parser.ContinueStmtContext):
        return None

    def visitReturnStmt(self, ctx: D96Parser.ReturnStmtContext):
        return None

    def visitInstanceCall(self, ctx: D96Parser.InstanceCallContext):
        return None

    def visitStaticCall(self, ctx: D96Parser.StaticCallContext):
        return None

    def visitBlockStmt(self, ctx: D96Parser.BlockStmtContext):
        decl_list = [self.visit(decl) for decl in ctx.declarationStmt()]
        stmt = [self.visit(stmt) for stmt in ctx.stmt()]
        return Block(decl_list, stmt)

    def visitExp(self, ctx:D96Parser.ExpContext):
        if(ctx.STRADD()):
            return BinaryOP(
                ctx.STRADD().getText(),
                self.visit(ctx.exp(0)),
                self.visit(ctx.exp(1))
            )
        elif(ctx.STREQ()):
            return BinaryOP(
                ctx.STREQ().getText(),
                self.visit(ctx.exp(0)),
                self.visit(ctx.exp(1))
            )
        else:
            return self.visit(ctx.exp1())

    def visitExp1(self, ctx: D96Parser.Exp1Context):
        if(ctx.EQUAL()):
            return BinaryOP(
                ctx.EQUAL().getText(),
                self.visit(ctx.exp1(0)),
                self.visit(ctx.exp1(1))
            )
        elif(ctx.DIFF()):
            return BinaryOP(
                ctx.DIFF().getText(),
                self.visit(ctx.exp1(0)),
                self.visit(ctx.exp1(1))
            )
        elif(ctx.LT()):
            return BinaryOP(
                ctx.LT().getText(),
                self.visit(ctx.exp1(0)),
                self.visit(ctx.exp1(1))
            )
        elif(ctx.LTE()):
            return BinaryOP(
                ctx.LTE().getText(),
                self.visit(ctx.exp1(0)),
                self.visit(ctx.exp1(1))
            )
        elif(ctx.GT()):
            return BinaryOP(
                ctx.GT().getText(),
                self.visit(ctx.exp1(0)),
                self.visit(ctx.exp1(1))
            )
        elif(ctx.GTE()):
            return BinaryOP(
                ctx.GTE().getText(),
                self.visit(ctx.exp1(0)),
                self.visit(ctx.exp1(1))
            )
        else:
            return self.visit(ctx.exp2())

    def visitExp2(self, ctx: D96Parser.Exp2Context):
        if(ctx.AND()):
            return BinaryOP(
                ctx.AND().getText(),
                self.visit(ctx.exp2()),
                self.visit(ctx.exp3())
            )
        elif(ctx.OR()):
            return BinaryOP(
                ctx.OR().getText(),
                self.visit(ctx.exp2()),
                self.visit(ctx.exp3())
            )
        else:
            return self.visit(ctx.exp3())
    
    def visitExp3(self, ctx: D96Parser.Exp3Context):
        if(ctx.ADD()):
            return BinaryOP(
                ctx.ADD().getText(),
                self.visit(ctx.exp3()),
                self.visit(ctx.exp4())
            )
        elif(ctx.MINUS()):
            return BinaryOP(
                ctx.MINUS().getText(),
                self.visit(ctx.exp3()),
                self.visit(ctx.exp4())
            )
        else:
            return self.visit(ctx.exp4())
    
    def visitExp4(self, ctx: D96Parser.Exp4Context):
        if(ctx.MUL()):
            return BinaryOP(
                ctx.MUL().getText(),
                self.visit(ctx.exp4()),
                self.visit(ctx.exp5())
            )
        elif(ctx.DIV()):
            return BinaryOP(
                ctx.DIV().getText(),
                self.visit(ctx.exp4()),
                self.visit(ctx.exp5())
            )
        elif(ctx.MOD()):
            return BinaryOP(
                ctx.MOD().getText(),
                self.visit(ctx.exp4()),
                self.visit(ctx.exp5())
            )
        else:
            return self.visit(ctx.exp5())
    
    def visitExp5(self, ctx: D96Parser.Exp5Context):
        if(ctx.NOT()):
            return UnaryOP(
                ctx.NOT().getText(),
                self.visit(ctx.exp5())
            )
        else:
            return self.visit(ctx.exp6())

    def visitExp6(self, ctx: D96Parser.Exp6Context):
        if(ctx.MINUS()):
            return UnaryOP(
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
                    ctx.ID().getText(),
                    Id(ctx.DOLLAR_ID().getText()),
                    self.visit(ctx.expList()) if ctx.expList() else [] 
                )
            else:
                return FieldAccess(
                    ctx.ID().getText(),
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
            return IntLiteral(int(ctx.ZERO().getText()))
        elif(ctx.INTLIT()):
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif(ctx.FLOATLIT()):
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

    def visitBooleanLit(self, ctx: D96Parser.BooleanLitContext):
        if(ctx.TRUE()):
            return BooleanLiteral(bool(ctx.TRUE().getText()))
        else:
            return BooleanLiteral(bool(ctx.FALSE().getText()))
