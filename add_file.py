#!/usr/bin/env python3

import os


os.makedirs('/home/shiyanlou/syl/A')
fileA = open('/home/shiyanlou/syl/A/'+ '__init__' + '.py', 'w')
fileA.close()

os.makedirs('/home/shiyanlou/syl/B')
fileB = open('/home/shiyanlou/syl/B/'+ '__init__' + '.py', 'w')
fileB.close()

os.makedirs('/home/shiyanlou/syl/C')
fileC = open('/home/shiyanlou/syl/C/'+ '__init__' + '.py', 'w')
fileC.close()

file_ = open('/home/shiyanlou/syl/' + '__init__' + '.py', 'w')
file_.close()

