import sys

def getVariables(var_str: str):
    var_list = []
    for var in var_str:
        var_list.append(var)

    var_count = len(var_list)

    return var_list, var_count

# TODO: implement maxterms
def getTermSubscripts(tgt_func: str):
    term_subs = []
    for term in tgt_func:
        term_subs.append(int(term))

    return term_subs

def integerToBinaryString(num: int, bit_count: int):
    binary_str = ""
    while num > 0:
        binary_str += str(num % 2)
        num = num // 2
    
    append_count = bit_count - len(binary_str)
    binary_str += '0' * append_count

    return binary_str[::-1]

# TODO: finish implementation
def getStandardRepresentation(var_list: list[str], tgt_func: str):
    var_count = len(var_list)
    term_subscripts = getTermSubscripts(tgt_func)
    std_rep = []

    # for every term subscript get minterm/maxterm
