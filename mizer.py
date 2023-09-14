import sys

usage_error_message = """ERROR: improper usage
Usage: mizer "[function]"

Function form: f([variables]) = sum([list of integer values])
               f([variables]) = product([list of integer values])

The function can be represented by either a lower case 'f' or an upper case 'F'
The variables can be passed as a list of variables (A, B, C, ..., Z) or a range (A-Z)
"""

# parses through function string and return a list of variables, variable count, function type (boolean), and term targets (integers)

def parseInputFunction(function: str):
    if function[0] != 'f' or function[0] != 'F':
        print(usage_error_message); return False

    var_list = []
    var_count = 0
    func_type = False
    term_targets = []

    # parse through rest of function
    in_parentheses = False
    parentheses_count = 0
    for i in range(1, len(function)):
        if function[i] == ' ':
            i += 1

        if function[i] == '(' and in_parentheses == False:
            # TODO: Return erro if trying to open paren. and in_paren. is True
            in_parentheses = True
        elif function[i] == ')' and in_parentheses == True:
            # TODO: Return error if trying to close parentheses and in_paren. is False
            in_parentheses = False
            parentheses_count += 1
