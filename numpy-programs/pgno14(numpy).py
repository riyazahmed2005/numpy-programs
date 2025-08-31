# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 18:58:53 2024

extract the single,two,three digit of the file
pg no 14

@author: Riyaz
"""
import numpy as np 

f=open("word.txt","rb")

a=np.fromfile(f,dtype='uint16')

single=[i for i in a if(i>=0 and i<=9)]

two=[j for j in a if(j>=10 and j<=99)]

three=[k for k in a if(k>=100 and k<=999)]

print("single: ",single)
print()
print("Two digit: ",two)
print()
print("Three digit: ",three)

f.close()