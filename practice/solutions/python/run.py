#!/bin/python3

# {{{ Imports

import os
import copy

# }}}
# {{{ Constants

TESTS_DIR = "./local/tests/"
OUTPUT_DIR = "./local/output/"
MEMO = {}

# }}}
# {{{ Functions

# {{{ slicesCombination


def slicesCombination(tar, slices):
    """See practice problem speccification."""

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
# {{{ slicesCombinationRecursive

def slicesCombinationRecursive(tar, slices, ix, comb_sum, comb):
    """See practice problem speccification."""

    # Base case; return
    if ((ix + 1 == len(slices)) or (comb_sum + slices[ix] > tar)):
        return (comb_sum, comb)

    ix += 1

    # Don't add
    exclude_sum, exclude_comb = memoize(tar, slices,
            copy.deepcopy(ix), copy.deepcopy(comb_sum), copy.deepcopy(comb))

    # Do add
    comb_sum += slices[ix]
    comb.append(ix)

    include_sum, include_comb = memoize(tar, slices,
            copy.deepcopy(ix), copy.deepcopy(comb_sum), copy.deepcopy(comb))

    if include_sum <= tar:
        return minDiff(tar, include_sum, include_comb, exclude_sum, exclude_comb)
    else:
        return (exclude_sum, exclude_comb)


# }}}
# {{{ memoize


def memoize(*args):

    k = ""
    for arg in args:
        k += str(arg)

    if k in MEMO:
        return MEMO[k]
    return slicesCombinationRecursive(*args)

# }}}
# {{{ minDiff


def minDiff(tar, include_sum, include_comb, exclude_sum, exclude_comb):

    if (tar - include_sum) < (tar - exclude_sum):
        return (include_sum, include_comb)
    else:
        return (exclude_sum, exclude_comb)

# }}}
# {{{ formatOutput


def formatOutput(combination):
    """Formats the output of the combination to hashcode specs."""

    combination = combination[1]
    return (str(len(combination)) + "\n" + str(combination)[1:-1]).replace(",", "")

# }}}
# {{{ runTests


def runTests(tests_dir):
    """Runs all test files in the given directory."""

    for test_case in os.listdir(TESTS_DIR):
        try:
            print()
            print("Running test: " + str(test_case))

            with open(TESTS_DIR + test_case, "r") as f:
                target, num_pizzas = list(map(int, f.readline().split(" ")))
                slices = list(map(int, f.readline().split(" ")))

            # result = formatOutput(slicesCombination(target, slices))
            ix = -1
            comb_sum = 0
            comb = []
            result = formatOutput(slicesCombinationRecursive(target, slices, ix, comb_sum, comb))

            path_output = OUTPUT_DIR + "output_" + test_case[:test_case.rfind(".")] + ".txt"
            os.makedirs(os.path.dirname(path_output), exist_ok=True)
            with open(path_output, "w") as f:
                f.write(result)
                print("Result written to: " + str(path_output))
        except KeyboardInterrupt:
            print("Test cancelled.")



# }}}

# }}}

if __name__ == '__main__':
    runTests(TESTS_DIR)

"""

We know the following:

    TODO

"""
