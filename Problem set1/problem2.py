# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 01:58:44 2020

@author: Mostafa Atalla
"""

#Problem2 solution for edx Introduction to computer science

s='azcbobobegghaklbob'
n=0
for i in range(len(s)-2):
    if s[i:i+3] == 'bob':
        n+=1
        
print("Number of times bob occurs is: "+str(n))

#for i in range(len(s)-2)