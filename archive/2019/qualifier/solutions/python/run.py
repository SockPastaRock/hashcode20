#!/bin/python3

# {{{ Imports

import os

# }}}
# {{{ Constants

TESTS_DIR = "./local/tests/"
OUTPUT_DIR = "./local/output/"

# }}}
# {{{ Photos

# {{{ Photo


class Photo():
    """docstring for Photo"""

# {{{ Constructor


    def __init__(self, photo_line):
        photo_elements = photo_line.replace("\n", "").split(" ")

        self.orientation = photo_elements[0]
        self.num_tags = int(photo_elements[1])
        self.tags = photo_elements[2:]

# }}}
# {{{ Methods


# }}}

# }}}

# }}}
# {{{ Functions

# {{{ runTests


def runTests(tests_dir):
    """Runs all test files in the given directory."""


    for test_case in os.listdir(TESTS_DIR):
        print()
        print("Running test: " + str(test_case))

        with open(TESTS_DIR + test_case, "r") as f:
            num_photos = int(f.readline())
            photos = []
            for _ in range(num_photos):
                photos.append(Photo(f.readline()))

        buildSlideshow(photos)

# }}}
# {{{ buildSlideshow


def buildSlideshow(photos):
    """Creates an interesting slideshow of photos"""

    tag_buckets = {}
    for photo in photos:
        if photo.num_tags not in tag_buckets:
            tag_buckets[photo.num_tags] = [photo]
        else:
            tag_buckets[photo.num_tags].append(photo)

    keys = list(tag_buckets.keys())
    keys.sort(reverse=True)
    for k in keys:
        target = int(k/2)

# }}}

# }}}


if __name__ == '__main__':
    runTests(TESTS_DIR)

"""

We know the following:

    TODO

"""
