#!/usr/bin/python3

# {{{ Imports

import os
import sys
import copy
import timeit

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

    runtime = 0
    os.makedirs(tests_dir, exist_ok=True)
    for test_case in os.listdir(tests_dir):
        print()
        print("Running test: " + str(test_case))

        with open(tests_dir + test_case, "r") as f:
            tar, n = list(map(int, f.readline().split(" ")))
            arr = list(map(int, f.readline().split(" ")))

        start = timeit.default_timer()

        try:
            writeOutput(maxCombinationSum(tar, arr), test_case, output_dir)
        except KeyboardInterrupt:
            print("\n\tTest cancelled - KeyboardInterrupt")
        except Exception as e:
            print("\tError: " + str(e))

        stop = timeit.default_timer()
        print("\tTime for test: " + str(stop - start) + " seconds.")

        runtime += (stop - start)

    if runtime == 0:
        abs_tests_path = (os.path.realpath(__file__)[:os.path.realpath(__file__).rfind("/")]
            + TESTS_DIR[1:]
        )
        abs_data_path = (
            os.path.realpath(__file__)[:os.path.realpath(__file__).rfind("/")]
        )
        abs_data_path = (
            abs_data_path[:abs_data_path.rfind("/")]
            + "/data/"
        )
        print("No test case files found in tests directory:\n\t" + abs_tests_path)
        print("\nYou can find some default test cases to use in this project's data directory:\n\t" + abs_data_path)
        print("\ncp " + abs_data_path + "* " + abs_tests_path)
    else:
        print("\nCompleted all tests in : " + str(runtime) + " seconds")



# }}}
# {{{ writeOutput


def writeOutput(result, fname, output_dir):
    """Writes output file as hashcode question specifies"""

    s = str(len(result)) + "\n" + str(result).replace(",", "")[1:-1]
    fname = fname[:fname.rfind(".")] + ".txt"
    os.makedirs(output_dir, exist_ok=True)
    with open(output_dir + fname, "w") as f:
        f.write(s)

    print("\tOutput written to: " + output_dir + fname)

# }}}
# {{{ maxCombinationSum


def maxCombinationSum(tar, arr):
    """Returns combination in arr with largest sum less than or equal to tar. O(nlog(n))"""

    n = len(arr)
    u_bound = int("1" * n, 2)
    l_bound = int("0" * n, 2)

    prev_ix = 0
    ix = 1
    while ix != prev_ix:  # binary search loop
        prev_ix = ix

        mean = bin((u_bound + l_bound) >> 1)
        ix = list(map(int, mean[-1:1:-1]))
        ix += [0] * (n - len(ix))  # add padding bits
        combination = [arr[i] for i in range(n) if ix[i]]

        if sum(combination) <= tar:
            l_bound = int(mean, 2)
        else:
            u_bound = int(mean, 2)

    return [x for x in range(n) if ix[x]]

# }}}

# }}}


if __name__=="__main__":
    main()
