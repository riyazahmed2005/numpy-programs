# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 19:10:39 2024

sum the single digit two digit and three digit number
using numpy boolean array

pg no 28

@author: Riyaz
"""
import numpy as np 

n=int(input("Enter the number: "))
rn=np.random.randint(1,1500,n,dtype='int16')

print(rn)
s=(rn>=0)&(rn<=9)
t=(rn>=10)&(rn<=99)
th=(rn>=100)&(rn<=999)
f=(rn>=1000)&(rn<=9999)
print()

'''
If use the sum() method in the boolean array it
return the count value based on the condition

'''
print("single digit: ",sum(s))
print("Two digit: ",sum(t))
print("Three digit: ",sum(th))
print("Four digit: ",sum(f))

