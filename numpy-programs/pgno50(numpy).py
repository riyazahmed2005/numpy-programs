# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 19:17:00 2024

find the maximum element of the entire matrix

row,column

pg no 50

@author: Riyaz
"""
import numpy as np

file=open("2d.txt","rb")

n=np.fromfile(file,dtype='uint16')

x=n.reshape((5,5))

print(x)
print()

#max of the entire matrix

matrix_max=x.max()
print("matrix max",matrix_max)
print()

max_row=x.max(1)
print("max row",max_row)
print()

max_column=x.max(0)
print("max column",max_column)
print()
