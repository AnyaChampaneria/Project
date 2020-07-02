# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 15:32:03 2020

@author: anyaj
"""

# import the necessary packages
import numpy as np
import argparse
import cv2
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image file")
ap.add_argument("-r", "--radius", type = int,
	help = "radius of Gaussian blur; must be odd")
args = vars(ap.parse_args())
# load the image and convert it to grayscale
image = cv2.imread("flower.jpg")
#orig = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# perform a naive attempt to find the (x, y) coordinates of
# the area of the image with the largest intensity value

# display the results of the naive attempt
#cv2.imshow("Naive", image)
# apply a Gaussian blur to the image then find the brightest
# region
gray = cv2.GaussianBlur(gray, (5,5), 0)
(minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)
#image = orig.copy()
cv2.circle(image, maxLoc, 5, (255, 0, 0), 2)
cv2.circle(image, minLoc, 5, (255, 0, 0), 2)
# display the results of our newly improved method
cv2.imshow("Robust", image)
cv2.waitKey(0)

