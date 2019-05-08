#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 09:35:31 2018

@author: kingpc
"""
from sympy import *
from numpy import *  
import numpy as np
#from scipy.fftpack import fft,ifft,ifftshift,fftshift
from numpy.fft import fft,ifft,fft2,ifft2,ifftshift,fftshift
import matplotlib.pyplot as plt 
import seaborn
import math
import scipy


from math import sin
def sinc(x):
    return (sin(x) + (x == 0)) / (x + (x == 0))
#    return (scipy.special.jn(1,abs(x-(10000/2+1)*a*3.831705970207513)/abs(x-(10000/2+1)*a*3.831705970207513+1e-40)))
                            
N=100000
y =zeros((N),dtype=float)    #先创建一个全零方阵A，并且数据的类型设置为float浮点型  
x=np.linspace(1,N,N)  
#xf=np.linspace(1,N,N)  
yf = zeros((N),dtype=float)
y3 = zeros((N),dtype=float)
ran=2#number of  Radius of 1st ring
ra=math.pi/ran #Radius of 1st ring 
a=ra/math.pi # 
for nn in range(0,N):     
    y[nn]=sinc(ra*(x[nn]-(N/2+1)))**2
    if (1-abs(x[nn]-(N/2+1))/a/N)>0:
        yf[nn]=(1-abs(x[nn]-(N/2+1))/a/N)  
yy=fftshift(abs(fft(y)))
yft=ifftshift(yf)   
xf=  np.linspace(-0.5,0.5,N)    
y2=abs(fftshift(ifft((yft))))

 
k=float(pi/(2*Si(N/3*pi)))
#1.000006079257701
#1.000004052863771


y22=y2/max(y2)*k
yy2=yy/max(yy)/k
zz=(y-abs(y22))
zzf=(yy2-yf)
zz[int(N/2)-200:int(N/2)+200]=1e-10
#zzf[int(N/2)-100:int(N/2)+100]=1e-40

plt.subplot(221)
plt.plot(x,(zz) )
plt.subplot(222)
plt.plot(x,-1*log10(abs(zz)))  
plt.subplot(223)
plt.plot(xf,zzf)
plt.subplot(224)
plt.plot(xf,-1*log10(abs(zzf )))  
plt.show()