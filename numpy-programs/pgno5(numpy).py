# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 18:36:32 2024

pg no 5

create a array of zeros, ones, fill the value with particular
number and empty array 


@author: Riyaz
"""
import numpy as np 

n=int(input("Enter : "))

a1=np.zeros(n)  #array of zeros
print(a1)

a2=np.ones(n)   #array of ones
print(a2)

a3=np.full(124,n)   # full the array with given val
print(a3)

a4=np.empty(n)  # empty array
print(a4)