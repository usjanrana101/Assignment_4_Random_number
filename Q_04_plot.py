#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 16:02:25 2020

@author: jaga
"""

import numpy as np
from matplotlib import pyplot as plt

def exp_dist(x):
    return 2 * np.exp( -2 * x)
x = np.arange(0 , 10 , 0.01)
plt.plot(x , exp_dist(x) , label = 'Exponential Dist. with mean 0.5' , color = 'red')

# Data imported from the file created by running c code in terminal
file = '/home/jaga/Desktop/com_phy_assgts/assgt4/Q_04_data.txt'
data_from_c = np.loadtxt(file)

plt.hist(data_from_c, density = 'true' , bins = 50 , label = 'Histogram of Random Nos')
plt.title(" Random Nos. Using Transformation Method" , fontsize = 15 ,color = 'red')
plt.xlabel('x' , fontsize = 13)
plt.ylabel('p(x)' , fontsize = 13)
plt.xlim(0,8)
plt.legend()