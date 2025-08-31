# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 18:59:06 2024

generate the array of marks and check the if all the student are pass
5.8.2024

@author: Riyaz
"""
import numpy as np

n=int(input("Enter the number of students: "))


marks=np.random.randint(1,100,n,dtype='int8')
print(marks)

any_pass=np.any(marks>=45)
all_pass=np.all(marks>=45)

print()
print("All the students pass the exam ? ",all_pass) #it returns the boolean value(True) if the
# all the condition are satisfied the condition otherwise False

print()
print("If any students pass the exam? ",any_pass)
#it return the vvalue true if any valuein the array
# are satisfied the given condition otherwise false