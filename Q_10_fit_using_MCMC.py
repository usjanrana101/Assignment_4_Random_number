#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 21 18:43:57 2020

@author: jaga
"""

import numpy as np
from matplotlib import pyplot as plt

file = '/home/jaga/Desktop/com_phy_assgts/assgt4/data.txt'
x , y , sigma_y = np.loadtxt(file , usecols = (2,4,6) , unpack = 'True')

# Defining the likelihood
def log_likelihood(parameter, x, y, sigma_y):
    a , b , c = parameter
    model = (a * x**2 + b * x + c)
    var = sigma_y**2
    # actually negative ln L and that's why we need to minimize it
    return 0.5 * np.sum((y - model) ** 2 / var +
                        np.log(2 * np.pi * var))

# Uniform prior dist. of our parameters    
def log_prior(parameter):
    a , b , c = parameter
    if  -1000 < a < 1000 and -500.0 < b < 500 and 0.0 < c < 1000.0 :
        return 0.0
    return -np.inf

# Defining the posterior probabilitity of our parameters
def log_posterior(parameter, x, y, sigma_y):
    log_pr = log_prior(parameter)
    if not np.isfinite(log_pr):
        return -np.inf
    return log_pr - log_likelihood(parameter, x, y, sigma_y)

# minimizing the -ln L i.e maximizing the  L ,which is objective fun. here
from scipy.optimize import minimize
guess = (1. , 1. ,1.)
soln = minimize(log_likelihood , guess , args=(x, y, sigma_y))

# initializing the Markov Chains of parameters
nwalkers, ndim = 50, 3
pos = soln.x + 1e-5 * np.random.randn(nwalkers, ndim)

# MCMC through emcee lib.
import emcee
sampling_tool = emcee.EnsembleSampler(nwalkers , ndim , 
                                log_posterior , args=(x, y, sigma_y))
sampling_tool.run_mcmc(pos, 4000)
samples = sampling_tool.get_chain()

# Calculating the best fitted value i.e. mean of posterior PDF
a_best=np.median(samples[:,:,0])
b_best=np.median(samples[:,:,1])
c_best=np.median(samples[:,:,2])

# Calculating the one-sigma uncertainties i.e. Standard Deviation
# of posterior PDF
one_sigma_a=np.std(samples[:,:,0])
one_sigma_b=np.std(samples[:,:,1])
one_sigma_c=np.std(samples[:,:,2])


print("Best Fitted Values of a , b , c are respectively : \n" ,
               a_best , '\t' , b_best , '\t' , c_best , '\n')
print("One-Sigma Uncertainties Values of a , b , c are respectively : \n" ,
               one_sigma_a , '\t' , one_sigma_b , '\t' , one_sigma_c, '\n')

#Markov Chains of parameters
plt.plot(samples[:,:,0] , color='red')
plt.title('Markov Chains for parameter a ' , fontsize = 20)
plt.ylabel('a' , fontsize = 13)
plt.xlabel('steps' , fontsize = 13)
plt.show()

plt.plot(samples[:,:,0] , color='red')
plt.title('Markov Chains for parameter b ' , fontsize = 20)
plt.ylabel('b' , fontsize = 13)
plt.xlabel('steps' , fontsize = 13)
plt.show()

plt.plot(samples[:,:,0] , color='red')
plt.title('Markov Chains for parameter c ' , fontsize = 20)
plt.ylabel('c' , fontsize = 13)
plt.xlabel('steps' , fontsize = 13)
plt.show()


# Plotting the joint and marzinalized PDF using corner
import corner
data = np.vstack([samples[i] for i in range(len(samples))])
fig = corner.corner(data , truths = [a_best , b_best , c_best],
                    labels = [r"$a$", r"$b$", r"$c$",r"$\Gamma \, [\mathrm{parsec}]$"],
                    show_titles = True , title_kwargs = {"fontsize": 15}) 
plt.show()

# Random index for 200 models
index = np.random.randint( 0 , nwalkers * 4000 , 200)

def fun(parameters , x):
    return(parameters[0] * x**2 + parameters[1] * x + parameters[2])
    
# Considering the max and min value of x of the given data
x_arr = np.linspace(0 , 290 , 400)
parameters_best=np.array([a_best , b_best , c_best])    
 
# Plotting of Best_fitted model and Data   
plt.errorbar(x, y, yerr = sigma_y , fmt='o' , ecolor = 'black' , capsize = 5)
plt.plot(x_arr , fun(parameters_best , x_arr),
         lw = 2 , color = 'black' , label = 'Best Fitted Model')

# Plotting of another 200 models from posterior PDF 
fun_pts = []
x_pts = []
for i in range(200):
    parameters = data[index[i]]
    plt.scatter(x_arr , fun (parameters , x_arr) , marker="o" ,
                s = 0.01 , color = 'Orange')
    for j in range(len(x_arr)):
        x_pts.append(x_arr[i])
        fun_pts.append(fun(parameters , x_arr))
    
plt.title('Data and Best-Fitted Model \n with other 200 Models ',
          fontsize=20)
plt.xlabel('x',fontsize=15)
plt.ylabel('y(x)',fontsize=15)
plt.legend()
plt.show()