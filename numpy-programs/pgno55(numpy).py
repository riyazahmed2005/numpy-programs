# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 19:00:14 2024

print the transpose , diagonal ,and trace of the matrix

pg no 54    

@author: Riyaz
"""
import numpy as np 

mat=np.random.randint(1,20,(10,10) ,dtype='uint8')

#transpose 

trans=np.transpose(mat)
print(trans)
print()

diagonal=mat.diagonal()
print(diagonal)
print()

trace=mat.trace()
print(trace)

