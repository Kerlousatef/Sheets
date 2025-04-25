# -*- coding: utf-8 -*-
"""
Created on Tue Mar 11 18:50:13 2025

@author: 𝐇𝐀𝐌𝐎𝐎𝐃
"""

number_of_runs = 0
total_time = 0

while True:
    X = input("Enter 10 km run time: ")
    
    if X == "" or X == "0":
        break
    
    if X.replace('.', '', 1).isdigit():  #for float numbers
        run_time = float(X)
        total_time += run_time
        number_of_runs += 1
    else:
        print("Invalid input!!. Please enter a  number* .")

if number_of_runs > 0:
    average = total_time / number_of_runs
    print(f"Average of {average}, over {number_of_runs} runs")
else:
    print("No runs recorded.")