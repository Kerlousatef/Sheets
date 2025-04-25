# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 23:42:36 2025

@author: atefkero58@gmail.com
"""

result = " ".join([chr(i) for i in range(ord("A"), ord("Z"))] + 
                 [chr(j) for j in range(ord("a"), ord("z"))] +  
                 [chr(k) for k in range(ord("0"), ord("9"))])  

print(result)
