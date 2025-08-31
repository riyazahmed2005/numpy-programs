# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 18:03:46 2024

Continuty of pg no 46

pg no 46.1



@author: Riyaz
"""
import numpy as np

file=open("2d.txt","rb")

n=np.fromfile(file,dtype='uint16')

reshape=n.reshape((5,5))

print(reshape)

file.close()
