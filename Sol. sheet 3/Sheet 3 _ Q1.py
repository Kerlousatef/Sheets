# -*- coding: utf-8 -*-
"""
Created on Thu Apr 24 16:25:46 2025

@author: Lenovo
"""

number_of_runs = 0
total_time = 0
while True:
    number= input("Enter 10 km run time: ")
    if number=="0" or number =="":
        break
    
    elif number.replace(".", "") .isdigit() :
        number=float(number)
        total_time+= number
        number_of_runs+=1
        
    else:
        print("Invalid number!")
        continue

if number_of_runs > 0 :
    avg= total_time/number_of_runs
    print(f"The average is: {avg:.2f}, and number of runs is: {number_of_runs:d}")