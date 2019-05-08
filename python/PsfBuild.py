#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 18:07:49 2019

this program is used to build PSF 

@author: kingpc
"""

import os,sys
import time
import  math
import numpy as np
from tkinter import filedialog
import matplotlib.pyplot as plt
from scipy.special import j1 as J1
import scipy

def GaussianFunc(sig,size,cx,cy):
    x = np.linspace(1, size, size)
    y = np.linspace(1,size, size)
    X,Y = np.meshgrid(x,y)  
    out=math.e**( -1*((X-cx)**2+(Y-cy)**2 )/2/sig/sig )
    return out

def GaussianFunce(sigx,sigy,thetax,size,cx,cy):
    a=(math.cos(thetax))**2/(2*sigx**2)+(math.sin(thetax))**2/(2*sigy**2)
    b=-1*(math.sin(thetax*2))/(4*sigx**2)+(math.sin(thetax*2))/(4*sigy**2)
    c=(math.sin(thetax))**2/(2*sigx**2)+(math.cos(thetax))**2/(2*sigy**2)
    x = np.linspace(1, size, size)
    y = np.linspace(1,size, size)
    X,Y = np.meshgrid(x,y)  
    out=math.e**(-1*(a*(X-cx)**2+2*b*(X-cx)*(Y-cy)+c*(Y-cy)**2 ))
    return out

def AiryFunc(rn,size,cx,cy):
    a=1/rn
    N=size
    x = np.linspace(1, size, size)
    y = np.linspace(1,size, size)
    X,Y = np.meshgrid(x,y) 
    out=(4*(scipy.special.jn(1,((X-(N/2+1))**2+(Y-(N/2+1))**2)**0.5*a*math.pi)
           /(((X-(N/2+1))**2+(Y-(N/2+1))**2)**0.5*a*math.pi))**2)
    if cx/2==int(cx/2) and cy/2==int(cy/2):
        out[int(N/2),int(N/2)]=1
    return out

def MoffatFunc( size,alp,bet ,cx,cy ):
    #bet=2.5 4.675 4
    x = np.linspace(1, size, size)
    y = np.linspace(1,size, size)
    X,Y = np.meshgrid(x,y)    
    out=(bet-1)/(math.pi*alp**2)* (1+(((X-cx)**2+(Y-cy)**2)/(alp**2) ))**(-bet)
    return out 

def SersicFunc( size,Re,n,cx,cy ):
    #bet=2.5 4.675 4
    b=2*n-1/3#7.669
    Ie=0.5
    x = np.linspace(1, size, size)
    y = np.linspace(1,size, size)
    X,Y = np.meshgrid(x,y)    
    out= Ie*math.e**( ( ( (  ((X-cx)**2+(Y-cy)**2)**0.5)/Re)**(1/n)-1)*-b)
    return out 


if __name__=='__main__':   
    start =time.perf_counter()
#    PSF=GaussianFunc(5,5,0,100,50,50  )
#    PSF=AiryFunc(20,100,50,50)
    PSF=MoffatFunc(100,20,2.5,50,50)
#    PSF=SersicFunc(100,5,1,50.5,50.5) 
    plt.imshow(PSF,cmap=plt.cm.viridis)
    plt.colorbar()
    plt.show()   
    seconds=time.perf_counter()-start
    print('It took {:.2f} seconds.'.format(seconds))