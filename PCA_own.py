# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 11:25:07 2020

@author: anyaj
"""
import numpy as np
from PIL import Image
import PCA2
import cv2

img = cv2.imread('images/skyex.jpg')
img2 = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
array = np.array(img2)
print(array.shape) 
#print(array)

V,S,immean = PCA2.pca(array)




