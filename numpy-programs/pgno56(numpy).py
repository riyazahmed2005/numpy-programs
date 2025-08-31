# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 19:22:51 2024

Implement the horizontal and vertical stacking

pg no 56

@author: Riyaz
"""

import numpy as np 

mat1=np.random.randint(1,2000,(5,5),dtype='uint16')
mat2=np.random.randint(1,2000,(5,5),dtype='uint16')

print(mat1)
print()
print(mat2)
print()
#horizontal stacking 

horizontal=np.hstack((mat1,mat2))

#vertical stacking
vertical=np.vstack((mat1,mat2))

print(horizontal)
print()
print(vertical)

