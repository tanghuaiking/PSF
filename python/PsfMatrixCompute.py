#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 10:08:37 2018

@author: kingpc
"""
import  math
from numpy import *  
import numpy as np
from numpy.fft import fft,ifft,fft2,ifft2,ifftshift,fftshift
from tkinter import filedialog
import matplotlib.pyplot as plt
from PsfBuild import GaussianFunc
import time

class Location:
    def __init__(self,x,y):  #定义psf的位置，即平面上的一点，用x和y坐标表示
        self.x=x
        self.y=y
    def move(self,xc,yc):  #输入x和y坐标的变动值，返回变动后的坐标
        return Location(self.x+xc,self.y+yc)
    def getLocation(self):
        return self.x,self.y
    def getDistance(self,other):  #输入另一个点的坐标，根据x轴和y轴变动的距离，算出原点和另一个点之间的直线距离
        ox,oy=other.getLocation()
        xDist=ox-self.x
        yDist=oy-self.y
        return math.sqrt(xDist**2+yDist**2)
    
        

   
    
class PsfMatrix: 
    def __init__(self,psf): 
        self.psf=psf
        
    def centroid(psf):
        N=len(psf[0,:])
        lx=0
        for nx in range(0,N):
            lx=lx+(nx+1)*sum(psf[nx,:])
        ly=0    
        for ny in range(0,N):
            ly=ly+(ny+1)*sum(psf[:,ny])   
        cx=lx/sum(sum(psf))
        cy=ly/sum(sum(psf))
        return [cx,cy]
#use for compute the second Moment of PSF matrix
    def secondMoment(psf,cx,cy):
        accd=len(psf[0,:])
        Q11=0
        Q22=0
        Q12=0
        for nx in range(0,accd):
            for ny in range(0,accd):
                deltax=(cx-(nx+1))
                deltay=(cy-(ny+1))
                Q11= psf[nx,ny]*(deltax)**2+Q11 
                Q22= psf[nx,ny]*(deltay)**2+Q22
                Q12= psf[nx,ny]*(deltax)*(deltay)+Q12    
        T=Q11+Q22;
        e_plus=(Q11-Q22)/T;
        e_x=2*Q12/T;
        return [e_plus,e_x]  
# use for convert e+ ex to kab and theta
    def epex2kabtheta(ep,ex):
        e_plus_ort= math.sqrt(ex**2+ep**2)
        if ep>=0:
            kab_w=1/(math.sqrt((1-e_plus_ort)/(1+e_plus_ort)))
        else:
            kab_w=(math.sqrt((1-e_plus_ort)/(1+e_plus_ort))) 
        theta_w= math.atan((ex/ep))/2  
        return [kab_w,theta_w]
    
#def GaussianWeight(psf,sigx,kabw,thetaw,cx,cy):
#    size=len(psf[0,:])
#    wf=GaussianFunc(sigx,kabw*sigx,thetaw,size,cx,cy)
#    psfw=psf*wf
#    return psfw 

def GaussianWeightn(psf,sigx):
    N=len(psf[0,:]);
    kw=1
    kab_w=1
    theta_w=0
    bx=N/2
    by=N/2
    sigxw=kw*sigx
    for nn in range(0,30):
        psfw=psf*GaussianFunc(sigxw,kab_w*sigxw,theta_w,N,bx,by)
#        GaussianWeight(psf,sigxw,kab_w,theta_w,bx,by)
        [bx,by]=PsfMatrix.centroid(psfw)
        [ep,ex]=PsfMatrix.secondMoment(psfw,bx,by)
        [kab_w,theta_w]=PsfMatrix.epex2kabtheta(ep,ex)
    return [bx,by,kab_w,theta_w]
    
    
if __name__=='__main__':    
    start =time.perf_counter()
    N=30
    x = np.linspace(1, N, N)
    y = np.linspace(1,N, N)
    X,Y = np.meshgrid(x,y)
    sigx=3
    kab=1.3
    sigy=kab*sigx    
#    psf=math.e**(-(X-(N/2+1))**2/(sigx**2))*math.e**(-(Y-(N/2+1))**2/(sigy**2))
    cx=N/2+1
    cy=N/2+1
    thetax=0.2
    size=N
    psf=GaussianFunc(sigx,sigy,thetax,size,cx,cy)
    #
    [bx,by]=PsfMatrix.centroid(psf)
    [ep,ex]=PsfMatrix.secondMoment(psf,bx,by)
    [kab_w,theta_w]=PsfMatrix.epex2kabtheta(ep,ex)
    print(bx,by,kab_w,theta_w)
    # compute with weight

    [bx,by,kab_w,theta_w]=GaussianWeightn(psf,sigx)
    print(bx,by,kab_w,theta_w)
    
    seconds=time.perf_counter()-start
    print('It took {:.2f} seconds.'.format(seconds))
    
    plt.imshow(psf,cmap=plt.cm.viridis)
    plt.colorbar()
    plt.show()   
    
    