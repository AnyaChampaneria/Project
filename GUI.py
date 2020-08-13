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
from ELA_opencv import ELA
import detect_blur

Ui_MainWindow, QtBaseClass = uic.loadUiType('gui.ui')

class MyApp(QMainWindow):
    def __init__(self, parent=None, name=None):
    #def __init__(self) #original
        super(MyApp, self).__init__(parent)
        #super(MyApp, self).__init__() #original
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Upload.clicked.connect(self.analyse)
        
    def analyse(self):
        img = QImage(self.ui.image_path_2.toPlainText())
        image = cv2.imread(self.ui.image_path_2.toPlainText())
        #img.QtGui.QImage(QtGui.QImageReader(img).read())
        #self.ui.image_label.QImage(img)
       # image = QtGui.QImage(QtGui.QImageReader(":/images/test.png").read())
        self.ui.image_label.setPixmap(QPixmap(img))
        #ELA(img)
        
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
            global ela95
            cv2.imwrite("images/temps/diff1.jpg", diff1)
            
            # write img2 at 90% jpg compression
            temp90="images/temps/temp90.jpg"
            cv2.imwrite(temp90, img2, [cv2.IMWRITE_JPEG_QUALITY, jpg_quality2])
            
            # read compressed image
            img3 = cv2.imread(temp90)
            
            # get absolute difference between img1 and img2 and multiply by scale
            diff2 = scale * cv2.absdiff(img2, img3)
            global ela90
            cv2.imwrite("images/temps/diff2.jpg", diff2)
            
            # display it
            #cv2.imshow("ela95", diff1)
            #cv2.imshow("ela90", diff2)
            #cv2.waitKey(0)
            
        if __name__ == '__ELA__': 
            ELA()
        
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
                
        ELA(image)
        #ela95=QImage(diff1)
        #ela90=QImage(diff2)
        self.ui.ela95_label.setPixmap(QPixmap("images/temps/diff1.jpg"))
        self.ui.ela90_label.setPixmap(QPixmap("images/temps/diff2.jpg"))
                
        print("Draw a box on a border in the original object in image (try to get half of the object and half the background using the cross-hair as a guide)")
        roi(image)
        dst_roi=ROI

        print("Draw a box the same size on a border in the suspected object image (try to get half of the object and half the background using the cross-hair as a guide)")
        roi(img2)
        src_roi=ROI
    
        detect_blur.blur(dst_roi, src_roi, img)
        
if __name__ == '__main__':
    app = QApplication([])
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

