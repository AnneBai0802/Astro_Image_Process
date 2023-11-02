# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from astropy.io import fits
import plotdata as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

def gauss_function(x, a, x0, sigma):
    return a*np.exp(-(x-x0)**2/(2*sigma**2))


hdulist = fits.open("Astro\Astro\Fits_Data\mosaic.fits")
data = hdulist[0].data
flatten=[]
data2=np.array([[]])
for i in  range(500,len(data)-400):
    data2=np.append(data2,(data[i]))
    for j in range(400,len(data[i])-400):
        flatten.append(data[i][j])
values, edges = np.histogram(flatten,bins = 100, range = (3200,3700))
bins = np.array([(edges[i]+edges[i+1])/2 for i in range(len(edges)-1)])
popt, pcov = curve_fit(gauss_function, bins, values, p0 = [1e6, 3421, 10])


text = 'Mean:'+f"{popt[1]:.5g}"+'$\pm$'+f"{np.sqrt(pcov[1][1]):.1g}"+'\nStandard Deviation: '+f"{popt[2]:.3g}" +'$\pm$'+f"{np.sqrt(pcov[2][2]):.1g}"
plt.stairs(values,edges,fill = True,label='Histogram')
plt.plot(bins,gauss_function(bins,popt[0],popt[1],popt[2]),label = 'Gaussian Fit')
plt.title('Background Counts')
plt.xlabel('Counts')
plt.ylabel('Frequency')
plt.legend()
plt.text(3450,0.6e6,text)
plt.show()
hdulist.close()
