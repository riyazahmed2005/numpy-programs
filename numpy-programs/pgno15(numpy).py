# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 19:14:15 2024

implement the differnet types of slicing

pg no 15

@author: Riyaz
"""
import numpy as np 

f=open("word.txt","rb")

a=np.fromfile(f,dtype='uint16')

n=int(input("Starting index: "))

m=int(input("Ending index: "))

s=int(input("Step to: "))

print(a)

print()
s1=a[n:]
s2=a[:m]
s3=a[n:m:s]
s4=a[::-1]
s5=a[-n:]
s6=a[:-m]
s7=a[-m:-n]
s8=a[:]
s9=a[-m:-n:s]
print("slice 1: ",s1)
print()
print("slice2: ",s2)

print()
print("slice 3: ",s3)
print()
print("slice4: ",s4)
print()
print("slice 5",s5)
print()
print("slice 6: ",s6)
print()
print("slice 7: ",s7)
print()
print("slice8: ",s8)
print()
print("slice 9: ",s9)


