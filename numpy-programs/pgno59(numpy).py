# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 19:21:25 2024

Store your bio data in file and load it

pg no 59

@author: Riyaz
"""
import numpy as np 

dty={'names':('name','age','dept','rollno','year'),
       'formats': ((np.str_,12),np.uint8,(np.str_,10),np.uint64,np.uint8)}

data=('fayaz',19,'C.S.E',811722104124,3)

bio=np.array(data,dty)

file=open("bio.txt","wb")

bio.tofile(file)

file.close()

print("Data stored")                   
                   
