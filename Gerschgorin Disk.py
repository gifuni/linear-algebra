#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 15:16:04 2017

@author: anthonygifuni
"""

import matplotlib.pyplot as plt
import numpy as np

A = np.matrix( ((2,1,0), (0.5, 6,0.5), (2,0,8)) )
n = 3

lst = []
lstr = []
for i in range(0,n):
    lst.append(A.item(i,i))
    lstr.append(np.sum(np.absolute(A[i])-np.absolute(A.item(i,i))
    

circle1 = plt.Circle((lst[0], 0), lstr[0], color='r', clip_on=False)
circle2 = plt.Circle((lst[1], 0), lstr[1], color='blue', clip_on=False)
circle3 = plt.Circle((lst[2], 0), lstr[2], color='g', clip_on=False)

fig, ax = plt.subplots() # note we must use plt.subplots, not plt.subplot
# (or if you have an existing figure)
# fig = plt.gcf()
# ax = fig.gca()

ax.add_artist(circle1)
ax.add_artist(circle2)
ax.add_artist(circle3)

fig.show()