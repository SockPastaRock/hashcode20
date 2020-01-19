#!/bin/python3

# {{{ Imports

import os

# }}}
# {{{ Constants

DATA_DIR = "./data/"

# }}}
# {{{ Functions

# {{{ maxSlices


def maxSlices():
    """Docstring for max_slices"""

    raise NotImplementedError

# }}}

# }}}

if __name__ == '__main__':
    for test_case in os.listdir(DATA_DIR):
        with open(DATA_DIR + test_case, "r") as f:
            n = int(f.readline())

        result = maxSlices()

"""

We know the following:

    TODO

"""
