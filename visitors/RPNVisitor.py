import tokens as T
import helpers as H
import visitors.printVisitor


# TODO this code is fully written yet undebugged
# Also, write the third visitor - the calculating one

class RPNVisitor:
    def __init__(self):
        self.opstack = []
        self.outstack = []

    def visit(self, token):
        if isinstance(token, T.Brace):
            if token.type == 'L':
                self.opstack.append(token)
            else:
                while True:
                    if len(self.opstack) == 0:
                        assert False, 'Mismatched parentheses'
                    top_elem = self.opstack[-1]
                    if isinstance(top_elem, T.Brace) and top_elem.type == 'L':
                        break
                    self.outstack.append(top_elem)
                    self.opstack.pop()
                self.opstack.pop()
        elif isinstance(token, T.Op):
            while True:
                if len(self.opstack) == 0:
                    break
                top_elem = self.opstack[-1]

                if isinstance(top_elem, T.Op) and H.isHignerPriority(top_elem, token):
                    self.outstack.append(top_elem)
                    self.opstack.pop()
                else:
                    break
            self.opstack.append(token)
        elif isinstance(token, T.NumberToken):
            self.outstack.append(token)
        else:
            assert False, 'Unexpected token type'

    def getProcessedTokens(self):
        while len(self.opstack) > 0:
            op = self.opstack.pop()
            self.outstack.append(op)
        return self.outstack
