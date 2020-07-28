# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 12:04:37 2020

@author: anyaj
"""
from PIL import Image
import numpy as np
import pylab as py
import PCA2
import cv2

im = cv2.imread("images/fish.jpg") # open one image to get size
m,n = im.shape[0:2] # get the size of the images
#imnbr = len(imlist) # get the number of images

# create matrix to store all flattened images
imflat = Image.open(im).flatten()

# perform PCA
V,S,immean = PCA2.pca(imflat)

# show some images (mean and 7 first modes)
py.figure()
py.gray()
py.subplot(2,4,1)
py.imshow(immean.reshape(m,n))
for i in range(7):
  py.subplot(2,4,i+2)
  py.imshow(V[i].reshape(m,n))

py.show()

