# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 14:18:06 2018

@author: Malviya
"""
inputVal = input('enter range: ')
n = int(inputVal)
value = 0
for x in range(0,n):
    if x%3 == 0 or x%5 == 0:
        value = value + x
print(value)