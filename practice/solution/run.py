#!/usr/bin/python3

# {{{ Imports

import os

# }}}
# {{{ Constants

TESTS_DIR = "./local/tests/"
OUTPUT_DIR = "./local/output/"

# }}}
# {{{ Functions

# {{{ main


def main():

    runTests(TESTS_DIR, OUTPUT_DIR)

# }}}
# {{{ runTests


def runTests(tests_dir, output_dir):
    """Runs all test files in the given directory."""

    for test_case in os.listdir(tests_dir):
        print()
        print("Running test: " + str(test_case))

        with open(tests_dir + test_case, "r") as f:
            tar, n = list(map(int, f.readline().split(" ")))
            arr = list(map(int, f.readline().split(" ")))

        writeOutput(maxCombSum(tar, arr), test_case, output_dir)

# }}}
# {{{ writeOutput


def writeOutput(result, fname, output_dir):
    """Writes output file as hashcode question specifies"""

    s = str(len(result)) + "\n" + str(result).replace(",", "")[1:-1]
    fname = fname[:fname.rfind(".")] + ".txt"
    os.makedirs(output_dir, exist_ok=True)
    with open(output_dir + fname, "w") as f:
        f.write(s)

    print("output written to: " + output_dir + fname)

# }}}
# {{{ maxCombSum


def maxCombSum(tar, arr):

    max_sum = 0
    max_comb = []

    local_sum = 0
    local_comb = []

    u_ix = len(arr)  # upper bound index
    while True:

        u_ix -= 1

        for ix in range(u_ix, -1, -1):

            if local_sum + arr[ix] == tar:
                local_comb.append(ix)
                return local_comb

            if local_sum + arr[ix] < tar:
                local_sum += arr[ix]
                local_comb.append(ix)

        if local_sum > max_sum:

            max_sum = local_sum
            max_comb = local_comb.copy()

        try:
            u_ix = local_comb.pop()
            local_sum -= arr[u_ix]
        except IndexError:
            break  # All combinations searched

    return max_comb

# }}}

# }}}


if __name__=="__main__":
    main()
