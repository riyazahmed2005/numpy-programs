# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 17:53:03 2024

Load the content from the file and print it

pg no 46

@author: Riyaz
"""
import numpy as np

file=open("2d.txt","rb")

n=np.fromfile(file,dtype='uint16')
print(n)
print(n.reshape((5,5)))
file.close()


# if we load the file it return the value in 1d array
#because the content are store in array of element


# follow the next program