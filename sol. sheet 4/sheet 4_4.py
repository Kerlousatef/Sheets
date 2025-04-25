# -*- coding: utf-8 -*-
"""
Created on Sun Mar 30 15:41:34 2025

@author: atefkero58@gmail.com
"""
def average(*numbers):
    s= sum(numbers)
    avg= s / len(numbers)
    return avg
lst1=[5,6,7,8,9,10]
print(average(*lst1))