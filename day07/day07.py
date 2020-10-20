#!/usr/bin/python3
#-*- conding: utf-8 -*-
class Student(object):
    def __init__(self,name,score):
        self.__name = name
        self.__score = score
    def print_score(self):
        print ('%s : %s' % (self.__name,self.__score))
    def print_grade(self):
        if self.__score > 90:
            return 'this is very good'
        else:
            return 'this is bad'
student = Student('mcj',10)
print (student.print_grade())
