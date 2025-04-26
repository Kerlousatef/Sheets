# -*- coding: utf-8 -*-
"""
Created on Sat Apr 26 23:50:13 2025

@author: atefkero58@gmail.com
"""

#12
import numpy as np
a = np.arange(10).reshape(-1,2)
b = np.arange(10,20).reshape(-1,2)
x=np.concatenate((a,b),axis=1)              #Horizontal (5,4)
y=np.concatenate((a,b),axis=0)              #Vertical   (10,2)


