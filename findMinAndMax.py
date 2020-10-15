#!/usr/bin/python3
#-*- conding: utf-8 -*-
def findMinAndMax(L):
    if L==[]:
        return(None,None)
    else:
        MIN = L[0]
        MAX = L[0]
        for i in L:
            if MIN > i:
                MIN = i
            if MAX < i:
                MAX = i
        return (MIN,MAX)
# 测试
if findMinAndMax([]) != (None, None):
        print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
        print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
        print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
        print('测试失败!')
else:
        print('测试成功!')
