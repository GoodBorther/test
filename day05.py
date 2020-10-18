#!/usr/bin/python3
#-*- coding: utf-8 -*-
##第一题
from functools import reduce
def normalize(name):
    name = name[0].upper()+name[1:].lower()
    return name
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)
##第二题
def test(x,y):
    return x * y
def prod(L):
    num = reduce(test,L)
    return num
print (prod([3,5,7,9]))
    
##第三题

#!/usr/bin/python3
#-*- coding: utf-8 *-*
from functools import reduce
def str3float(s):
	def fn(x,y):
		return x * 10 + y
	def str2float(s):
		digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,'.': '.'}
		return digits[s]
	def str2float1(s):
		digits = {1: 1,2: 2,3: 3,4: 4,5: 5,6: 6,7: 7,8: 8,9: 9}
		return digits[s]
	a = map(str2float,s)
	n = (list(a))
	print (n[2])
	for i in range(len(n)-1):
		if n[i] is '.':
			q = len(n) - i - 1
			w = pow(10,q)
			n.remove('.')
			e = map(str2float1,n)
			x = (list(e))
			v = reduce(fn,x)
	return (v/w)
print (str3float('123.456'))
