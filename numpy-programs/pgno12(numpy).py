# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 18:39:21 2024

generate a random number write into the file
pg no 12

@author: Riyaz
"""
import numpy as np

n=int(input())

arr=np.random.randint(0,999,n,dtype='int16')
print(arr)

f=open("word.txt","wb")

arr.tofile(f)

f.close()
