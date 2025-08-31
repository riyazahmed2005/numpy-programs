# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 19:35:38 2024

generate a random number and store in file and segrigate the 
single digit,two digit ,three digit number nad writen in anothe file

pg no 29

@author: Riyaz
"""
import numpy as np 

n=int(input("Enter the number to generate: "))

rn=np.random.randint(1,700,n,dtype='int16')
print(rn)

f1=open("word.txt","wb")
rn.tofile(f1)
f1.close()

print("stored")

