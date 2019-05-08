#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 20:28:35 2019

display deconvolution

@author: kingpc
"""
import os,sys
import time
import  math
import numpy as np
from numpy.fft import fft,ifft,fft2,ifft2,ifftshift,fftshift
from PsfBuild import *
import galsim

#step 1 conv

#galaxy parameter
#def run():
    sigx=10
    sigy=1.25*sigx
    theta=0
    size=4000
    cx=size/2
    cy=size/2
    Galaxy=GaussianFunc(sigx,sigy,thetax,size,cx,cy)

    sigx=100/(0.5/3)*1/2/math.pi#
    sigy=1*sigx
    theta=0
    size=4000
    cx=size/2
    cy=size/2
    PSF=GaussianFunc(sigx,sigy,thetax,size,cx,cy)



      
#    return 

#step 2 : deconv & densfy deconv

if __name__=='__main__':   
    start =time.perf_counter()
    
    run
    sersic_obj1 = galsim.Sersic(n=3.5, half_light_radius=2.5, flux=40.)
    print(sersic_obj1.xValue(galsim.PositionD(0.,0.)))    
    
    
    seconds=time.perf_counter()-start
    print('It took {:.2f} seconds.'.format(seconds))
