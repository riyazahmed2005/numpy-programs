# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 17:49:45 2024
create a list of n random number and pass into the numpy array
pg no 2 
@author: Riyaz
"""
import numpy as np
import random as rd 

list1=[rd.randint(1,1000) for i in range(501)]

a1=np.array(list1)

print(a1)