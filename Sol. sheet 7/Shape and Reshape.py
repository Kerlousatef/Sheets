# -*- coding: utf-8 -*-
"""
Created on Sat Apr 26 21:28:07 2025

@author: Lenovo
"""

import numpy as np

#6
my_array1=np.arange(1,10)
my_array1=my_array1.reshape(3,3 )

#7
my_array1=my_array1.reshape(-1)         #or my_array1=my_array1.ravel()

#8
my_array2=np.arange(100)
my_array2=my_array2.reshape(4, -1)

