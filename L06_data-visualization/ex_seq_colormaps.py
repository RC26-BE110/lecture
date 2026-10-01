#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 09:26:35 2018

@author: Reggie DePiero
Math 3340, Summer 2018

Description: 
    Testing sequential color maps
    
"""
import numpy as np
import matplotlib.pyplot as plt

fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
number_of_plots=10
colormap = plt.cm.nipy_spectral #I suggest to use nipy_spectral, Set1,Paired
ax1.set_color_cycle([colormap(i) for i in np.linspace(0, 1,number_of_plots)])
for i in range(1,number_of_plots+1):
    ax1.plot(np.array([1,5])*i,label=i)

ax1.legend(loc=2)  