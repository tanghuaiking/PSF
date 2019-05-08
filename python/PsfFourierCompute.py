#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 20:15:30 2019
Fourier compute 

@author: kingpc
"""

import os,sys
import time
import  math
import numpy as np
from numpy.fft import fft,ifft,fft2,ifft2,ifftshift,fftshift
from PsfBuild import *
from PsfMatrixCompute import *

def Angle(a):
    return math.atan(a.imag/a.real)

def FourierPosition(psfw,accd,dn):
    fz2=fft2(re_dw)
    absfz=abs(fz2)
    
    angfz=Angle(fz2)
    
    funx=0     
    funy=0 
    for m in range(1,accd*dn/2):
        funxn=2*absfz(m,1) *(sin((m-1)*2*pi+(angfz(m,1)-(1/accd*(m-1)*2*pi))))
           /((m-1)/accd*2*pi);%    * (-1*sin(((angfz(m,n)-angfz(accd+1-m,n))/2)) )   
        funyn=2*absfz(1,m) *(sin((m-1)*2*pi+(angfz(1,m)-(1/length(y)*(m-1)*2*pi))))
           /((m-1)/accd*2*pi);%    * (-1*sin(((angfz(m,n)-angfz(accd+1-m,n))/2)) )   
        funx=funx+funxn;
        funy=funy+funyn;
    bx_w2=(funx)/absfz(1,1);
    by_w2=(funy)/absfz(1,1);
    bx_w=accd/2+bx_w2;
    by_w=accd/2+by_w2;
    
    funxx=0
    funyy=0
    cx=bx_w
    cy=by_w
    for m in range(1,accd*dn/2):
        funxxn=(    (accd-cx)**2-cx**2)*2*absfz(m,1) *(sin((angfz(m,1)-(1/accd*(m-1)*2*pi))))/((m-1)/accd*2*pi)+...   
               (accd)*2*absfz(m,1) *(cos((angfz(m,1)-(1/accd*(m-1)*2*pi))))/((m-1)/accd*2*pi)**2*2 ;
        funyyn=((accd-cy)**2-cy**2)*2*absfz(1,m) *(sin((angfz(1,m)-(1/accd*(m-1)*2*pi))))/((m-1)/accd*2*pi)+...
          (accd)*2*absfz(1,m) *(cos((angfz(1,m)-(1/accd*(m-1)*2*pi))))/((m-1)/accd*2*pi)**2*2;
        funxx=funxx+funxxn;
        funyy=funyy+funyyn;
 
    funxx=funxx+(accd**3/3-cx*accd^2+cx**2*accd)*absfz(1,1)
    funyy=funyy+(accd**3/3-cy*accd^2+cy**2*accd)*absfz(1,1)
    T=funxx+funyy;
    e_plus=abs(funxx-funyy)/T;
    
    funxy=0  
    for m=2:(accd*dn)/2
        for n=2:(accd*dn)/2
            funxyn=2*(absfz(m,n)-absfz(accd*dn-m+2,n))*(accd)^2
                 *( cos(((angfz(m,n)+angfz(m,accd*dn-n+2))/2-1/(accd)*2*pi*(m-1) ))/((m-1)/(accd)*2*pi)*...
               cos(((angfz(m,n)-angfz(m,accd*dn-n+2))/2-1/(accd)*2*pi*(n-1) ))/((n-1)/(accd)*2*pi))   
            funxy=funxy+funxyn
    e_x=2*funxy/T/accd;
    e_plus_ort=math.sqrt(e_x^2+e_plus^2);
    [kab_w,theta_w]=exep2kabtheta(e_x,e_plus);

    return [bx_w2,by_w2,kab_w,theta_w]


if __name__=='__main__':   
    start =time.perf_counter()
    
    
    seconds=time.perf_counter()-start
    print('It took {:.2f} seconds.'.format(seconds))