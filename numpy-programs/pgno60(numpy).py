# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 19:31:21 2024

Load the bio data from the file 

pg no 60

@author: Riyaz
"""
import numpy as np 

file=open("bio.txt","rb")

dty={'names':('name','age','dept','rollno','year'),
       'formats': ((np.str_,12),np.uint8,(np.str_,10),np.uint64,np.uint8)}

arr=np.fromfile(file,dtype=dty)

print(arr)