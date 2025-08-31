# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 19:57:15 2024

Create own tabel using dictionary

pg no 58

@author: Riyaz
"""
import numpy as np 

dty={'names':('Name','age','Dept','Rollnumber'),
       'formats': ((np.str_,12),np.uint8,(np.str_,5),np.uint64)}

data=("Riyaz ahmed",19,"C.S.E",811722104124)


a=np.array(data,dty)

print(a)


