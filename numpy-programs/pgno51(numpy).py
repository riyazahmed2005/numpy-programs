# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 19:25:56 2024

find the minimum element of the matrix,row and column

pg no 51

@author: Riyaz
"""
import numpy as np

file=open("2d.txt","rb")

n=np.fromfile(file,dtype='uint16')

x=n.reshape((5,5))

print(x)
print()

matrix_min=x.min()
print("matrix min",matrix_min)
print()

min_row=x.min(1)
print("min row",min_row)
print()

min_column=x.min(0)
print("min column",min_column)
print()




