# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 14:18:06 2018

@author: Malviya
"""

n = input('enter the number of values you want to average:')
i = int(n)
x = 0
value = 0
for x in range(1, i+1) :
    ent = input('enter number '+ str(x) + ':')
    integer = int(ent)
    value = integer + value

    
print('average is ', value/i)