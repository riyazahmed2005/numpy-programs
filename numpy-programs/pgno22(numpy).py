# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 17:28:11 2024

calculate a deduction of the basic pay

pg no 22

@author: Riyaz
"""
import numpy as np 

n=int(input())

bp=np.random.randint(5000,25000,n,dtype='uint16')

pf=bp*(25/100)
print("PF: ",pf)

print()

insurence=bp*(20/100)
print()
print("Insurence: ",insurence)


