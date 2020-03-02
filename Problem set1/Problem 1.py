# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 01:49:09 2020

@author: Mostafa Atalla
"""

#This code is to calculate the number of vowels in a string

s='ahshdgfsfsgsh'

vowels=['a','e','i','o','u']

n=0

for char in s:
    if char in vowels:
        n+=1

print("Number of vowels: " + str(n))
