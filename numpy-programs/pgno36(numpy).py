# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 19:44:24 2024

Split the array

pg no 36

@author: Riyaz
"""
import numpy as np

n=int(input())

arr1=np.random.randint(1,1000,n,dtype='int16')
print(arr1)
print()

s=int(input("Enter the split : "))

x=np.split(arr1,s)
print(x)
print()

a,b,c,d,e=np.split(arr1,5)
print(a)
print(b)
print(c)
print(d)
print(e)
print()

x1=np.split(arr1,[3,10,60])
print(x1)
