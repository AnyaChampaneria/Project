# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 16:08:51 2020

@author: anyaj
"""
import cv2
import imutils
import numpy as np
import joblib

img = cv2.imread("images/fish.jpg")
pts = [] # for storing points
 
 # :mouse callback function
def draw_roi(event, x, y, flags, param):
    #if __name__ == '__draw_roi__':
        img2 = img.copy()
     
        if event == cv2.EVENT_LBUTTONDOWN: # Left click, select point
            pts.append((x, y))  
     
        #if event == cv2.EVENT_RBUTTONDOWN: # Right click to cancel the last selected point
           # pts.pop()  
     
        if event == cv2.EVENT_RBUTTONDOWN: # 
            mask = np.zeros(img.shape, np.uint8)
            points = np.array(pts, np.int32)
            points = points.reshape((-1, 1, 2))
                     # 
            mask = cv2.polylines(mask, [points], True, (255, 255, 255), 2)
            mask2 = cv2.fillPoly(mask.copy(), [points], (255, 255, 255)) # for ROI
            mask3 = cv2.fillPoly(mask.copy(), [points], (0, 255, 0)) # for displaying images on the desktop
     
            show_image = cv2.addWeighted(src1=img, alpha=0.8, src2=mask3, beta=0.2, gamma=0)
     
            cv2.imshow("mask", mask2)
            cv2.imshow("show_img", show_image)
            global ROI
            ROI = cv2.bitwise_and(mask2, img)
            
            cv2.startWindowThread()
            cv2.namedWindow("preview")
            cv2.imshow("ROI", ROI)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            print(ROI)
            
     
        if len(pts) > 0:
                     # Draw the last point in pts
            cv2.circle(img2, pts[-1], 3, (0, 0, 255), -1)
     
        if len(pts) > 1:
                     # 
            for i in range(len(pts) - 1):
                cv2.circle(img2, pts[i], 5, (0, 0, 255), -1) # x ,y is the coordinates of the mouse click place
                cv2.line(img=img2, pt1=pts[i], pt2=pts[i + 1], color=(255, 0, 0), thickness=2)
     
        cv2.imshow('image', img2)

img = cv2.imread("images/fish.jpg")
img = imutils.resize(img, width=500)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_roi)
print("[INFO] Click the left button: select the point, right click: delete the last selected point, click the middle button: determine the ROI area")
print("[INFO] Press ‘S’ to determine the selection area and save it")
print("[INFO] Press ESC to quit")
while True:
    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break
    if key == ord("s"):
        saved_data = {
            "ROI": pts
        }
        joblib.dump(value=saved_data, filename="config.pkl")
        print(pts)
        print("[INFO] ROI coordinates have been saved to local.")
        break
cv2.destroyAllWindows()


#image = cv2.imread("images/fish.jpg")
#int_image(image)


    







