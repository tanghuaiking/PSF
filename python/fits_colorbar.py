#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 20:16:29 2019

@author: kingpc
"""
import sys
import os
import math
import logging
import galsim
import time
import matplotlib.pyplot as plt
from astropy.io import fits


hdulist = fits.open('output/demo1.fits')   
data=hdulist[0].data
plt.imshow(data,cmap=plt.cm.viridis)
plt.colorbar()
plt.show()