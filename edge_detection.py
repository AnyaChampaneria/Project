# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 16:28:28 2020

@author: anyaj
"""
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread("images/flower.jpg")


#edges = cv.Canny(img,100,200)
#plt.subplot(121),plt.imshow(img,cmap = 'gray')
#plt.title('Original Image'), plt.xticks([]), plt.yticks([])
#plt.subplot(122),plt.imshow(edges,cmap = 'gray')
#plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
#plt.show()

imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

#To draw all the contours in an image:
#cnt = contours[4]
#cv.drawContours(img, [cnt], 0, (0,255,0), 3)
cv.drawContours(img, contours,-1, (0,255,0), 3)
cv.imshow('draw contours',img)
cv.waitKey(0)

print(cv.CHAIN_APPROX_NONE)

#cv.imshow(img)
#To draw an individual contour, say 4th contour:
#cv.drawContours(img, contours, 3, (0,255,0), 3)
#But most of the time, below method will be useful:
