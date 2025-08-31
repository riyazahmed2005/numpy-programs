# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 18:27:08 2024

Generate the set of random numbers extract only the positive
number

pg no 25

@author: Riyaz
"""

import numpy as np 

n=int(input())
print()

rn=np.random.randint(-127,128,n,dtype='int8')

print(rn)
print()

print(rn>0)