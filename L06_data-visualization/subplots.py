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
# import matplotlib as mpl

x = np.linspace(1,10,5)

y1 = x+1;
y2 = x+2;


fig, (ax1, ax2) = plt.subplots(1,2)
### second subplot
ax1.plot(x,y2,'-',linewidth=2)
ax1.plot(x,y1,'-',linewidth=2)
ax1.set_title('1st Plot')

### second subplot
ax2.plot(x,y2,'-',linewidth=2)
ax2.plot(x,y1,'-',linewidth=2)
ax2.set_title('2nd Plot')

fig.suptitle('Subplots',size=14,weight='bold')