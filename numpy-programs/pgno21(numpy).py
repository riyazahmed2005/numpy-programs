# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 17:22:23 2024

Calculate the allowances of the employee using basic pay

pg no 21

@author: Riyaz
"""
import numpy as np 

n=int(input())

bp=np.random.randint(5000,25000,n,dtype='uint16')

print("Basic pay: ",bp)

hra=bp*(30/100)

cca=bp*(20/100)

print()
print("hra: ",hra)

print()
print("CCA: ",cca)

