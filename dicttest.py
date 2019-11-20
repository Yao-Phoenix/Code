#!/usr/bin/env python3

import sys

if __name__ == '__main__':
    courses = dict()
    for argv in sys.argv[1:]:
        id,name = argv.split(':')
        courses[id] = name
    for key,value in courses.items():
        print("ID: {} Name: {}".format(key,value))
