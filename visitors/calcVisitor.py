import tokens as T


# This class does not do error processing 
# because I assume I only call this on tokens 
# I got from RPNVisitor, who does all the error 
# processing.
class CalcVisitor:
    def __init__(self):
        self.argstack = []

    def visit(self, token):
        if isinstance(token, T.Op):
            op = token
            arg_1 = self.argstack.pop()
            arg_2 = self.argstack.pop()
            print(arg_1, arg_2)
            if op.op == '+':
                self.argstack.append(arg_1 + arg_2)
            elif op.op == '-':
                self.argstack.append(arg_2 - arg_1)
            elif op.op == '*':
                self.argstack.append(arg_1 * arg_2)
            elif op.op == '/':
                # Tricky place, don't mess up the order!
                # Make sure you pop them out of your 
                # stack in the right order.
                self.argstack.append(arg_2 / arg_1)
            else:
                assert False, 'No operations except +-/* are expected!'
        if isinstance(token, T.NumberToken):
            self.argstack.append(token.n)

    def getResult(self):
        return self.argstack[-1]

