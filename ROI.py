# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 14:28:09 2020

@author: anyaj
"""
import cv2
import imutils
from matplotlib import pyplot as plt
import detect_blur
 
img = cv2.imread("images/penguins_trekkers.jpg")
img = imutils.resize(img, width=500)
 
roi = cv2.selectROI(windowName="roi", img=img, showCrosshair=True, fromCenter=False)
x, y, w, h = roi
 
img2=img.copy()
cv2.rectangle(img=img2, pt1=(x, y), pt2=(x + w, y + h), color=(0, 0, 255), thickness=2)
cv2.imshow("roi", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

ROI=img[y:y+h, x:x+w]

#print(x, x+w, y, y+h)
#cv2.imshow('roi', ROI)
#cv2.imshow('roi', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


detect_blur.blur(ROI,img)




