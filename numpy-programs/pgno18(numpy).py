# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 17:21:56 2024

Extract and make the seperate copy of the array

@author: Riyaz
"""
import numpy as np 

f=open("word.txt","rb")


print("----------orginal array----------")
print()
arr=np.fromfile(f,dtype='uint16')
print(arr)
print()


n=int(input("Starting pos : "))
m=int(input("Ending pos: "))
step=int(input("Step to skip: "))
print()
s1=arr[n:].copy()
print("Extract 1: ",s1)
print()

s2=arr[:m].copy()
print("Extract 2: ",s2)
print()

s3=arr[n:m].copy()
print("Extract 3: ",s3)
print()

s4=arr[n:m:step].copy()
print("Extract 4: ",s4)
print()

s5=arr[-n:]
print("Extract 5: ",s5)
print()

s6=arr[:-m].copy()
print("Extract 6: ",s6)
print()

s7=arr[-m:-n].copy()
print("Extract 7: ",s7)
print()

s8=arr[-m:-n:step].copy()
print("Extract 8: ",s8)
print()

s9=arr[::-1].copy()
print("Extract 9: ",s9)
print()


