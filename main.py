import tokenizer 
import visitors.printVisitor as PV
import visitors.RPNVisitor as RPNV
import visitors.calcVisitor as CV


def main():
    f = open('./input.txt')
    line = f.readline().strip() + ' '
    f.close()
    print("Given input:", line)
    print('-----------')

    t = tokenizer.Tokenizer()
    tokens = t.tokenize(line)

    print('Tokens before transformation:')
    pv = PV.PrintVisitor()
    for token in tokens:
        token.accept(pv)

    print('-----------')
    print('Processing tokens...')
    rpnv = RPNV.RPNVisitor()
    for token in tokens:
        token.accept(rpnv)
    tokens = rpnv.getProcessedTokens()

    print('-----------')
    print('Tokens after transformation')
    pv = PV.PrintVisitor()
    for token in tokens:
        token.accept(pv)

    print('-----------')
    calcVisitor = CV.CalcVisitor()
    for token in tokens:
        token.accept(calcVisitor)
    print('Resulting value:', calcVisitor.getResult())


if __name__ == "__main__":
    main()
