# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 19:57:37 2024

Load the csv file and print it 


pg no 61

@author: Riyaz
"""
import numpy as np 

dty={'names':('name','class','rollno','language','maths','science','social','others','total','avg','Result'),
       'formats': ((np.str_,12),np.uint8,(np.str_,10),np.uint8,np.uint8,np.uint8,np.uint8,np.uint8,np.uint16,np.float16,(np.str_,10))}

data=np.loadtxt("marksheet.csv",delimiter=",",dtype=dty)

print(data)
