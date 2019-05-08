#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 18:00:52 2018

@author: kingpc
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 15:23:04 2018

@author: kingpc
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 15:24:30 2018

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

from math import sin
def sinc(x):
    return (sin(x) + (x == 0)) / (x + (x == 0))


N=1000
x = np.linspace(1, N, N)
y = np.linspace(1,N, N)
X,Y = np.meshgrid(x,y)
ZF=zeros((N,N),dtype=float)
Z=ones((N,N),dtype=float)
rn=2
a=1/rn
ra=math.pi/rn #Radius of 1st ring 
sigx=50
kab=1
sigy=kab*sigx
#Z = 2 * np.cos(0.2 * np.pi * X)     #光栅*1.22*pi
#ZF=math.e**(-1*((X-(N/2+1))/N*sigx*math.pi)**2)*math.e**(-1*((Y-(N/2+1))/N*sigy*math.pi)**2)
for nn in range(0,N):  
#    print(x[nn])
    for mm in range(0,N):
        Z[nn,mm]=(sinc(ra*(x[nn]-(N/2+1))))**2*(sinc(ra*(y[mm]-(N/2+1))))**2
        if 1-(abs(x[nn]-(N/2+1)))/N/a>0 and 1-(abs(y[mm]-(N/2+1)))/N/a>=0  :
            ZF[nn,mm]=(1-(abs(x[nn]-(N/2+1)))/N/a)*(1-(abs(y[mm]-(N/2+1)))/N/a)
Z_fft2 = abs(fft2(Z))
Z_fft2_sh = abs(np.fft.fftshift(Z_fft2))/max(Z_fft2[0,:])

z2=ifftshift(ZF)
z21=abs(ifft2(z2))
z22=fftshift(z21)/max(z21[0,:])

plt.subplot(221)
plt.imshow((abs(Z-z22)))
plt.colorbar()
plt.title('R')
plt.subplot(222)
plt.imshow(-1*log10(abs(Z-z22)))
plt.colorbar()
plt.title('LOG(R)')
plt.subplot(223)
plt.imshow(abs(ZF-Z_fft2_sh))
plt.colorbar()
#plt.title('fft2-shift')
plt.subplot(224)
plt.imshow(-1*log10(abs(ZF-Z_fft2_sh)+1e-15))
plt.colorbar()
plt.show()
#plt.title('x = 128')
plt.plot(x,((ZF[int(N/2)+1,:]-Z_fft2_sh[int(N/2)+1,:]))) 
#plt.plot(x,((ZF[int(N/2)+1,:]))) 
#plt.plot(x,((Z_fft2_sh[int(N/2)+1,:])))
plt.show()