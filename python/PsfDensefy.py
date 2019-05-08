#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 17:44:48 2019


@author: kingpc
"""

import os,sys
import time
import math
import numpy as np
from numpy.fft import fft,ifft,fft2,ifft2,ifftshift,fftshift
from PsfBuild import *

def PutZeros(fpsf,dn):
    accd=len(fpsf[0,:]);  
    evenorodd=accd%2
    fdpsf=np.zeros((accd*dn,accd*dn))
    if evenorodd==0 : #even
        for nx in range(0,accd*dn):
            for ny in range(0,accd*dn):

                if nx<=accd/2 :
                    if ny<=accd/2:
                        fdpsf[nx,ny]=fpsf[nx,ny];
                    elif ny>= dn*accd-accd/2+1:
                        fdpsf[nx,ny]=fpsf[nx,ny-(dn-1)*accd];                                       
                elif nx>=dn*accd-accd/2+1:
                    if ny<=accd/2:
                        fdpsf[nx,ny]=fpsf[nx-(dn-1)*accd,ny];
                    elif ny>=dn*accd-accd/2 +1:
                        fdpsf[nx,ny]=fpsf[nx-(dn-1)*accd,ny-(dn-1)*accd];  
    else:
        for nx in range(0,accd*dn):
            for ny in range(0,accd*dn):
                if nx<=math.ceil(accd/2) -1:
                    if ny<=math.ceil(accd/2)-1:
                        fdpsf[nx,ny]=fpsf[nx,ny];
                    elif ny>= dn*accd-math.floor(accd/2):
                        fdpsf[nx,ny]=fpsf[nx,ny-(dn-1)*accd];                                       
                elif nx>=dn*accd-math.floor(accd/2):
                    if ny<=math.ceil(accd/2)-1:
                        fdpsf[nx,ny]=fpsf[nx-(dn-1)*accd,ny];
                    elif ny>=dn*accd-math.floor(accd/2):
                        fdpsf[nx,ny]=fpsf[nx-(dn-1)*accd,ny-(dn-1)*accd];
#        fpsf2=np.fft.fftshift(fpsf)
#        fdpsf2=np.zeros((accd*dn,accd*dn))
#        for nx in range(0,accd*dn-1):
#            for ny in range(0,accd*dn-1):    
#                if nx >=-(accd-1)/2+math.ceil(dn/2*accd) and nx<(accd-1)/2+math.ceil(dn/2*accd)+1:
#                    if ny >=-(accd-1)/2+math.ceil(dn/2*accd) and ny<(accd-1)/2+math.ceil(dn/2*accd)+1:       
#                        print(nx-math.ceil((dn-1)*accd/2))
#                        fdpsf2[nx,ny]=fpsf2[nx-math.ceil((dn-1)*accd/2),ny-math.ceil((dn-1)*accd/2)];
#        fdpsf=np.fft.ifftshift(fdpsf2)
    return fdpsf

def PsfDensefy(psf,dn): 
    #step 1 FFT
    fpsf=np.fft.fft2(psf)
    # dn put 0 in 
    fdpsf=PutZeros(fpsf,dn)
    dpsf=np.fft.ifft2(fdpsf)*dn*dn
    return dpsf


if __name__=='__main__':   
    start =time.perf_counter()
    #test code 
#    a=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16] ])
    a=np.array([[1,2,3],[4,5,6],[7,8,9]])
    b=PutZeros(a,3)
    print(b)
    seconds=time.perf_counter()-start
    print('It took {:.2f} seconds.'.format(seconds))