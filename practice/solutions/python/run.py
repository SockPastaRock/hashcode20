#!/bin/python3

# {{{ Imports

import os

# }}}
# {{{ Constants

TESTS_DIR = "./tests/"

# }}}
# {{{ Functions

# {{{ slicesCombination


def slicesCombination(tar, slices):
    """Docstring for max_slices"""

    slice_sums = [0]
    combinations = [[]]

    for ix_slice, slice in enumerate(slices):
        tmp_sums = []
        tmp_combs = []
        for ix_sum, slice_sum in enumerate(slice_sums):
            tmp_sums.append(slice_sum + slice)
            tmp_combs.append(combinations[ix_sum] + [ix_slice])

        slice_sums += tmp_sums
        combinations += tmp_combs

    min_diff = tar
    min_diff_ix = 0
    for ix, slice_sum in enumerate(slice_sums):
        diff = tar - slice_sum
        if diff == 0:
            return combinations[ix]
        if diff > 0:
            if diff < min_diff:
                min_diff = diff
                min_diff_ix = ix
    return combinations[min_diff_ix]

# }}}

# }}}

if __name__ == '__main__':
    for test_case in os.listdir(TESTS_DIR):
        with open(TESTS_DIR + test_case, "r") as f:
            target, num_pizzas = list(map(int, f.readline().split(" ")))
            slices = list(map(int, f.readline().split(" ")))

        result = slicesCombination(target, slices)

        print()
        print(result)

"""

We know the following:

    TODO

"""
