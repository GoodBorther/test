#!/usr/bin/python3
#-*- conding: utf-8 -*-
## 将方法定义为属性
class Student(object):
    

    @property
    def score(self):
        return self._score


    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0~100!')
        self._score = value
## 多重继承
## 定义Runnable和Flyable的功能
class Runnable(object):
    def run(self):
        print('Running...')
class Flyable(object):
    def fly(self):
        print('Flying...')
class Animal(object):
    pass
## 大类
class Mammal(Animal):
    pass
class Bird(Animal):
    pass
## 各种动物
class Dog(Mammal,Runnable):
    pass
class Bat(Mammal,Flyable):
    pass
class Parrot(Bird):
    pass
class Ostrich(Bird):
    pass

## 定制类
class Student(object):
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return 'Student object (name: %s)' % self.name
    __repr__ = __str__
class Fib(object):
    def __init__(self):
        self.a,self.b = 0,1
    def __iter__(self):
        return self
    def __next__(self):
        self.a,self.b = self.b,self.a + self.b
        if self.a > 100000:
            raise StopIteration()
        return self.a
    def __getitem__(self,n):
        if isinstance(n,int):
            a,b = 1,1
            for x in range(n):
                a,b = b,a + b
            return a
        if isinstance(n,slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a,b = 1,1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a,b = b,a + b
            return L
#for n in Fib():
#    print (n)
#f = Fib()
#print (f[0:5])
class Student1(object):
    def __init__(self):
        self.name = 'mcj'
    def __getattr__(self,attr):
        if attr == 'score':
            return 99
s = Student1()
print (s.name)
print (s.score)
print (s.asda)
class Test(object):
    def __init__(self,name):
        self.name = name
    def __call__(self):
        print ('My name is %s.' % self.name)
q = Test('MCJ')
print (q())
print (callable(Student))
##枚举类
from enum import Enum,unique

@unique

class Gender(Enum):
    Male = 0
    Female = 1
class Student(object):
    def __init__(self, name, gender:Gender):
        self.name = name
        self.gender = gender
