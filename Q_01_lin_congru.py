#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 21 00:00:43 2020

@author: jaga
"""

import numpy as np
import timeit
from matplotlib import pyplot as plt

''' returns n uniformly distributed random numbers generated 
         through Linear Congruential Method
                 between [0,max_range]....'''
def lin_congru(n , max_range , seed ):
    a = 1103515245
    c = 12345
    m = 2 ** 31
    max_range = max_range
    random_nums = np.zeros(n)
    for i in range(n):
        random_nums[i] = seed
        seed = ( a * seed + c ) % m
    return (max_range * random_nums) / max(random_nums)

# Obtaining n random numbers from the above function
n = 10000
start_time = timeit.default_timer() # initializing clock

# calling lin_congru() for range [0,1]
max_range = 1
uni_rand_nums = lin_congru( n , max_range , 1)
print("Time taken to generate ",n,
      " uniformly distributed random numbers through Linear Congruential Method is : ",
       timeit.default_timer() - start_time ,"sec" )
plt.hist(uni_rand_nums , density ='true' , label = " Histogram Plot for n =10000 ")

# Plotting the uniform PDF
x = []
y = []
for i in range(100):
    y.append(1)
    x.append( i/100)
plt.plot( x , y , color = 'red' , label = 'Uniform PDF')

plt.title("Random numbers between 0 and 1 generated through \n Linear Congruential Method" , 
          fontsize = 15 ,color = 'red')
plt.xlabel('x' , fontsize = 13)
plt.ylabel('p(x)' , fontsize = 13)
plt.legend()

 