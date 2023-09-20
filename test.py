#!/usr/bin/env python3

import functionTests as ft
import sys

if len(sys.argv) > 1:
    if sys.argv[1] == "all":
        ft.test_getVariables()
        ft.test_getTermSubscripts()
        ft.test_getBinaryList()
        ft.test_getMinterm()
        ft.test_getStandardRepresentation()

print("TESTING COMPLETE")
