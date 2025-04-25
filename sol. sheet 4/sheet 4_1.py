# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 23:58:02 2025

@author: atefkero58@gmail.com
"""

import random 
def generate_password(length, chars):
    password = "".join(random.choices(chars,k=length))
    print (password)
    
generate_password(8, "abcde")