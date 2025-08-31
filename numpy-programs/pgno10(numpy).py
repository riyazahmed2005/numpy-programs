# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 18:08:42 2024

pg no 10

generate a array of of n integer number

@author: Riyaz
"""
import numpy as np 

n=int(input("Enter size: "))

arr=np.random.randint(0,128,n,dtype='uint8')

print(arr)

