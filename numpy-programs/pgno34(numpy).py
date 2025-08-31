# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 19:17:51 2024

sort the array and flip the array

pg no 8.8.2024

@author: Riyaz
"""
import numpy as np

n=int(input())

arr=np.random.randint(1,4000,n,dtype='int16')
print(arr)
print()
sort=np.sort(arr)
print("Sort: ",sort)

print()

flip=np.flip(arr)
print("Flip the array: ",flip)