#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 15:23:04 2018

@author: kingpc
"""
from scipy.special import j1 as J1
import scipy
from scipy import array
import  math
from numpy import *  
import numpy as np
from numpy.fft import fft,ifft,fft2,ifft2,ifftshift,fftshift
from tkinter import filedialog
import matplotlib.pyplot as plt

def integJ(x):
    return -1*math.pi*((scipy.special.jn(0,x)**2+scipy.special.jn(1,x)**2)-(scipy.special.jn(0,1e-50)**2+scipy.special.jn(1,1e-50)**2))

N=100
x = np.linspace(1, N, N)
y = np.linspace(1,N, N)
X,Y = np.meshgrid(x,y)
ZF=zeros((N,N),dtype=float)
Z=ones((N,N),dtype=float)
rn=2
a=1/rn
a2=a/2
sigx=50
kab=1
sigy=kab*sigx
kab=1-0.0156125
inteJ=integJ(N/rn*(1/pi)**0.5*pi*kab)
inteJu=integJ(1e200)
k=inteJu/inteJ
#print(k)

#Z = 2 * np.cos(0.2 * np.pi * X)     #光栅*1.22*pi#3.831705970207513
Z=4*(scipy.special.jn(1,((X-(N/2+1))**2+(Y-(N/2+1))**2)**0.5*a*pi)/(((X-(N/2+1))**2+(Y-(N/2+1))**2)**0.5*a*pi))**2
Z[int(N/2),int(N/2)]=1
#ZF=math.e**(-1*((X-(N/2+1))/N*sigx*math.pi)**2)*math.e**(-1*((Y-(N/2+1))/N*sigy*math.pi)**2)
for nn in range(0,N):  
    for mm in range(0,N):
#        if nn !=N/2 or mm!=N/2:
#            Z[nn,mm]=Z2[nn,mm]
        if 2-((x[nn]-(N/2+1))**2+(y[mm]-(N/2+1))**2)**0.5/N/a2>=0 :
            #ZF[nn,mm]=1-((x[nn]-(N/2+1))**2+(y[mm]-(N/2+1))**2)**0.5/N/a2
            edg=a2-((x[nn]-(N/2+1))**2+(y[mm]-(N/2+1))**2)**0.5/N/2         
            ZF[nn,mm]=2*(math.asin((edg*2/a2-edg*edg/a2/a2)**0.5)*a2*a2-(edg*2*a2-edg*edg)**0.5*(a2-edg))/(pi*a2*a2)           
               
Z_fft2 = abs(fft2(Z))
Z_fft2_sh = abs(np.fft.fftshift(Z_fft2))/max(Z_fft2[0,:])/k


z2=ifftshift(ZF)
z21=abs(ifft2(z2))
z22=fftshift(z21)/max(z21[0,:])

plt.subplot(221)
plt.imshow((abs(Z-z22)))
plt.colorbar()
plt.title('R')
plt.subplot(222)
plt.imshow(-1*log10(abs(Z-z22)+1e-6))
plt.colorbar()
plt.title('LOG(R)')
plt.subplot(223)
plt.imshow(abs(ZF-Z_fft2_sh))
plt.colorbar()
#plt.title('fft2-shift')
plt.subplot(224)
plt.imshow(-1*log10(abs(ZF-Z_fft2_sh)+1e-10))
plt.colorbar()
plt.show()
#plt.title('x = 128')
ccc=(ZF[int(N/2)+1,:]-Z_fft2_sh[int(N/2)+1,:])
ddd=-1*log10(abs(ccc[100:int(N/2)-100]))
plt.plot(ddd) 
#plt.plot(x,((ZF[int(N/2)+1,:]))) 
#plt.plot(x,((Z_fft2_sh[int(N/2)+1,:])))
plt.show()
plt.plot(ccc) 
#plt.plot(x,((ZF[int(N/2)+1,:]))) 
#plt.plot(x,((Z_fft2_sh[int(N/2)+1,:])))
plt.show()

#
#ZFD1 = abs(ZF[int(N/2)+1,:]-Z_fft2_sh[int(N/2)+1,:])
#ZFD=ZFD1/max(ZFD1)*1.1
#plt.plot(x,((ZFD))) 
#plt.plot(x,((ZF[int(N/2)+1,:]))) 
##ZFD=ZFD1/max(ZFD1)
##zz=ZFD-Z_fft2_sh[int(N/2)+1,:]
##zz[2000]=0
##plt.plot(x,((zz)))
###plt.plot(x,((ZF[int(N/2)+1,:]))) 
###plt.plot(x,((Z_fft2_sh[int(N/2)+1,:])))
#plt.show()
#
#
#
#ZFD=ZFD1/max(ZFD1)*1.0475
#zz=ZFD-Z_fft2_sh[int(N/2)+1,:]
#zz[2000]=0
#zz[2001]=0
#plt.plot(x,((zz)))
###plt.plot(x,((ZF[int(N/2)+1,:]))) 
###plt.plot(x,((Z_fft2_sh[int(N/2)+1,:])))
#plt.show()











