#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 16:10:20 2018

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

da=0
for nn in range(0,1000): 
    dd=1/(2**nn)*1e-4
    b1=abs(scipy.special.jn(1,3.8317+da-dd))
    b2=abs(scipy.special.jn(1,3.8317+da+dd))
#    print(b1,b2)
    if b1>=b2:
        da=da+dd
    else:
        da=da-dd