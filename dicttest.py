#!/usr/bin/env python3
import sys

output_dict = {}
def handle_data(str_):
    id,name = str_.split(':')
    output_dict[id] = name

def print_data(k,v):
    print("ID: {} Name: {}".format(k,v))


if __name__ == '__main__':

    for arg in sys.argv[1:]:
        handle_data(arg)

    for key in output_dict:
        print_data(key, output_dict[key])
