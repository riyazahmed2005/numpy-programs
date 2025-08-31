# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 19:29:20 2024

display the segrigated numbers from the file

pg no 29.2

@author: Riyaz
"""
import numpy as np 

single=open("single.txt","rb")
snumber=np.fromfile(single,dtype='int16')
print(snumber)
print()

two=open("two.txt","rb")
tnumber=np.fromfile(two,dtype='int16')
print(tnumber)
print()

three=open("three.txt","rb")
thnumber=np.fromfile(three,dtype='int16')
print(thnumber)
