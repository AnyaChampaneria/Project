# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 17:04:26 2020

@author: anyaj
"""


import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread("images/tree.png",1)


b, g, r = cv2.split(img)
#b = img[:,:,0]
img2 = cv2.merge([r, g, b])
#ptl.imshow(img2)
#plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
#cv2.imshow("flower", img)
flowercentre = img2[135:185, 300:350]
img2[135:185, 50:100] = flowercentre
print (img2[100,100])
blue = img2[100,100,0]
print (blue)
#cv2.imshow("fowercentre repeat", img2)
 # full intensity to those pixel's R channel
img[50:100 , : , 0] = 255
img[150:200 , : , 1] = 255
img[250:300 , : , 2] = 255 
img[ 50:450 , 400:600 , [0,1,2] ] = 200

cv2.imshow("line",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
#plt.imshow(img2[125:175, 300:350,])

#convert to hsv
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
print(hsv[...,2].mean())


#plt.show()