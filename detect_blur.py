# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 12:22:03 2020

@author: anyaj
"""


# import the necessary packages
#from imutils import paths
#import numpy as np
import argparse
import cv2
import matplotlib.pyplot as plt
import imutils



def variance_of_laplacian(image):
	# compute the Laplacian of the image and then return the focus
	# measure, which is simply the variance of the Laplacian
	return cv2.Laplacian(image, cv2.CV_64F).var()
# construct the argument parse and parse the arguments
#ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--images", required=True,
	#help="path to input directory of images")
#ap.add_argument("-t", "--threshold", type=float, default=100.0,
	#help="focus measures that fall below this value will be considered 'blurry'")
#args = vars(ap.parse_args())


# loop over the input images
#for imagePath in paths.list_images(args["images"]):

#ROI_polygon.draw_roi
#cv2.imshow("img", image)
#plt.imshow(image)
#b, g, r = cv2.split(image)
#img2 = cv2.merge([r, g, b])
#img = imutils.resize(image, width=500)


#
#ROI = image[(14, 114), (119, 27), (345, 50), (406, 179), (294, 256), (133, 270), (77, 214), (34, 232), (12, 118)]
#plt.imshow(ROI)
  
def blur(dst_roi, src_roi, image):
    dst_grey = cv2.cvtColor(dst_roi, cv2.COLOR_BGR2GRAY)
    src_grey = cv2.cvtColor(src_roi, cv2.COLOR_BGR2GRAY)
    dst_fm = variance_of_laplacian(dst_grey)
    src_fm = variance_of_laplacian(src_grey)
    perc_diff_fm=((dst_fm-src_fm)/dst_fm)*100
    #text = "Not Blurry"
    
        # if the focus measure is less than the supplied threshold,
    	# then the image should be considered "blurry"
    if src_fm < dst_fm:
        text = "more"
    else :
        perc_diff_fm=-perc_diff_fm
        text = "less"
    	# show the image
    #cv2.putText(image, "Boundary on original image: {:.0f} \n, Suspected boundary: {:.0f} , {}".format(dst_fm, src_fm, text), (10, 30),
    #cv2.FONT_HERSHEY_COMPLEX, 0.1, (0, 0, 255), 3, 1)
    #image = imutils.resize(image, width=500)
    #cv2.imshow("Image",image)
    #cv2.waitKey(0)
    print("Boundary on original image: {:.0f} \nSuspected boundary: {:.0f} \nSuspected boundary is {:.0f}% {} blurry than the boundary on orginal object".format(dst_fm, src_fm, perc_diff_fm, text))

if __name__ == '__blur__': 
     blur()
#run function  
#image = cv2.imread("images/fish.jpg")
#ROI = image[100:500, 200:850]
#blur(ROI)
#blur(ROI)
