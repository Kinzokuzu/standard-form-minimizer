import boolfunc as bf
import cbuilder as cb
import quinemcclusky as qm
import shuntingyard as sh # sy was too similar to sys
import ttable as tt

import sys

usage_message = "usage: vcb -[options] [function]"

def main():
    if len(sys.argv) < 2:
        print(usage_message)
        sys.exit()

    # handle options
    # call quinemcclusky
    # create boolfunc object
    # call shuntingyard
    # call cbuilder
    # call ttable

if __name__ == "__main__":
    main()
