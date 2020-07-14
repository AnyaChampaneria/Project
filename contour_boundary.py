# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 15:47:42 2020

@author: anyaj
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.pyrDown(cv2.imread("images/fish.jpg", cv2.IMREAD_UNCHANGED))
#img=image[100:275, 150:300]
#img =  image[40:100, 150:275]
#img2 = img.copy()
img=image
#plt.imshow(img)

ret, thresh = cv2.threshold(cv2.cvtColor(img.copy(), cv2.COLOR_BGR2GRAY) , 127, 255, cv2.THRESH_BINARY)
contours, hier = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


#cv2.waitKey(0)
#cv2.destroyAllWindows()
for c in contours:
# find bounding box coordinates
    x,y,w,h = cv2.boundingRect(c)
    cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2)

# find minimum area
rect = cv2.minAreaRect(c)
# calculate coordinates of the minimum area rectangle
box = cv2.boxPoints(rect)
# normalize coordinates to integers
box = np.int0(box)
# draw contours
cv2.drawContours(img, [box], 0, (0,0, 255), 3)
# calculate center and radius of minimum enclosing circle
(x,y),radius = cv2.minEnclosingCircle(c)
# cast to integers
center = (int(x),int(y))
radius = int(radius)
# draw the circle
img = cv2.circle(img,center,radius,(0,255,0),2)
#epsilon = 0.01 * cv2.arcLength(contours, True)
#approx = cv2.approxPolyDP(contours, epsilon, True)
#hull = cv2.convexHull(approx)

cv2.drawContours(img, contours, -1, (255, 0, 0), 1)
cv2.imshow("contours", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

