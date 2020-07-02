# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 15:59:45 2020

@author: anyaj
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
#gray = np.zeros((256,256), dtype="uint8")

#for i in range(255):
 # for j in range(255):
    #gray[i,j]= (i*0.5 + j*0.5)
    #gray[i,:]=i
    #gray=r.astype("uint8")
   # plt.imshow(gray)
   # cv2.waitKey(10)
    
r = np.zeros((256,256),dtype="uint8")
g = np.zeros((256,256),dtype="uint8")
b = np.zeros((256,256),dtype="uint8")

for i in range(255):
  for j in range(255):
    r[i,j]= (i*0.5 + j*0.5)
    g[i,j]= i
    b[i,j]= 0

r=r.astype("uint8")
g=g.astype("uint8")
b=b.astype("uint8")

img = cv2.merge( (r,g,b) )    
plt.imshow(img)
print('Maximum RGB value in this image {}'.format(img.max()))
print('Minimum RGB value in this image {}'.format(img.max()))

print('Maximum R value in this image {}'.format(r.max()))
print('Maximum B value in this image {}'.format(b.max())) 
print('Maximum G value in this image {}'.format(g.max()))
print('Minimum R value in this image {}'.format(r.min()))
print('Minimum B value in this image {}'.format(b.min())) 
print('Minimum G value in this image {}'.format(g.min()))
    
#print(gray)