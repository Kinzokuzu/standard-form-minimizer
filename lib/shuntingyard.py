
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
