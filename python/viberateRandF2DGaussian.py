#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 15:24:30 2018

@author: kingpc
"""

import  math
from numpy import *  
import numpy as np
from numpy.fft import fft,ifft,fft2,ifft2,ifftshift,fftshift
from tkinter import filedialog
import matplotlib.pyplot as plt

N=1000
x = np.linspace(1, N, N)
y = np.linspace(1,N, N)
X,Y = np.meshgrid(x,y)
sigx=5
kab=1
sigy=kab*sigx
#Z = 2 * np.cos(0.2 * np.pi * X)     #光栅
ZF=math.e**(-1*((X-(N/2+1))/N*sigx*math.pi)**2)*math.e**(-1*((Y-(N/2+1))/N*sigy*math.pi)**2)
Z=math.e**(-(X-(N/2+1))**2/(sigx**2))*math.e**(-(Y-(N/2+1))**2/(sigy**2))
Z_fft2 = fft2(Z)
Z_fft2_sh = abs(np.fft.fftshift(Z_fft2))/max(Z_fft2[0,:])

z2=ifftshift(ZF)
z21=abs(ifft2(z2))
z22=fftshift(z21)/max(z21[0,:])

plt.subplot(221)
plt.imshow(abs(Z-z22))
plt.colorbar()
plt.title('R')
plt.subplot(222)
plt.imshow(-1*log10(abs(Z-z22)+1e-22))
plt.colorbar()
plt.title('LOG(R)')
plt.subplot(223)
plt.imshow(abs(ZF-Z_fft2_sh))
plt.colorbar()
#plt.title('fft2-shift')
plt.subplot(224)
plt.imshow(-1*log10(abs(ZF-Z_fft2_sh)+1e-22))
plt.colorbar()
#plt.axis('off')
plt.tight_layout()
#plt.title('x = 128')
plt.show()