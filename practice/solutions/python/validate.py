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
    runTests(OUTPUT_DIR, TESTS_DIR)


# }}}
# {{{ runTests


def runTests(output_dir, tests_dir):
    """Runs all test files in the given directory."""

    for output_file in os.listdir(output_dir):
        print()
        print("Validating Output: " + str(output_file))

        file_id = output_file[7]

        with open(output_dir + output_file, "r") as f:
            n = int(f.readline())
            ixs = list(map(int, f.readline().split(" ")))

        for test_case in os.listdir(tests_dir):
            if test_case[0] == file_id:
                with open(tests_dir + test_case, "r") as f:
                    tar, n_pizzas = list(map(int, f.readline().split(" ")))
                    arr = list(map(int, f.readline().split(" ")))
        combination_sum = sum([arr[ix] for ix in ixs])

        print(combination_sum)
        print(tar)


# }}}

# }}}


if __name__=="__main__":
    main()
