#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 09:26:25 2018
vibrate of R&F 
@author: kingpc
"""

# 1D
import  math
#math.e
import numpy as np
from scipy.fftpack import fft,ifft
import matplotlib.pyplot as plt
import seaborn

x=np.linspace(1,1000,1000)      
y=math.e**(-(x-500)**2/2000)
yy=fft(y)
z=ifft(yy)
yreal = yy.real
yimag = yy.imag
yf=abs(fft(y))
yf1=abs(fft(y))/len(x)
yf2 = yf1[range(int(len(x)/2))]
xf = np.arange(len(y)) 
xf1 = xf
xf2 = xf[range(int(len(x)/2))] 

plt.subplot(221)
plt.plot(x[1:1000],y[1:1000])   
plt.title('Original wave')

plt.subplot(222)
plt.plot(xf,yf,'r')
plt.title('FFT of Mixed wave(two sides frequency range)',fontsize=7,color='#7A378B')  #注意这里的颜色可以查询颜色代码表

plt.subplot(223)
plt.plot(xf1,yf1,'g')
plt.title('FFT of Mixed wave(normalization)',fontsize=9,color='r')

plt.subplot(224)
plt.plot(xf2,yf2,'b')
plt.title('FFT of Mixed wave)',fontsize=10,color='#F08080')

plt.show()

'''   '''







