#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 21 15:00:20 2020

@author: jaga
"""

import numpy as np
from matplotlib import pyplot as plt
fig , ax = plt.subplots(1,1)

# Definition of the PDF
def pdf(x):
    if 3 <= x <= 7:
       return 0.25
    else:
       return  0

# Definition of the function from which samples will be drawn
def fun(x):
    if 3 <= x <= 7:
       return 10
    else:
       return  0

steps = 100000
theta = 0.0
sampl_arr = np.zeros(steps)
rejected_sampl_arr = np.zeros(steps)
pdf_arr = np.zeros(steps)
steps_arr = np.zeros(steps)
x = np.linspace(0,10,steps)

for i in range(steps):
    theta_prime = theta + np.random.standard_normal()
    r = np.random.rand()
    pdf_arr[i] = pdf(x[i])
    steps_arr[i] = i
    if fun(theta)!=0.0:
        if (fun(theta_prime)/fun(theta)) > r:
                theta = theta_prime
    else:
        theta = theta_prime
    sampl_arr[i] = theta
    rejected_sampl_arr[i] = theta_prime

# plotting of sample histogram and PDF    
ax.plot(x,pdf_arr, color = 'red' , label='Uniform PDF')
plt.hist(sampl_arr, density = 'true' , bins = 100 , 
                        label = 'Histogram Plot for n=100000' )
plt.title('Uniform Distribution \n Using Metropolis Algorithm' ,
                         color = 'red' , fontsize = 20)
plt.xlabel('x' , fontsize = 15)
plt.ylabel('p(x)' , fontsize = 15)
plt.legend()
plt.xlim(2,8)
plt.ylim(0,0.35)
plt.show()

# plotting of Markov Chain
plt.scatter(steps_arr , rejected_sampl_arr,
            marker = '*' , s = 1 , color = 'Green' , label = "Rejected points")
plt.plot(steps_arr , sampl_arr , label = "Markov chain" , color = 'Red')
plt.xlabel('steps', fontsize = 17)
plt.ylabel('theta' , fontsize = 17)
plt.ylim(0,10)
plt.xlim(0,10000)
plt.title('Markov Chain.', fontsize=20 , color = 'red')
plt.legend()
plt.show()
