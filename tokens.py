class Brace:
    def __init__(self, type):
        self.type = type

    def accept(self, visitor):
        visitor.visit(self)


class Op:
    def __init__(self, op):
        self.op = op

    def accept(self, visitor):
        visitor.visit(self)


class NumberToken:
    def __init__(self, n):
        self.n = n

    def accept(self, visitor):
        visitor.visit(self)
