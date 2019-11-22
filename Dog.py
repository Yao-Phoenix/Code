#!/usr/bin/env python3

class Dog:
    def __init__(self, name, age):  # 创建类的实例是不需传入 name 参数
        self.name = name            # 设置实例的属性
        self.age = age

    def __repr__(self):
        return 'Dog: {}'.format(self.name) # 自定义打印格式


dog = Dog('旺财', 2)               # 创建类的实例
print(dog)                          # 打印类的实例
print(dog.name)                     # 打印实例的属性 name
print(dog.age)
