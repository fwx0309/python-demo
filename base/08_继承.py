# -*-coding: Utf-8 -*-
# @File : 08_继承 .py
# author: fwx
# Time：2024/1/30

# 动物类
class Animal:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def run(self):
        print("动物跑...")

# 狗类
class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name)
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def call(self):
        print("汪汪叫...")

# 测试
dog = Dog("小白",2)
print(dog.name)
print(dog.age)
