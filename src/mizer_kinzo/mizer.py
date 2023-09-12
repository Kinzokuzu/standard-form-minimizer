#!/usr/bin/env python3

import sys

def getTargetFunc(canon_func: str) -> list[str]:
    tgt_func = []
    # parse canon_func
    for i in range(len(canon_func)):
        if canon_func[i] == 'm' or canon_func[i] == 'M':
            tgt_func.append(canon_func[i] + canon_func[i+1])
            i += 1

    return tgt_func

def decimalToBinary(decimal_int: int, var_cout: int) -> list[int]:
    binary_func = []

    for i in range(var_cout):
        binary_func.append(decimal_int % 2)
        decimal_int = decimal_int // 2

    return binary_func[::-1]

def getStandardFunc(tgt_func: list[str], num_vars) -> list[str]:
    binary_func = []
    std_func = []

    # give appropriate binary representation of minterms
    for term in tgt_func:
        if term[0] == 'm':
            # take minterm subscript and convert it to a binary list representation
            binary_func.append(decimalToBinary(int(term[1]), num_vars))

    # using binary representation, create standard representation
    for binary_num in binary_func:
        std_term = ""
        for i in range(num_vars):
            if binary_num[i] == 0:
                std_term += var_list[i].upper()
            else:
                std_term += var_list[i]

        std_func.append(std_term)

    return std_func

# TODO: implement this method
"""
def simplifyStd(std_func: list[str]) -> list[str]:
    simp_func = []
    return simp_func
"""

if len(sys.argv) != 3:
    print("Arg count = ", len(sys.argv), " Should = 3", sep="")
    sys.exit()

# get var_list
var_list = list(sys.argv[1])

# get tgt_func -> need to format  * implement method 
tgt_func = getTargetFunc(sys.argv[2])

# create std_func                 * implement method
std_func = getStandardFunc(tgt_func, len(var_list))

# simplify std_func -> simp_func  * implement method

# return std_func & simp_func
print(std_func)
# print(simp_func)
