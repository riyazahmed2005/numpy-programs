# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 17:49:58 2024

Create a 5x5 matrix and write in a file

pg no 45

@author: Riyaz
"""
import numpy as np

arr=np.random.randint(1,2000,(5,5),dtype='uint16')
print(arr)
file=open("2d.txt","wb")

arr.tofile(file)
print("Matrix stored")

file.close()

