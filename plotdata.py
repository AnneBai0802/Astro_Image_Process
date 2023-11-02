# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 21:12:40 2021

@author: jm497
"""

import matplotlib.pyplot as plt
from numpy import min, max, where, any

def plot_data(xdata,ydata,xdata_start,xdata_end):
    
    xdata_index1 = where(xdata <= xdata_start)
    if not any(xdata_index1):
        xdata_index1 = 0
        print('Lower limit outside range. Minimum value is ', xdata[0])
    else:
        xdata_index1 = max(xdata_index1)
    
    xdata_index2 = where(xdata >= xdata_end)
    if not any(xdata_index2):
        xdata_index2 = -1
        print ('Upper limit outside range. Maximum value is ', xdata[-1])
    else:
        xdata_index2 = min(xdata_index2)


    plt.figure()
    plt.plot(xdata[xdata_index1:xdata_index2],ydata[xdata_index1:xdata_index2])
    if min(xdata) >= 0.0:
        plt.ylabel("Amplitude [a.u.]")
        plt.xlabel("Time (s)")
        plt.title("Recorded Signal")
        plt.show()
    else:
        plt.ylabel("Magnitude [a.u.]")
        plt.xlabel("Frequency (Hz)")
        plt.title("Absolute Value of Fourier Transform")
    plt.show()