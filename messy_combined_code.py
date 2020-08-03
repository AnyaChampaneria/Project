
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 16:08:51 2020
@author: anyaj
"""
import cv2
import imutils
import numpy as np
import joblib

pts = [] # for storing points


 # :mouse callback function
def draw_roi(event, x, y, flags, param):
    img2 = img.copy()

    if event == cv2.EVENT_LBUTTONDOWN: # Left click, select point
        pts.append((x, y))  

    #if event == cv2.EVENT_RBUTTONDOWN: # Right click to cancel the last selected point
      #  pts.pop()  

    if event == cv2.EVENT_RBUTTONDOWN: # 
        mask = np.zeros(img.shape, np.uint8)
        points = np.array(pts, np.int32)
        points = points.reshape((-1, 1, 2))
                 # 
        mask = cv2.polylines(mask, [points], True, (255, 255, 255), 2)
        global mask2
        mask2 = cv2.fillPoly(mask.copy(), [points], (255, 255, 255)) # for ROI
        #mask3 = cv2.fillPoly(mask.copy(), [points], (0, 255, 0)) # for displaying images on the desktop

        #show_image = cv2.addWeighted(src1=img, alpha=0.8, src2=mask3, beta=0.2, gamma=0)

        cv2.imshow("mask", mask2)
        #cv2.imshow("show_img", show_image)
        global ROI
        ROI = cv2.bitwise_and(mask2, img)
        #cv2.imshow("ROI", ROI)
        cv2.waitKey(0)

    if len(pts) > 0:
                 # Draw the last point in pts
        cv2.circle(img2, pts[-1], 3, (0, 0, 255), -1)

    if len(pts) > 1:
                 # 
        for i in range(len(pts) - 1):
            cv2.circle(img2, pts[i], 5, (0, 0, 255), -1) # x ,y is the coordinates of the mouse click place
            cv2.line(img=img2, pt1=pts[i], pt2=pts[i + 1], color=(255, 0, 0), thickness=2)

    cv2.imshow('image', img2)



 #Create images and windows and bind windows to callback functions
img = cv2.imread("images/SC_fishandwhale.jpg")
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

def variance_of_laplacian(image):
	# compute the Laplacian of the image and then return the focus
	# measure, which is simply the variance of the Laplacian
	return cv2.Laplacian(image, cv2.CV_64F).var()

image=img
#image = cv2.imread("SC_example.jpg")
ROI=ROI
b, g, r = cv2.split(image)
img2 = cv2.merge([r, g, b])
#plt.imshow(img2)
gray = cv2.cvtColor(ROI, cv2.COLOR_BGR2GRAY)
fm = variance_of_laplacian(ROI)
#text = "Not Blurry"

# if the focus measure is less than the supplied threshold,
	# then the image should be considered "blurry"
if fm < 100:
		text = "Blurry"
else :
		text = "Not Blurry"
	# show the image
cv2.putText(ROI, "{}: {:.2f}".format(text, fm), (10, 30),
		cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
cv2.imshow("Image",ROI)
key = cv2.waitKey(0)
