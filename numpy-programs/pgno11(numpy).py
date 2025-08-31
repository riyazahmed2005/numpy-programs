# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 18:45:25 2024

pg no 11

print the attribute of the given array

@author: Riyaz
"""
import numpy as np 

n=int(input("Enter size: "))

arr=np.random.randint(0,128,n,dtype='uint8')

arr1=np.random.randint(100,32768,n,dtype='uint16')

print(arr)
print()
print("Dimension :",arr1.ndim)
print()
print("shape: ",arr1.shape)
print()
print("datatype: ",arr1.dtype)
print()
print("itemsize: ",arr1.itemsize)
print()
print("number_of_bytes: ",arr1.nbytes)