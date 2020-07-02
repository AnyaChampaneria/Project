# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 15:08:24 2020

@author: anyaj
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread("flower.jpg",1)
#cv2.imwrite("flowercopy.jpg", img)
#cv2.imshow('Flower Image',img)
#plt.imshow(img)
#flip colour order to RGB
b, g, r = cv2.split(img)
img2 = cv2.merge([r, g, b])
plt.imshow(img2)
#another way to do this is
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

# If we want to get the dimensions of the image we use img.shape
# It will tell us the number of rows, columns, and channels 
dimensions = img.shape
print(dimensions)

# We can obtain a total number of elements by using img.size
total_number_of_elements= img.size
print(total_number_of_elements)

# Image data type is obtained by img.dtype
image_dtype = img.dtype
print(image_dtype)

# To get the value of the pixel (x=50, y=50), we would use the following code
(b, g, r) = img[50, 50]
print("Pixel at (50, 50) - Red: {}, Green: {}, Blue: {}".format(r,g,b))

# We changed the pixel color to red
img[50, 50] = (0, 0, 255)

# Displaying updated image
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Updated')

# Using indexing we modified a whole region rather than one pixel
# For the top-left corner of the image, we can rewrite 
# the color channels in folowing way:
img[0:150, 0:300] = [0,255,0]
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Updated')

#cv2.imshow("flower", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
