#!/usr/bin/env python3

import sys

if __name__ == '__main__':
    courses = set()
    for argv in sys.argv[1:]:
        courses.add(argv)
    print(' '.join(courses))
