#!/usr/bin/python3
#-*- conding: utf-8 -*-
class Student(object):
    count = 0
    def __init__(self,name,score):
        self.__name = name
        self.__score = score
        Student.count += 1
    def print_score(self):
        print ('%s : %s' % (self.__name,self.__score))
    def print_grade(self):
        if self.__score > 90:
            return 'this is very good'
        else:
            return 'this is bad'
student = Student('mcj',10)
qaq = Student('wangwu',20)
print (Student.count)
