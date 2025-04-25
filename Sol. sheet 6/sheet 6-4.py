# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 22:24:49 2025

@author: atefkero58@gmail.com
"""

myfile=open("section6","r")
lines= myfile.read()
myfile.close()


for x in lines[49:60]:
    print (x.strip())