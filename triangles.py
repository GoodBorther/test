#!/usr/bin/python3
#-*- conding: utf-8 -*-
def triangles(m=11):
    num = [1]
    while m > 0:
        yield num
        for  i in range(1, len(num)):
            num[i] = pre[i] + pre[i - 1]
        num.append(1)
        pre = num[:]
        m = m - 1
for i in triangles():
    print (i)
