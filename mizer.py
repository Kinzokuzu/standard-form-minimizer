import sys

def getVariables(var_str: str):
    var_list = []
    for var in var_str:
        var_list.append(var)

    var_count = len(var_list)

    return var_list, var_count

# TODO: - implement maxterms
#       - fix so that last subscript appends to term_subs without a ',' being needed
def getTermSubscripts(tgt_func: str):
    term_subs = []
   
    curr_term = ""
    for i in range(len(tgt_func)):
        if tgt_func[i] == ',':
            term_subs.append(int(curr_term))
            curr_term = ""
        else:
            curr_term += tgt_func[i]

    return term_subs

def integerToBinaryString(num: int, bit_count: int):
    binary_str = ""
    while num > 0:
        binary_str += str(num % 2)
        num = num // 2
    
    append_count = bit_count - len(binary_str)
    binary_str += '0' * append_count

    return binary_str[::-1]

# TODO: implement maxterms
def getStandardRepresentation(var_list: list[str], tgt_func: str):
    var_count = len(var_list)
    term_subscripts = getTermSubscripts(tgt_func)
    std_rep = []

    # for every term subscript get minterms
    for term in term_subscripts:
        curr_product = ""
        binary_representation = integerToBinaryString(term, var_count)

        for i in range(var_count):
            # get compliments for all terms that evaluate to 0
            if binary_representation[i] == '0':
                curr_product += var_list[i] + '\''
            else:
                curr_product += var_list[i]
        # append current product of inputs to standard rep. function
        std_rep.append(curr_product)

    return std_rep

# TODO: implement maxterms
def printFunction(func: list[str]):
    # TODO: fix '+' being printed after the last term
    for term in func:
        print(term, "+", end=" ")

    print("")
