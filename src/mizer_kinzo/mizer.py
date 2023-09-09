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

# TODO: implement this method
def getStandardFunc(tgt_func: list[str]) -> list[str]:
    std_func = []
    # for every term in tgt_func, create minterm/maxterm
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
std_func = getStandardFunc(tgt_func)

# simplify std_func -> simp_func  * implement method

# return std_func & simp_func
print(std_func)
# print(simp_func)
