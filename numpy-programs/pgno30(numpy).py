# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 19:46:43 2024

print the sum of the even and odd number from the 
individual file 

pg no 30

@author: Riyaz
"""
import numpy as np 

single=open("single.txt","rb")
single_digit=np.fromfile(single,dtype='int16')

single_even=single_digit%2==0 
single_odd=single_digit%2!=0

print("single even: ",sum(single_even))
print("single odd",sum(single_odd))
print()



two=open("two.txt","rb")
two_digit=np.fromfile(two,dtype='int16')

two_even=two_digit%2==0 
two_odd=two_digit%2!=0

print("Two even: ",sum(two_even))
print("Two odd",sum(two_odd))

print()

three=open("three.txt","rb")
three_digit=np.fromfile(three,dtype='int16')

three_even=three_digit%2==0 
three_odd=three_digit%2!=0

print("three even: ",sum(three_even))
print("three odd",sum(three_odd))
