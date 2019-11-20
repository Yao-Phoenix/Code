#!/usr/bin/env python3

import sys

if __name__ == '__main__':
    a_list=[] 
    b_list=[]
    for argv in sys.argv[1:]:
        if len(argv) <= 3:
            a_list.append(argv)
        elif len(argv) > 3:
            b_list.append(argv)
    print(' '.join(a_list))
    print(' '.join(b_list))
