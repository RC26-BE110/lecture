#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 09:04:39 2018

@author: Reggie DePiero
Math 3340, Summer 2018

Description: 
    
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

x = np.linspace(1,10,5)

y1 = x+1;
y2 = x+2;
y3 = x+3;
y4 = x+4;
y5 = x+5;
y6 = x+6;
y7 = x+7;
y8 = x+8
y9 = x+9
y10 = x+10
y11 = x+11
y12 = x+12


plt.figure()

fig,
(ax1, ax2) = plt.subplots(1,2)

## plot original data
#plt.plot(x_plot,y_plot, '--') 
## plot polynomial interpolation
#plt.plot(x_plot,interp, '-')
##plot nodes
#plt.plot(x_data,y_data,'o')
plt.plot(x,y12,'-',linewidth=2)
plt.plot(x,y11,'-',linewidth=2)
plt.plot(x,y10,'-',linewidth=2)
plt.plot(x,y9,'-',linewidth=2)
plt.plot(x,y8,'-',linewidth=2)
plt.plot(x,y7,'-',linewidth=2)
plt.plot(x,y6,'-',linewidth=2)
plt.plot(x,y5,'-',linewidth=2)
plt.plot(x,y4,'-',linewidth=2)
plt.plot(x,y3,'-',linewidth=2)
plt.plot(x,y2,'-',linewidth=2)
plt.plot(x,y1,'-',linewidth=2)

plt.title("The 10 Default Cylced Python colors", size = 14, weight = 'bold')
plt.xlabel("x")
plt.ylabel("y")
plt.legend(('1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10'))
plt.savefig("plot_colors.eps")

plt.figure()
cmap = plt.get_cmap("tab10")
plt.plot(x,y1,color='r',linewidth=2)
plt.plot(x,y2,color='g',linewidth=2)
plt.plot(x,y3,color='b',linewidth=2)
plt.plot(x,y4,color='c',linewidth=2)
plt.plot(x,y5,color='m',linewidth=2)
plt.plot(x,y6,color='y',linewidth=2)
plt.plot(x,y7,color='k',linewidth=2)
plt.legend(('red','green','blue','cyan','magenta','yellow','black'))
plt.title('Pre-defined Line Colors',size = 14, weight = 'bold')

plt.figure()
plt.plot(x,y1,color='r',x,y2,color='g')