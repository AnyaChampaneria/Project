# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 12:43:11 2020

@author: anyaj
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
import cv2  # Not actually necessary if you just want to create an image.
import numpy as np
import detect_blur as db
from ROI import roi
from ELA_opencv import ELA
from PCA3 import pca

Ui_MainWindow, QtBaseClass = uic.loadUiType('gui.ui')

class MyApp(QMainWindow):
    def __init__(self, parent=None, name=None):
    #def __init__(self) #original
        super(MyApp, self).__init__(parent)
        #super(MyApp, self).__init__() #original
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.upload_button.clicked.connect(self.upload)
        self.ui.ela_button.clicked.connect(self.ela)
        self.ui.pca_button.clicked.connect(self.pca)
        self.ui.bd_button.clicked.connect(self.bd) 
        
    def upload(self):
        global img        
        img = QImage(self.ui.image_path.toPlainText())
        global image
        image = cv2.imread(self.ui.image_path.toPlainText())
        self.ui.image_label.setPixmap(QPixmap(img))

    
            
    def ela(self):
        ELA(image)
        self.ui.ela_image.setPixmap(QPixmap("images/temps/diff1.jpg"))
        self.ui.ela_image_2.setPixmap(QPixmap("images/temps/diff2.jpg")) 

    def pca(self):
        pca(image)
        self.ui.pca_image.setPixmap(QPixmap("images/temps/final1.jpg")) 
        self.ui.pca_image_2.setPixmap(QPixmap("images/temps/final2.jpg")) 
             
            
    def bd(self):   
        
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
        
        print("Draw a box on a border in the original object in image (try to get half of the object and half the background using the cross-hair as a guide)")
        QMessageBox.information(self,'Instructions','Draw a box on a border in the original object in image (try to get half of the object and half the background using the cross-hair as a guide)')  
        roi(image)
        global dst_roi
        dst_roi=ROI
        
        print("Draw a box the same size on a border in the suspected object image (try to get half of the object and half the background using the cross-hair as a guide)")
        QMessageBox.information(self,'Instructions','Draw a box the same size on a border in the suspected object image  (try to get half of the object and half the background using the cross-hair as a guide)')  
        roi(img2)
        global src_roi
        src_roi=ROI
                
        img3=img2.copy()
        cv2.rectangle(img=img3, pt1=(x, y), pt2=(x + w, y + h), color=(0, 0, 255), thickness=2)
        cv2.imwrite("images/temps/rois.jpg", img3) 
                
        self.ui.bd_image.setPixmap(QPixmap("images/temps/rois.jpg")) 
            
        def blur(dst_roi, src_roi, image):
            dst_grey = cv2.cvtColor(dst_roi, cv2.COLOR_BGR2GRAY)
            src_grey = cv2.cvtColor(src_roi, cv2.COLOR_BGR2GRAY)
            global dst_fm
            dst_fm = db.variance_of_laplacian(dst_grey)
            global src_fm
            src_fm = db.variance_of_laplacian(src_grey)
            global perc_diff_fm
            perc_diff_fm=((dst_fm-src_fm)/dst_fm)*100
                  
            if src_fm < dst_fm:
                global text
                text = "more"
            else :
                perc_diff_fm=-perc_diff_fm
                text = "less"
        
                
        if __name__ == '__blur__': 
            blur()
                    
        
        blur(dst_roi, src_roi, image)
        print("Boundary on original image: {:.0f} \nSuspected boundary: {:.0f} \nSuspected boundary is {:.0f}% {} blurry than the boundary on orginal object".format(dst_fm, src_fm, perc_diff_fm, text))
        
        self.ui.bd_results.setText('Boundary on original image: {:.0f} \nSuspected boundary: {:.0f} \nSuspected boundary is {:.0f}% {} blurry than the boundary \non orginal object'.format(dst_fm, src_fm, perc_diff_fm, text))


        
if __name__ == '__main__':
    app = QApplication([])
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

