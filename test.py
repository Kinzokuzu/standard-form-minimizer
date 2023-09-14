import mizer

import sys, os

# disable
def disablePrint():
    sys.stdout = open(os.devnull, 'w')

# restore
def enablePrint():
    sys.stdout = sys.__stdout__

def parseInputFunction_test1():
    test_str = "F,=,A,1,m,M,-,()" 

    disablePrint()
    test_result = mizer.parseInputFunction(test_str)
    enablePrint()

    print("parseInputFucntion_test1:", test_result)

parseInputFunction_test1()
