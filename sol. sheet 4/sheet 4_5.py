# -*- coding: utf-8 -*-
"""
Created on Sun Mar 30 16:25:13 2025

@author: atefkero58@gmail.com
"""

def substitute(equation, **kwargs):
    for key ,value in kwargs.items():
        equation=equation.replace(key, str(value))
    print (equation)

substitute("5*x+3*y+10*z/2",x=3,y=4,z=5)