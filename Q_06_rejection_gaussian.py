#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 21 10:07:11 2020

@author: jaga
"""

import numpy as np
from matplotlib import pyplot as plt

# definition and plotting the given distribution
def non_uni_dist(x):
    return np.exp( - x * x / 2) * np.sqrt(2 / np.pi)
x = np.arange( 0 , 5 , 0.01) 
plt.plot(x , non_uni_dist(x) , color = 'red' , label = 'Given Distribution')

# generating the uniformly distributed random points 
n = 100000
x = np.random.rand(n) 

# defining an envelop function to get more efficiency
def envelop_fun(x):
    return 1.5 * np.exp(-x)
# Applying transformation method to get sample drawn from exp(-x)
x = - np.log(x) 
# corresponding distribution Probability
y = np.random.rand(n) * envelop_fun(x)

# Filtering the good points rejecting the bad ones
x_good = x [ y < non_uni_dist(x)]
plt.hist(x_good , density = 'true' , bins = 30 , label = 'Histogram Plot with bin=30')

plt.title("Random numbers following showed distribution \n generated through Rejection Method" , 
          fontsize = 15 ,color = 'red')
plt.xlabel('x' , fontsize = 13)
plt.ylabel('p(x)' , fontsize = 13)
plt.legend()