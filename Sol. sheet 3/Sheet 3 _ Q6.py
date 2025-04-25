# -*- coding: utf-8 -*-
"""
Created on Tue Mar 11 18:17:09 2025

@author: Lenovo
"""

# Your code here
d1 = {'a': 1}
d2 = {'a': 2}
d3 = {'b': 3}
all_dicts = [d1, d2, d3]
fin_di = {}
for x in all_dicts:
    fin_di.update(x)
print(fin_di)