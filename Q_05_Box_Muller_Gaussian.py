#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 21 08:55:12 2020

@author: jaga
"""

import numpy as np
from matplotlib import pyplot as plt

# generating the uniformly distributed random points
n = 10000
x1 = np.random.rand(n)
x2 = np.random.rand(n)

# Applying the Transformation to uniformly distribyted random variable x1 and x2 
y1 = np.sqrt(-2 * np.log(x1)) * np.cos(2 * np.pi * x2)
y2 = np.sqrt(-2 * np.log(x1)) * np.sin(2 * np.pi * x2)

plt.hist(y1 , density = 'true' , bins = 30 , label = 'Histogram Plot for n=10000')

# Plotting the Standard Noramal PDF
def stand_normal(x):
    return np.exp( - x * x / 2) / np.sqrt(2 * np.pi)
x = np.arange( -5 , 5 , 0.01) 
plt.plot(x , stand_normal(x) , color = 'red' , label = 'N(0,1) PDF')

plt.ylim(0,.5)
plt.title("Random numbers following N(0,1) distribution \n generated through Box-Muller Method" , 
          fontsize = 15 ,color = 'red')
plt.xlabel('x' , fontsize = 13)
plt.ylabel('p(x)' , fontsize = 13)
plt.legend()