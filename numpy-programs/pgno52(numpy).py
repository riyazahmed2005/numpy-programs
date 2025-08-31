# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 19:29:53 2024

find the index of the arg and min of the matrix
 with row and column
 
pg no 52

@author: Riyaz
"""
import numpy as np

file=open("2d.txt","rb")

n=np.fromfile(file,dtype='uint16')

x=n.reshape((5,5))

print(x)
print()

matrix_index=x.argmax()
print("matrix max index",matrix_index)
print()

max_index_row=x.argmax(1)
print("max index row",max_index_row)
print()

max_index_column=x.argmax(0)
print("max index column",max_index_column)
print()

matrix_index_min=x.argmin()
print("matrix min index",matrix_index_min)
print()

min_index_row=x.argmin(1)
print("min index row",min_index_row)
print()

min_index_column=x.argmin(0)
print("min index column",min_index_column)
print()


