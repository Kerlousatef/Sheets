# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 22:19:24 2025

@author: atefkero58@gmail.com
"""

myfile=open("section6","w")
for x in range(1,101):
    myfile.write(f"{x}\n")
myfile.close()