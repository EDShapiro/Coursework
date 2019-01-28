# -*- coding: utf-8 -*-
"""
Created on Wed Feb 01 19:21:14 2017

@author: EvanD
"""

import numpy as np
import matplotlib.pyplot as plt

 

def myfun(x,t,c_max=1,c_res=1000):
    return np.array( [ [x, t**0.5] for t in np.linspace(0,c_max,c_res) ])

 

x = 4
t = 10
y = myfun(t,x,c_max = 5)
plot1 = plt.scatter(y[:,0], y[:,1])
#plot1 = plt.scatter(x,t,color = 'red')
plt.show(plot1)