# helper functions for shunting_yard
def negate_variable(var: str, neg: bool):
    if neg: return "!" + var
    else: return var
# end helper functions for shunting_yard

# TODO: fix operator behavior.  Look at test_shunting_yard_hard
def shunting_yard(rhs: str):
    rpn = []        # reverse polish notation      
    op_stack = []   # operator stack

    negate_var = False

    for i in range(len(rhs)):
        if rhs[i] == ' ': # ignore whitespace
            pass
        elif rhs[i] == '+': # 'or' operator
            op_stack.append('or')
        elif rhs[i] == '!': # negation with '!'
            negate_var = True
        else:
            # current token is a variable
            if rhs[i].isalpha():
                # look for negation with apostrophe
                if i+1 < len(rhs) and rhs[i+1] == '\'':
                    negate_var = True
                # look for 'and' operations between two variables
                elif i+1 < len(rhs) and rhs[i+1].isalpha():
                    op_stack.append("and")

                # negate_variable handles proper true or negated variables
                rpn.append(negate_variable(rhs[i], negate_var))

    # empty operator stack into rpn
    while op_stack:
        rpn.append(op_stack.pop())

    return rpn


def get_inputs_outputs(lhs: str):
    inputs = []
    outputs = []

    in_parentheses = False

    for token in lhs:
        match token:
            case ' ': # ignore whitespace
                pass
            case ',': # ignore delimeters
                pass
            case '(': # entering parentheses
                in_parentheses = True
            case ')': # exiting parentheses
                in_parentheses = False
            case _:
                if in_parentheses: # handle inputs (variables)
                    inputs.append(token)
                else: # handle outputs (function name)
                    outputs.append(token) 
    
    return inputs, outputs
