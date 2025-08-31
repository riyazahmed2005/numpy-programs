# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 18:40:44 2024

Generate a random number and extract the positive
number by passing the boolean array

pg no 26

@author: Riyaz
"""

import numpy as np 

n=int(input())

rn=np.random.randint(-127,128,n,dtype='int8')
print()
print(rn)
print()
b=rn>0 

positive=rn[b]

print()
print("Positive: ",positive)