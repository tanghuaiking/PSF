#!/usr/bin/python
#from ftplib import FTP
#import sys
#import socket
#import pdb
from photutils.datasets import make_4gaussians_image
from photutils import centroid_com, centroid_1dg, centroid_2dg
import matplotlib.pyplot as plt
from photutils import data_properties
from numpy import *  
#accd=32 #k5 14  #k10 26#rn1 8#rn2 14


for kp in range(1,6):
    for sg in range(1,6):
        sgs=str((sg+12))
        for nn in range(1,101):
            nums=str((nn))
            if kp==1:
                accd=150
            elif kp==2:
                accd=134
            elif kp==3:
                accd=120
            elif kp==4:
                accd=110
            else:
                accd=100
            A = zeros((accd,accd),dtype=float)    #先创建一个全零方阵A，并且数据的类型设置为float浮点型  
            B = zeros((accd,accd),dtype=float) 
            kps=str((kp+7))
#db='0.'+str(8)	
            file_str = 'psf_ag_'+kps+'_'+sgs+'_'+nums+'.txt'
#print(file_str)
            f = open(file_str)               #打开数据文件文件  
            lines = f.readlines()           #把全部数据文件读到一个列表lines中  
            A_row = 0                       #表示矩阵的行，从0行开始  
            for line in lines:              #把lines中的数据逐行读取出来  
                list = line.strip('\n').split(' ')      #处理逐行数据：strip表示把头尾的'\n'去掉，split表示以空格来分割行数据，然后把处理后的行数据返回到list列表中  
#    print(list)
                A[A_row:] = list[0:accd]                   
#把处理后的数据放到方阵A中。list[0:3]表示列表的0,1,2列数据放到矩阵A中的A_row行  
                A_row+=1                                #然后方阵A的下一行接着读  
    #print(line)  

  
#print(A[0])    #打印 方阵A里的数据 
#            for i in range(1,101):
#                for j in range(1,accd+1):
#                    B[j-1]=A[(i-1)*accd+j-1]
#                    print(B[j-1])
            data =A
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

            file_out = 'astrp_ag_' +kps+'_'+sgs+'.txt'
            f=open(file_out ,'a')
#            f.write( '%s,%s,%s,%s,%s,%s' % (x1,y1,x2,y2,x3,y3))
#        f.write( '%s ' % (eccef))
            f.write( '%s,%s,%s,%s,%s,%s,%s,%s,%f,%s,%s,%s,%s' %(x1,y1,x2,y2,x3,y3,semimajorf,semiminorf,eccef,orientationf,cxxf,cxyf,cyyf))
            f.write('\n')
            f.close()#!/usr/bin/python
