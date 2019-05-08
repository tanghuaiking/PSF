#!/usr/bin/python
#from ftplib import FTP
import sys
#import socket
#import pdb
from photutils.datasets import make_4gaussians_image
from photutils import centroid_com, centroid_1dg, centroid_2dg
import matplotlib.pyplot as plt
from photutils import data_properties
from numpy import *  
#accd=32 #k5 14  #k10 26#rn1 8#rn2 14
def psfpy(data):
    x1, y1 = centroid_com(data)
    x2, y2 = centroid_1dg(data)
    x3, y3 = centroid_2dg(data)
#    print(data)
#    print(x1,y1,x2,y2,x3,y3)
#    mean, median, std = sigma_clipped_stats(data, sigma=3.0, iters=5)
#    data -= median    # subtract background
    cat = data_properties(data)
#        print (cat)
#列输出
    columns = ['id', 'xcentroid','ycentroid','semimajor_axis_sigma','semiminor_axis_sigma','orientation','cxx','cyy','cxy','eccentricity']
    tbl = cat.to_table(columns=columns)
    tbl['cxy'].info.format = '.10f'
    eccef=float(tbl['eccentricity'])
    str1=str(tbl['semimajor_axis_sigma'])
    semimajorf=str1.split("[")[1].split("]")[0]
    str1=str(tbl['semiminor_axis_sigma'])
    semiminorf=str1.split("[")[1].split("]")[0]
    str1=str(tbl['orientation'])
    orientationf=str1.split("[")[1].split("]")[0]
    str1=str(tbl['cxx'] )
    cxxf=str1.split("[")[1].split("]")[0]
    str1=str(tbl['cxy'] )
    cxyf=str1.split("[")[1].split("]")[0]
    str1=str(tbl['cyy'])
    cyyf=str1.split("[")[1].split("]")[0]
    return(x1,y1,x2,y2,x3,y3,semimajorf,semiminorf,eccef,orientationf,cxxf,cxyf,cyyf)

if __name__=='__main__':    
    N=100
    x = np.linspace(1, N, N)
    y = np.linspace(1,N, N)
    X,Y = np.meshgrid(x,y)
    sigx=5
    kab=1.1
    sigy=kab*sigx    
    psf=math.e**(-(X-(N/2+1))**2/(sigx**2))*math.e**(-(Y-(N/2+1))**2/(sigy**2))
    [x1,y1,x2,y2,x3,y3,semimajorf,semiminorf,eccef,orientationf,cxxf,cxyf,cyyf]=psfpy(psf)
    kab=float(semimajorf)/float(semiminorf)
    print(x1,y1,x2,y2,x3,y3,kab,orientationf)