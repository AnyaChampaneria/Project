# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 16:55:10 2020

@author: anyaj
"""
import detect_blur
import cv2


def roi(img):
    roi = cv2.selectROI(windowName="roi", img=img, showCrosshair=True, fromCenter=False)
    global x,y,w,h
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
    
def db_roi(image):
     print("Draw a box on a border in the original object in image (try to get half of the object and half the background using the cross-hair as a guide)")
     # QMessageBox.information(self,'Instructions','Draw a box on a border in the original object in image (try to get half of the object and half the background using the cross-hair as a guide)')  
     roi(image)
     global dst_roi
     dst_roi=ROI  
        
     print("Draw a box the same size on a border in the suspected object image (try to get half of the object and half the background using the cross-hair as a guide)")
     #QMessageBox.information(self,'Instructions','Draw a box the same size on a border in the suspected object image  (try to get half of the object and half the background using the cross-hair as a guide)')  
     roi(img2)
     global src_roi
     src_roi=ROI                  
               
     img3=img2.copy()
     cv2.rectangle(img=img3, pt1=(x, y), pt2=(x + w, y + h), color=(0, 0, 255), thickness=2)
     cv2.imwrite("images/temps/rois.jpg", img3) 
     
     detect_blur.blur(dst_roi, src_roi, img)

if __name__ == '__roix__':
   db_roi()

   



     
     