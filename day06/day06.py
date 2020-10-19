#!/usr/bin/python3
#-*- coding: utf-8 -*-
def calc_sum(*args):
    def sum():
        ax = 0 
        for n in args:
            ax = ax + n
        return ax
    return sum
f1 = calc_sum(1,2,3,4)
print (f1())
