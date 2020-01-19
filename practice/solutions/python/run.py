#!/bin/python3

# {{{ Imports

import os

# }}}
# {{{ Constants

TESTS_DIR = "./tests/"

# }}}
# {{{ Functions

# {{{ maxSlices


def maxSlices(n, m):
    """Docstring for max_slices"""

    print()
    print(n)
    print(m)

# }}}

# }}}

if __name__ == '__main__':
    for test_case in os.listdir(TESTS_DIR):
        with open(TESTS_DIR + test_case, "r") as f:
            n = list(map(int, f.readline().split(" ")))
            m = list(map(int, f.readline().split(" ")))

        result = maxSlices(n, m)

"""

We know the following:

    TODO

"""
