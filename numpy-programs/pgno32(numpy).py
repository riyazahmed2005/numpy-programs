# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 19:16:47 2024

generate the random number and count the positive and 
negative number orelse sum the bool array

pg no 32

@author: Riyaz
"""
import numpy as np 

n=int(input("Enter: "))

number=np.random.randint(-1000,1000,n,dtype='int16')

print(number)
print()

positive=np.count_nonzero(number>0)

negative=np.count_nonzero(number<0)

print("Positive: ",positive)
print()
print("Negative: ",negative)
print()

con1=number>0
con2=number<0

print("positive count using sum(): ",sum(con1))
print()
print("negative count using sum(): ",sum(con2))