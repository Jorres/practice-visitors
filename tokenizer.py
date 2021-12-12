import tokens as T
import copy


class Tokenizer:
    def __init__(self):
        self.state = Start()
        self.tokens = []

    def tokenize(self, s):
        for smb in s:
            self.state = self.state.accept(self, smb)
        self.state = End()
        return self.tokens


class Start:
    def accept(self, tokenizer, smb):
        if smb == ' ':
            return self
        smbToToken = {
            '(': T.Brace('L'),
            ')': T.Brace('R'),
            '+': T.Op('+'),
            '-': T.Op('-'),
            '/': T.Op('/'),
            '*': T.Op('*')
        }
        singleTokens = '()+-/*'
        if smb in singleTokens:
            tokenizer.tokens.append(copy.deepcopy(smbToToken[smb]))
            return self
        if smb >= '0' and smb <= '9':
            newState = Number()
            newState.accept(tokenizer, smb)
            return newState

        return Error()


class Number:
    def __init__(self):
        self.curNum = 0

    def accept(self, tokenizer, smb):
        if smb >= '0' and smb <= '9':
            self.curNum *= 10
            self.curNum += int(smb)
            return self
        else:
            tokenizer.tokens.append(T.NumberToken(self.curNum))
            newState = Start()
            newState.accept(tokenizer, smb)
            return newState


class Error:
    def accept(self, tokenizer, smb):
        return self


class End:
    def accept(self, tokenizer, smb):
        return self
