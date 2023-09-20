import sys

def getVariables(function: str) -> list[str]:
    v_list = []
    # TODO: implement checks for variables
    for v in function:
        v_list.append(v)

    return v_list

def getTermSubscripts(function: str) -> list[int]:
    term_subs = []
    # TODO: implement checks for terms & subscripts
    for t in function:
        term_subs.append(int(t))

    return term_subs

def getBinaryList(num_list: list[int]) -> list[str]:
    binary_list = []

    for n in num_list:
        binary_list.append(bin(n))

    return binary_list

def getMinterm(var_list: list[str], binary_subscript: str) -> str:
    minterm = ""

    r_binary_num= binary_subscript[::-1]
    end_of_binary_num = False
    for i in range(len(var_list)):
        if r_binary_num[i] == 'b': end_of_binary_num = True

        if not end_of_binary_num and r_binary_num[i] == '0':
            minterm += var_list[i] + '\''
        else:
            minterm += var_list[i]

    return minterm

def getStandardRepresentation(var_list, subscript_list) -> str:
    variable_count = len(var_list)
    function = "F("

    # append variables
    for i in range(variable_count):
        function += var_list[i]
        # close parentheses
        if i == variable_count-1:
            function += ')'
        else:
            function += ','

    # append '='
    function += " = "

    # append terms

    return function
