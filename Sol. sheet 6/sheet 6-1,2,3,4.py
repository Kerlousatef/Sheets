# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 22:31:14 2025

@author: atefkero58@gmail.com
"""
# 1
import json
users = [
    {"username": "Kerlous", "password": "0123ff#"},
    {"username": "Abanoub", "password": "zzz12*"},
    {"username": "Ahmed ", "password": "ll1245"},
    {"username": "Omar", "password": "004kk"}
    ]
file = open("users.json", "w")
file.write(json.dumps(users))
file.close()

#2
import json
users = [
    {"username": "Kerlous", "password": "0123ff#"},
    {"username": "Abanoub", "password": "zzz12*"},
    {"username": "Ahmed ", "password": "ll1245"},
    {"username": "Omar", "password": "004kk"}
    ]
file = open("users.json", "r")
users = json.load(file)  
file.close()
print(f"First user: {users[0]["username"]} , pass: {users[0]["password"]}")

#3
import json
users = [
    {"username": "Kerlous", "password": "0123ff#"},
    {"username": "Abanoub", "password": "zzz12*"},
    {"username": "Ahmed ", "password": "ll1245"},
    {"username": "Omar", "password": "004kk"}
    ]
users.append({"username": "Basssam", "password": "bess11*"})
file = open('users.json', 'w')
file.write(json.dump(users))
file.close()
print("The  new user is added")

#4
import json
users = [
    {"username": "Kerlous", "password": "0123ff#"},
    {"username": "Abanoub", "password": "zzz12*"},
    {"username": "Ahmed ", "password": "ll1245"},
    {"username": "Omar", "password": "004kk"}
    ]
file = open("users.json", "r")
users = json.load(file)
file.close()
username_input = input("Enter username: ")
password_input = input("Enter password: ")

for user in users:
    if user["username"] == username_input and user["password"] == password_input:
        found = True
        break
    else:
        found=False
print("Login Success!" if found else "Login Failed")
































