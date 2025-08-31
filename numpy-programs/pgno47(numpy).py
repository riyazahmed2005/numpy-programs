# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 18:22:35 2024

slice the extracted array

pg no 47

@author: Riyaz
"""
import numpy as np

file=open("2d.txt","rb")

n=np.fromfile(file,dtype='uint16')

x=n.reshape((5,5))
print("Before slice ->",x)
print()

s1=x[:2]
print("slice 1->",s1)
print()

s2=x[1:]
print("slice 2->",s2)
print()

s3=x[1:3]
print("slice 3->",s3)
print()

s4=x[0:5:2]
print("slice 4->",s4)
print()

s5=x[::-1]
print("slice 5->",s5)
print()

s6=x[-5:]
print("slice 6->",s6)
print()

s7=x[:-2]
print("slice 7->",s7)
print()

s8=x[-4:-1]
print("slice 8->",s8)
print()

s9=x[-5:-1:2]
print("slice 9->",s9)