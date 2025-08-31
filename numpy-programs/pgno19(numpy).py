# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 17:54:28 2024

Convet the feet into meters using numpy 

pg no 19
@author: Riyaz
"""
import numpy as np 

n=int(input("Enter the number of feet: "))

feet=np.random.randint(0,5000,n,dtype='uint16')

meters=feet * 0.3048

'''
Instead of applying loop to multiply the value to all
the element in array ,we can use array_name * value we
want to multiply -> advantages of the numpy 
 
'''

print("Feet: ",feet)

print()

print("Meters: ",meters)