# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 17:04:26 2020

@author: anyaj
"""


import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread("flower.jpg",1)

b, g, r = cv2.split(img)
b = img[:,:,0]
img2 = cv2.merge([r, g, b])
plt.imshow(img2)
#plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

#flowercentre = img[300:350, 125:175]
#img[50:100, 125:75] = flowercentre