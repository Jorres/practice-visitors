def isHignerPriority(op1, op2):
    return ((op1.op in '/*') and (op2.op in '+-')) or ((op1.op in '+-') and (op2.op in '+-'))
