# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 13:25:15 2020

@author: anyaj
"""
import cv2

# read image
img1 = cv2.imread("images/SC-images/genuine/skyscrapers.jpg")

def ELA(img1):
# set compression and scale
    jpg_quality1 = 95
    jpg_quality2 = 90
    scale = 15
    
    # write img1 at 95% jpg compression
    temp95="images/temps/temp95.jpg"
    cv2.imwrite(temp95, img1, [cv2.IMWRITE_JPEG_QUALITY, jpg_quality1])
                
    # read compressed image
    img2 = cv2.imread(temp95)
    
    # get absolute difference between img1 and img2 and multiply by scale
    
    diff1 = scale * cv2.absdiff(img1, img2)
    cv2.imwrite("images/temps/diff1.jpg", diff1)
                
    # write img2 at 90% jpg compression
    temp90="images/temps/temp90.jpg"
    cv2.imwrite(temp90, img2, [cv2.IMWRITE_JPEG_QUALITY, jpg_quality2])
                
    # read compressed image
    img3 = cv2.imread(temp90)
    
    # get absolute difference between img1 and img2 and multiply by scale
    diff2 = scale * cv2.absdiff(img2, img3)
    cv2.imwrite("images/temps/diff2.jpg", diff2)
    # display it
    cv2.imshow("ela95", diff1)
    cv2.imshow("ela90", diff2)
    cv2.waitKey(0)
    
    
if __name__ == '__ELA__': 
    ELA()

#ELA(img1)