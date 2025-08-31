# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 18:12:51 2024

pg no 9

generate a normal distribution of n random numbers

@author: Riyaz
"""

import numpy as np 

n=int(input("Enter: "))

# np.random.normal(mean,sd,n)


distribution = np.random.normal(8,9,n)

print(distribution)