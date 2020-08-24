# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 10:34:15 2020

@author: anyaj
"""
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread("images/temps/diff1.jpg")


#img_copy = img.copy()

#non_black=[img_copy != 0]
 
# change everything to white where pixel is not black
#cv2.imwrite('my_img2.jpeg', img)

#cv.imshow('img', img)
#cv.waitKey(0)
#plt.show()

lower_black = np.array([0, 0, 0], np.uint8)
upper_black = np.array([15,15,15], np.uint8)

#bl_img = img[np.all(BLUE_MIN<img<BLUE_MAX)] = (255,255,255)
#plt.imshow(bl_img)

black_mask = cv.inRange(img, lower_black, upper_black)
cv.imshow('mask0',black_mask)
cv.waitKey(0)

dst = cv.inRange(img, lower_black, upper_black)
non_black = cv.countNonZero(dst)
print(non_black)

#count = cv.countNonZero(img)
#print(count)
print(img.size)

perc_non_black=(non_black/img.size)*100
print(perc_non_black)


