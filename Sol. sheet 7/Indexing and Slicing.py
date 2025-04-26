# -*- coding: utf-8 -*-
"""
Created on Sat Apr 26 21:36:45 2025

@author: atefkero58@gmail.com
"""

import numpy as np
#9
a = np.arange(100).reshape(-1, 10)
print(a[9][2])                          #92

#10
print(a[2,:])                             #[20 21 22 23 24 25 26 27 28 29]

#11
print(a[:,3])