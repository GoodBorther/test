#!/usr/bin/python3
#-*- conding: utf-8 -*-
def log(func):
    def wrapper(*args,**kw):
        print ('call %s():' % func.__name__)
        return (func(*args,**kw))
    return wrapper
@log
def f1():
    print ('this is a f1')
@log
def f2():
    print ('this is a f2')
f1()
f2()
