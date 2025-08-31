# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 16:43:24 2024

pg no 20
generate a fahrenheit temperature and convert into celcius


@author: Riyaz
"""
import numpy as np

n=int(input())

f=np.random.rand(n)*100

print(f)
print()
c=5/9*(f-32)

print(c)