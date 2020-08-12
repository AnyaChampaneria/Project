# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 14:28:09 2020

@author: anyaj
"""
import cv2
#import imutils
#from matplotlib import pyplot as plt
import detect_blur
import ELA_opencv
#import PCA3
 
#img = cv2.imread("images/SC-images/made/SC_plantonwindow.jpg")
#img = imutils.resize(img, width=500)

#PCA3.pca(img)
#ELA_opencv.ELA(img)



def roi(img):
    roi = cv2.selectROI(windowName="roi", img=img, showCrosshair=True, fromCenter=False)
    x, y, w, h = roi
    global img2
    img2=img.copy()
    cv2.rectangle(img=img2, pt1=(x, y), pt2=(x + w, y + h), color=(0, 0, 255), thickness=2)
    cv2.imshow("roi", img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    global ROI
    ROI=img[y:y+h, x:x+w]
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__roi__':
    roi()

#print("Draw a box on a border in the original object in image (try to get half of the object and half the background using the cross-hair as a guide)")
#roi(img)
#dst_roi=ROI

#print("Draw a box the same size on a border in the suspected object image (try to get half of the object and half the background using the cross-hair as a guide)")
#roi(img2)
#src_roi=ROI


#detect_blur.blur(dst_roi, src_roi, img)




