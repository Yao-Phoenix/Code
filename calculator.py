#!/usr/bin/env python3

import sys

try:
    salary = int(sys.argv[1])
except:
    print("Parameter Error")
    sys.exit()
if salary - 5000 <= 3000:
    print("{:.2f}".format((salary - 5000) * 0.03))
elif 3000 < salary - 5000 <= 12000:
    print("{:.2f}".format((salary - 5000) * 0.1 - 210))
elif 12000 < salary - 5000 <= 25000:
    print("{:.2f}".format((salary - 5000) * 0.2 - 1410))
elif 25000 < salary - 5000 <= 35000:
    print("{:.2f}".format((salary - 5000) * 0.25 - 2660))
elif 35000 < salary - 5000 <= 55000:
    print("{:.2f}".format((salary - 5000) * 0.3 - 4410))
elif 55000 < salary - 5000 <= 80000:
    print("{:.2f}".format((salary - 5000) * 0.35 - 7160))
elif salary - 5000 > 80000:
    print("{:.2f}".format((salary - 5000) * 0.45 - 15160))


