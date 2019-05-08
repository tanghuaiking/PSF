#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 14:32:09 2018

@author: kingpc
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 09:35:31 2018

@author: kingpc
"""
from numpy import *  
import numpy as np
#from scipy.fftpack import fft,ifft,ifftshift,fftshift
from numpy.fft import fft,ifft,fft2,ifft2,ifftshift,fftshift
import matplotlib.pyplot as plt 
import seaborn
import math


N=1000
y = zeros((N),dtype=float) 
x=np.linspace(1,N,N)  
yf = zeros((N),dtype=float)
sig=5#number of  Radius of 1st ring
for nn in range(0,N):     
    y[nn]=math.e**(-1*(x[nn]-(N/2+1))**2 /(sig**2))
    yf[nn]=math.e**(-1*((x[nn]-(N/2+1))/N)**2 *(sig*pi)**2)
yy=fftshift(abs(fft(y)))
yft=ifftshift(yf)   
     
y2=abs(fftshift(ifft((yft))) ) 
y22=y2/max(y2)
yy2=yy/max(yy)

plt.subplot(221)
plt.plot(x,abs(y-y22) )
plt.subplot(222)
plt.plot(x,-1*log10(abs(y-abs(y22))))  
plt.subplot(223)
plt.plot(x,abs(yy2-yf))
plt.subplot(224)
plt.plot(x,-1*log10(abs(yy2-yf )))  
plt.show()
