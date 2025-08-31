# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 19:09:05 2024

find the unique value of the array

pg no 37

@author: Riyaz
"""
import numpy as np 

n=int(input("Enter the number: "))

arr=np.random.randint(1,100,n,dtype='int16')
print(arr)
print()
x1=np.unique(arr)
print("Unique: ",arr)
print()

x2=np.unique(arr,return_index=True)
print("Unique index: ",x2)
print()

x3=np.unique(arr,return_counts=True)
print("Unique counts: ",x3)
print()

x4=np.unique(arr,return_index=True,return_counts=True)
print("Unique count and index: ",x4)