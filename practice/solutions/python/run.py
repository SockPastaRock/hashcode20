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
    runTests(TESTS_DIR)

# }}}
# {{{ formatOutput


def formatOutput(combination):
    """Formats the output of the combination to hashcode specs."""

    return (str(len(combination)) + "\n" + str(combination)[1:-1]).replace(",", "")

# }}}
# {{{ buildMemo


def buildMemo(arr, tar):
    """Build memo table for sums of subsets of arr between zero and tar."""

    memo = []
    base = 1 << tar
    memo.append(base)
    for ix, x in enumerate(arr):
        memo.append(memo[ix] | memo[ix] >> x)

    return memo

# }}}
# {{{ readMemo


def readMemo(memo, arr, tar):
    """Docstring for readMemo"""

    ix_row = len(memo) - 1
    combination = []
    ix_col = tar
    while ix_row > 0:
        row_str = bin(memo[ix_row])[2:]
        nxt_str = bin(memo[ix_row - 1])[2:]

        while row_str[ix_col] == "0":
            ix_col -= 1
        if nxt_str[ix_col] == "0":
            combination.append(ix_row - 1)
            ix_col -= arr[ix_row - 1]
        ix_row -= 1
    return combination

# }}}
# {{{ runTests


def runTests(tests_dir):
    """Runs all test files in the given directory."""

    for test_case in os.listdir(tests_dir):
        try:
            print()
            print("Running test: " + str(test_case))

            with open(tests_dir + test_case, "r") as f:
                tar, n_pizzas = list(map(int, f.readline().split(" ")))
                arr = list(map(int, f.readline().split(" ")))

            result = formatOutput(readMemo(buildMemo(arr, tar), arr, tar))

            path_output = OUTPUT_DIR + "output_" + test_case[:test_case.rfind(".")] + ".txt"
            os.makedirs(os.path.dirname(path_output), exist_ok=True)
            with open(path_output, "w") as f:
                f.write(result)
                print("Result written to: " + str(path_output))
        except KeyboardInterrupt:
            print("Test cancelled.")
        except Exception as e:
            print("Test failed with error: " + str(e))

# }}}

# }}}


if __name__=="__main__":
    main()
