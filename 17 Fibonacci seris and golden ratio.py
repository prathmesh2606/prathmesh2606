# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 20:03:04 2020

@author: Prathmesh
"""
# Welcome Message
print("================= Welcome to Fibonacci calculator App ===================")

# Getting input from user
num = int(input("How many Digits of Fibonacci sequence would you like to compute: "))

# Logic of fibonacci series
a,b=0,1
print("The First",num,"numbers of fibonacci series is: ")
for i in range(num):
    print(b)
    a,b=b,a+b
    
# Golden Ratio
print("\nThe Corresponding Golden values Ratio are: ")
a,b=0,1
for i in range(num):
    a,b=b,a+b
    print(b/a)
print("\nThe Ratio of Consecutive Fibonacci terms approches Phi; 1.618...")