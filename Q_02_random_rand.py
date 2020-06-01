#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 21 08:32:02 2020

@author: jaga
"""

import numpy as np
import timeit
from matplotlib import pyplot as plt

# Obtaining n random numbers from np.random.rand
n = 10000
start_time = timeit.default_timer() # initializing clock

uni_rand_nums = np.random.rand(n)
print("Time taken to generate ",n,
      " uniformly distributed random numbers through np.random.rand is : ",
       timeit.default_timer() - start_time ,"sec" )
plt.hist(uni_rand_nums , density ='true' , label = " Histogram Plot for n =10000 ")

# Plotting the uniform PDF
x = []
y = []
for i in range(100):
    y.append(1)
    x.append( i/100)
plt.plot( x , y , color = 'red' , label = 'Uniform PDF')

plt.title("Random numbers between 0 and 1 generated \n through np.random.rand" , 
          fontsize = 15 ,color = 'red')
plt.xlabel('x' , fontsize = 13)
plt.ylabel('p(x)' , fontsize = 13)
plt.legend()

 