# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 21:57:05 2018

@author: Malviya
"""

n = 4000000
n1 = 0
n2 = 1
sum = 0
while True:
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    if n3 > n:
        break
    if n3%2 == 0:
        sum = sum + n3
print(sum)        
    
        
        