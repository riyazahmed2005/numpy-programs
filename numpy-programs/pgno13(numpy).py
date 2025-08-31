# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 18:44:07 2024

load the entire file

pg no 13

@author: Riyaz
"""
import numpy as np 

f=open("word.txt","rb")

a=np.fromfile(f,dtype='uint16')

print(a)

f.close()
