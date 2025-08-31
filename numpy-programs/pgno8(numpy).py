# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 18:00:00 2024

generate a real random number 0 to 1000 using numpy

pg no 8

@author: Riyaz
"""
import numpy as np 

n=int(input("Enter: "))

arr1=np.random.rand(n)*1000

print(arr1)


