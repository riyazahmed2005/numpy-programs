# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 17:33:05 2024

Calculate the net salary of the employe

pg no 23

@author: Riyaz
"""
import numpy as np 

n=int(input())

bp=np.random.randint(5000,25000,n,dtype='uint16')

print("----------------Basic pay---------------------")
print()
print(bp)
print()

#allowances
hra=bp*(30/100)
cca=bp*(20/100)
#deduction

pf=bp*(25/100)
insurence=bp*(20/100)

a=hra+cca 
d=pf+insurence

print("---------Net salary--------------")
print()
netslary=a-d
print(netslary)

