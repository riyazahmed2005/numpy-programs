# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 16:41:42 2024

extract the number from the file and make some changes in that and 
print the orginal and the modified array

pg no 13 


@author: Riyaz
"""

import numpy as np 

f=open("word.txt","rb")

arr=np.fromfile(f,dtype='uint16')

n=int(input("Enter start pos: "))

s1=arr[n:] #it just only create a view of the orginal array

s1[2]=222 

s1[3]=555

s1[0]=666

print("orginal array: ",arr)
print()
print()
print("modified: ",s1)