#!/usr/bin/python3
#-*- conding: utf-8 -*-
try:
        print('try...')
        r = 10 / 2
        print('result:', r)
except ZeroDivisionError as e:
        print('except:', e)
finally:
        print('finally...')
        print('END')
