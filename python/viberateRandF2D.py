#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 10:04:15 2018

@author: kingpc
"""
import  math
import numpy as np
from numpy.fft import fft,ifft,fft2,ifft2,ifftshift,fftshift
from tkinter import filedialog
import matplotlib.pyplot as plt
N=1000
x = np.linspace(1, 1000, N)
y = np.linspace(1, 1000, N)
X,Y = np.meshgrid(x,y)
#Z = 2 * np.cos(0.2 * np.pi * X)     #光栅
Z=math.e**(-(X-500)**2/5000)*math.e**(-(Y-500)**2/5000)
Z_fft2 = fft2(Z)
Z_fft2_sh = abs(np.fft.fftshift(Z_fft2))
plt.subplot(221)
plt.imshow(Z)
plt.title('Original')
plt.subplot(222)
plt.imshow(abs(Z_fft2))
plt.title('fft2')
plt.subplot(223)
plt.imshow(Z_fft2_sh)
plt.title('fft2-shift')
plt.subplot(224)
plt.plot(Z_fft2_sh[500,:])
plt.title('x = 128')
plt.show()