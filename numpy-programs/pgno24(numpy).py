# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 17:49:27 2024

calculate the netslary in single expression

pg no 23.1

@author: Riyaz
"""

import numpy as np 

n=int(input("Enter the no of employee salary: "))

bp=np.random.randint(5000,25000,n,dtype='uint16')



print()
print(bp)

ns=((bp*(30/100))+(bp*(20/100)))-((bp*(25/100))+(bp*(20/100)))

print("-------netsalary-----------")
print()
print(ns)

print("Found" if(22242 in bp) else "Not found")