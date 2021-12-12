import tokens as T


class PrintVisitor:
    def visit(self, token):
        if isinstance(token, T.Brace):
            if token.type == 'L':
                print('(')
            else:
                print(')')
        if isinstance(token, T.Op):
            print(token.op)
        if isinstance(token, T.NumberToken):
            print(token.n)
