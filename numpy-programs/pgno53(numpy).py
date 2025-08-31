# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 19:50:42 2024

Find the sum of the matrix,rw and column

pg no 53

@author: Riyaz
"""
import numpy as np

file=open("2d.txt","rb")

n=np.fromfile(file,dtype='uint16')

x=n.reshape((5,5))

print(x)
print()

add=x.sum()
print("sum : ",add)
print()

add_row=x.sum(1)
print("sum row: ",add_row)
print()

add_column=x.sum(0)
print("sum column: ",add_column)
