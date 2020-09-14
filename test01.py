#!/usr/bin/python3
# -*- coding: utf-8 -*-
def test02(n):
    if n == 1:
        print(1)
    else:
        return test02(n-1*n)


test02(5)
