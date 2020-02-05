#!/usr/bin/python3

# {{{ Imports

import random
import sys

# }}}
# {{{ Functions

# {{{ main

def main():

    _, tar, num_elements = sys.argv
    tar = int(tar)
    num_elements = int(num_elements)
    # tar = 1000000000
    # num_elements = 2000


    arr = set([])
    while len(list(arr)) != num_elements:
        arr.add(int(random.uniform(0, tar)))
    arr = list(arr)
    arr.sort()
    arr = str(arr)[1:-1].replace(",", "")
    s = str(tar) + " " + str(num_elements) + "\n" + str(arr)
    print(s)
    # $python3 random_test.py 100000000 2000 > rand_x.in

# }}}

# }}}


if __name__=="__main__":
    main()
