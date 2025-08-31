# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 16:56:10 2024

extract the orginal copy of the array 

pg no 17 


@author: Riyaz
"""
import numpy as np 

f=open("word.txt","rb")

arr=np.fromfile(f,dtype='uint16')


n=int(input("Enter the pos: "))

s1=arr[n:].copy() # extract the orginal copy of the array with seperate memory


s1[2]=333

s1[5]=456 

s1[6]=666

print("orginal: ",arr)
print()
print("extract : ",s1)