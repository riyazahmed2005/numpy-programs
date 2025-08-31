# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 19:35:53 2024

concatenate the two matrix horizontaly and vertically
(as same as stacking previous program)
pg no 57

@author: Riyaz
"""

import numpy as np 

mat1=np.random.randint(1,2000,(5,5),dtype='uint16')
mat2=np.random.randint(1,2000,(5,5),dtype='uint16')
mat3=np.random.randint(1,2000,(5,5),dtype='uint16')

x1=np.concatenate([mat1,mat2,mat3])

x2=np.concatenate([mat1,mat2,mat3],axis=1)

print(x1)
print()
print(x2)




