# -*- coding: utf-8 -*-
"""
Created on Thu Mar 13 10:50:12 2025

@author: Lenovo
"""

# Your code here
fl_num = 88887.778
bef_int_num = 2
aft_int_num = 3
num =str(fl_num)
x,y = num.split(".")
print(x[-bef_int_num:] +"."+y[:aft_int_num])

