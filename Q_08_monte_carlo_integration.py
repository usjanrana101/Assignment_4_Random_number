#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 21 10:25:12 2020

@author: jaga
"""

import numpy as np

def f(x,y):
    if (x ** 2 + y ** 2) <= 1:
        return 1
    else:
        return 0

'''Calculating the area of the unit circle'''
# n random points in each direction between -1 to 1
n = 100000
x = np.random.rand(n) * 2 - 1
y = np.random.rand(n) * 2 - 1
z = np.random.rand(n)

# counting the no of points inside the circle
count = 0
for i in range(n):
    if z[i] < f(x[i] , y[i]):
        count = count + 1

area = (2 ** 2) * count / n
print ("The area under the Unit circle is : " , area)


''' Generalization for calculating the volume of ten-dim sphere.
     Put dim = 2 for verification with the above code '''

dim = 10
n = 100000
def fun(x):
    s = 0
    for i in range(dim):
        s = s + x[i] ** 2
    if s <= 1:
        return 1
    else:
        return 0

# n random points in each direction between -1 to 1
all_random_pts = []
for i in range(dim):
    all_random_pts.append( np.random.rand(n) * 2 - 1 )
f = np.random.rand(n)  

# counting the no of points inside the Sphere
count = 0
for i in range(n):
    # Constructing a single point in this space
    single_point = np.zeros(dim)
    for j in range(dim):
        single_point[j] = all_random_pts[j][i]
   
    if f[i] < fun(single_point):
        count = count + 1

volume = (2 ** dim) * count / n
print ("The volume under the" , dim ,"dimensional Unit Sphere  is : " , volume)

