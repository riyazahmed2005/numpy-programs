# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 19:05:29 2024

pg no 49

row and column slicing

@author: Riyaz
"""
import numpy as np

file=open("2d.txt","rb")

n=np.fromfile(file,dtype='uint16')

x=n.reshape((5,5))

print("Orginal: ",x)
print()

s1=x[2:,2:]
print("slice 1->")
print(s1)
print()

s2=x[:4,:4]
print("slice 2->")
print(s2)
print()

s3=x[2:4,1:4]
print("slice 3->")
print(s3)
print()

s4=x[1:5:2,1:5:2]
print("slice 4->")
print(s4)
print()

s5=x[::-1,::-1]
print("slice 5->")
print(s5)
print()

s6=x[-3:,-2:]
print("slice 6->")
print(s6)
print()

s7=x[:-3,:-3]
print("slice 7->")
print(s7)
print()

s8=x[-5:-1,-5:-2]
print("slice 8->")
print(s8)
print()




