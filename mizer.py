# gets variables from a passed function in the form F([variables]) = sum([terms])
def getVariables(function: str) -> list[str]:
    v_list = []
    # TODO: implement checks for variables
    for v in function:
        v_list.append(v)

    return v_list

# gets term subscripts from a passed function who's terms are in a list (see above function form)
def getTermSubscripts(function: str) -> list[int]:
    term_subs = []
    # TODO: implement checks for terms & subscripts
    for t in function:
        term_subs.append(int(t))

    return term_subs

# returns binary representaion of intergers passed from num_list
def getBinaryList(num_list: list[int], bits: int) -> list[str]:
    binary_list = []

    curr_binary_num = ""
    for n in num_list:
        # ignore "0b"
        curr_binary_num = bin(n)[2::]
        # preppend the appropriate # of '0's given bits
        binary_list.append('0'*(bits - len(curr_binary_num)) + curr_binary_num)


    return binary_list

# returns the appropriate minterm given a list of variables and the term subscript in binary
def getMinterm(var_list: list[str], binary_subscript: str) -> str:
    minterm = ""

    r_binary_num = binary_subscript[::-1]
    end_of_binary_num = False
    for i in range(len(var_list)):
        # ingore all characters after the 'b' in binary number string
        if not end_of_binary_num and r_binary_num[i] == 'b':
            end_of_binary_num = True
        # apppend appropriate true or complimented term
        if not end_of_binary_num and r_binary_num[i] == '1':
            minterm += var_list[i]
        else:
            minterm += var_list[i] + '\''

    return minterm

# returns the standard representation of a sum of products function given its variables and minterm subscripts
def getStandardRepresentation(var_list: list[str], subscript_list: list[int]) -> str:
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
    binary_list = getBinaryList(subscript_list, variable_count)
    for i in range(len(subscript_list)):
        function += getMinterm(var_list, binary_list[i])

        if i != len(subscript_list)-1:
            function += ' + '

    return function
