# helper functions for shunting_yard
def negate_variable(var: str, neg: bool):
    if neg: return "!" + var
    else: return var
# end helper functions for shunting_yard

def shunting_yard(user_func: str):
    rpn = [] # reverse polish notation
    # rpn[0] holds everything left of '='

    found_equal_sign = False
    op_stack = []
    for i in range(len(user_func)):
        # all content on the left side of '=' should be in rpn[0]
        if user_func[i] == '=': found_equal_sign = True
        if not found_equal_sign:
            if user_func[i] == ' ': pass # ignore whitespace
            elif rpn: 
                rpn[0] += user_func[i]
            else: # create first element if it does't yet exist
                rpn.append(user_func[i])

        else: # shunting yard algorithm
            if user_func[i] == ' ': pass # ignore whitespace
            elif user_func[i] == '+':
                # 'and' operator has precedence over 'or' so we move 'or'
                # forward in our operator stack before the first instance
                # of 'and'
                op_stack.insert(op_stack.index("and"), "or")

            elif user_func[i].isalpha() and i < len(user_func)-1:
                # negation and the 'and' operator are handled here
                if user_func[i+1] == '\'':
                    # if user[i+1] == '\'' evaluates to true, negate_variable()
                    # returns "!user_func[i]"
                    rpn.append( negate_variable(user_func[i], True) )
                    # if '\'' is not the last character, skip '\'' character
                    if i+1 < len(user_func)-1: i += 1
                else:
                    rpn.append(user_func[i])

                if user_func[i+1].isalpha():
                    op_stack.append("and")

            else: # appending last variable
                if user_func[i].isalpha(): rpn.append(user_func[i])

    # pop all operators into our reverse polish notation
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
