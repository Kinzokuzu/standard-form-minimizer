class BooleanFunction:
    outputs = []
    inputs = []
    _rpn = [] # reverse polish notation

    def __init__(self) -> None:
        pass

# end class BooleanFunction

def convert_to_boolean_function(user_function: str) -> BooleanFunction:
    user_function.replace(" ", "") # remove all white space
    boolean_function = BooleanFunction()

    left_side = True
    in_parenthesis = False
    variable_list_created = False
    for i in range(len(user_function)):
        # left side of function should only contain outputs and variables
        if left_side:
            match user_function[i]:
                case '(':
                    in_parenthesis = True
                case ')':
                    in_parenthesis = False
                case '=':
                    left_side = False
                case _: # handle outputs and inputs
                    if in_parenthesis:
                        boolean_function.inputs.append(user_function[i])
                        variable_list_created = True
                    else:
                        boolean_function.outputs.append(user_function[i])
        # right side of function can contain variables, operators, or minterms
        else:
            if user_function[i] == 'm': # minterms
                # TODO: handle minterm
                pass 
            elif user_function[i] == '+': # OR operator
                boolean_function._rpn.append("or")
            else: # variables, negation, and AND operator
                # TODO: continue here 
                pass

    return boolean_function
