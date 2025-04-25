# -*- coding: utf-8 -*-
"""
Created on Tue Mar 11 17:17:51 2025

@author: Lenovo
"""

# Your code here
USERS = {'user1': 'password1', 'user2': 'password2'}
name_input= input("What is your name? ").strip().lower()
pass_input= input("What is the password? ").strip().lower()
if name_input in USERS and USERS[name_input]==pass_input:
    print(f"welcome back, {name_input}")
else: 
    print("Erorr")  