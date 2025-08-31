# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 19:53:34 2024

find the add,sub,mul the two matrix

pg no 54

@author: Riyaz
"""
import numpy as np 

mat1=np.random.randint(1,2000,(10,10),dtype='uint16')

mat2=np.random.randint(1,2000,(10,10),dtype='uint16')


add_mat=np.add(mat1,mat2)
print("add_mat",add_mat)
print()

sub_mat=np.subtract(mat1,mat2)
print("sub_mat",add_mat)
print()

mul_mat=np.dot(mat1,mat2)
print("mul_mat",add_mat)
print()