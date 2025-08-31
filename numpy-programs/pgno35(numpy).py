# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 19:24:58 2024

concatenate one or more arrays

pg no 35


@author: Riyaz
"""
import numpy as np

n=int(input())

arr1=np.random.randint(1,100,n,dtype='int8')
print(arr1)
print()
arr2=np.random.randint(1,4000,n,dtype='int16')
print(arr2)
print()
arr3=np.random.randint(1,40000,n,dtype='int32')
print(arr3)
print()

x=np.concatenate([arr1,arr2,arr3])
print(x)
