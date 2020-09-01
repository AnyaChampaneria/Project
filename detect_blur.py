# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 12:22:03 2020

@author: anyaj
"""


# import the necessary packages
import cv2

def variance_of_laplacian(image):
	# compute the Laplacian of the image and then return the focus
	# measure, which is simply the variance of the Laplacian
	return cv2.Laplacian(image, cv2.CV_64F).var()

  
def blur(dst_roi, src_roi, image):
    #create grreyscale versions
    dst_grey = cv2.cvtColor(dst_roi, cv2.COLOR_BGR2GRAY)
    src_grey = cv2.cvtColor(src_roi, cv2.COLOR_BGR2GRAY)
    dst_fm = variance_of_laplacian(dst_grey)
    src_fm = variance_of_laplacian(src_grey)
    perc_diff_fm=((dst_fm-src_fm)/dst_fm)*100
    
    if perc_diff_fm<20:
        text = "{:.0f}% - GREEN: Percentage difference is not large enough to suggest cloning".format(perc_diff_fm)
    
    elif 20<perc_diff_fm<100:
        text = "{:.0f}% - AMBER: Percentage difference is large enough to cause concern, possible cloning present".format(perc_diff_fm)


    elif perc_diff_fm>100:
        text = "{:.0f}% -RED: Percentage difference is very large, it is likely there is cloning in this image"
    
    print(text)

if __name__ == '__blur__': 
     blur()

#run function  
#blur(ROI)

