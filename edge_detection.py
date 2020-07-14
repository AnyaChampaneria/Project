# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 16:28:28 2020

@author: anyaj
"""
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread("images/fish.jpg")

imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(imgray, (5,5), 0)
ret, thresh = cv.threshold(blur, 127, 255, 0)
edges = cv.Canny(thresh,180,250)
#plt.subplot(121),plt.imshow(img,cmap = 'gray')
#plt.title('Original Image'), plt.xticks([]), plt.yticks([])
#plt.subplot(122),plt.imshow(edges,cmap = 'gray')
#plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
#plt.show()

imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(imgray, (5,5), 0)

print(edges)
contours, hierarchy = cv.findContours(edges, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

#To draw all the contours in an image:
#cnt = contours[4]
#cv.drawContours(img, [cnt], 0, (0,255,0), 3)
#for( int i = 0; i< contours.size(); i++ )
#cv.drawContours(thresh, contours,i, (0,255,0),0, 8, hierarchy ); 
     
     
cv.drawContours(img, contours,-1, (0,255,0), 3)
cv.imshow('draw contours',img)
cv.waitKey(0)

#print(cv.CHAIN_APPROX_NONE)

#cv.imshow(img)
#To draw an individual contour, say 4th contour:
#cv.drawContours(img, contours, 3, (0,255,0), 3)
#But most of the time, below method will be useful:


