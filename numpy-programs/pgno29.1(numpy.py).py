# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 19:05:00 2024

data segrigation 


@author: Riyaz
"""
import numpy as np 

f2=open("word.txt","rb")
arr=np.fromfile(f2,dtype='uint16')
print(arr)

s=(arr>=0)&(arr<=9)
t=(arr>=10)&(arr<=99)
th=(arr>=100)&(arr<=999)

#single digit storation on single.txt
single_digit=arr[s]
s1=open("single.txt","wb")
single_digit.tofile(s1)
s1.close()

#two digit storation on two.txt
two_digit=arr[t]
t1=open("two.txt","wb")
two_digit.tofile(t1)
t1.close()

#three digit storation on three.txt
three_digit=arr[th]
th1=open("three.txt","wb")
three_digit.tofile(th1)
th1.close()



