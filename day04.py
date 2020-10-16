#!/usr/bin/python3
#-*- conding: utf-8 -*-
def Fibonacci(count):
    a,b = 1,0 
    while count > 1:
        a,b = b,a+b
        yield b
        count = count-1
for n in Fibonacci(9):
    print (n)
x = Fibonacci(8)
print (next(x))
print (next(x))
print (next(x))
print (next(x))
print (next(x))
print (next(x))
