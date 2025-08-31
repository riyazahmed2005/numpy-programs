# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 18:44:10 2024

Generate a random number and segrigate the single , two digit 
three digit

pg no 27

@author: Riyaz
"""
import numpy as np

n=int(input("Enter the number: "))

rn=np.random.randint(1,128,n,dtype='int8')
print(rn)

s=(rn>=0)&(rn<=9)

t=(rn>=10)&(rn<=99) 

th=(rn>=100)&(rn<=999)

single=rn[s]
two=rn[t]
three=rn[th]
print()

print("Single: ",single)
print()
print("Two digit: ",two)
print()
print("Three: ",three)































































