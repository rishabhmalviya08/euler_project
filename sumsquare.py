# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 18:51:01 2018

@author: Malviya
"""

size = 100
sum_of_n = 0
sum_of_sq = 0
sq = 0

for x in range(1, size + 1):
    sq = x*x
    sum_of_sq = sum_of_sq + sq
    sum_of_n = sum_of_n + x

sq_of_sum = sum_of_n*sum_of_n
diff = sq_of_sum - sum_of_sq    
    
print(diff)    
    
