# -*- coding: utf-8 -*-
"""
Created on Tue Mar 11 17:08:42 2025

@author: Lenovo
"""

# Your code here
sequence = [10, 20, 30, 40, 50, 60]
even_sum = 0
odd_sum = 0
for x in range(len(sequence)):
    if x % 2 == 0 :
        even_sum+= sequence[x]
    else:
        odd_sum += sequence[x]

print(f" The sum of evens is: {even_sum}, and the sum of odds is: {odd_sum} .")