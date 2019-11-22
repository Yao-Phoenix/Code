#!/usr/bin/env python3

class A:
    def test(self):
        print('----testA----')

class B:
    def test(self):
        print('----testB----')

class Person(A,B):
    pass

person = Person()
person.test()
print(Person.mro()) #类名.mro()方法可以查看该类的继承顺序，也就是调用方法的解析顺序
