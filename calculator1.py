#!/usr/bin/env python3
import sys
"""
def salary_insurance(salary):
    insurance = salary * 0.165
    return insurance

def income(salary):
    insurance = salary_insurance(salary)
    income = salary - insurance -5000
    return income
"""
def result(salary):
    income_ = salary - salary * 0.165 - 5000
    if income_ <= 0:
        result = 0
    elif income_ <= 3000:
        result = income_ * 0.03
    elif income_ <= 12000:
        result = income_ * 0.1 - 210
    elif income_ <= 25000:
        result = income_ * 0.2 - 1410
    elif income_ <= 35000:
        result = income_ * 0.25 - 2660
    elif income_ <= 55000:
        result = income_ * 0.30 - 4410
    elif income_ <= 80000:
        result = income_ * 0.35 - 7160
    else:
        result = income * 0.45 - 15160
    Salary = salary - salary * 0.165 - result
    return Salary

if __name__ == '__main__':
    input_ = dict()
    output_ = dict()
    Result = []
    for argv in sys.argv[1:]:
        id, salary = argv.split(':')
        try:
            input_[id] = int(salary)
        except:
            print("Parameter Error")
            exit()
    Salary = list(input_.values())
    ID = list(input_.keys())
   # print(Salary)
    for i in Salary:
        Result.append(result(i))
    for key, value in zip(ID, Result):
        print("{}:{:.2f}".format(key,value))
