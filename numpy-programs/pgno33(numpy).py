# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 18:50:25 2024

find the mean,median,varience,std

pg no 31

@author: Riyaz
"""
import numpy as np 

n=int(input("Enter the number: "))

num=np.random.randint(1,4000,n,dtype='int16')
print(num)
print()
mean=np.mean(num)
std=np.std(num)
var=np.var(num)
median=np.median(num)
print("Mean: ",mean)
print()
print("Std: ",std)
print()
print("Varience: ",var)
print()
print("Median: ",median)