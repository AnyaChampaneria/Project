# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 12:12:56 2020

@author: anyaj
"""
import sys
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QApplication
from PyQt5.QtGui import QImage, QPixmap
from PyQt5 import uic
import cv2  # Not actually necessary if you just want to create an image.
import detect_blur as db
from ELA_opencv import ELA

Ui_MainWindow, QtBaseClass = uic.loadUiType('gui2.ui')

class MyApp(QMainWindow):
    def __init__(self, parent=None, name=None):
    #def __init__(self) #original
        super(MyApp, self).__init__(parent)
        #super(MyApp, self).__init__() #original
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.upload_button.clicked.connect(self.upload)
        self.ui.ela_button.clicked.connect(self.ela)
        self.ui.bd_button.clicked.connect(self.bd) 
        self.ui.clear_all.clicked.connect(self.clear_all)
                                   
        
    def upload(self):
        global img        
        img = QImage(self.ui.image_path.toPlainText())
        global image
        image = cv2.imread(self.ui.image_path.toPlainText())
        self.ui.image_label.setPixmap(QPixmap(img))

             
    def ela(self):
        ELA(image)
        self.ui.ela_image.setPixmap(QPixmap("images/temps/diff2.jpg"))
        self.ui.ela_image_2.setPixmap(QPixmap("images/temps/ela_mask.jpg")) 
            
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
        
        print("Draw a box on a border in the original object in image "
              "(try to get half of the object and half the background using the cross-hair as a guide)")
        QMessageBox.information(self,'Instructions',
                            'Draw a box on a border in the original object in image '
                          '(try to get half of the object and half the background using the cross-hair as a guide)')  
        roi(image)
        global dst_roi
        dst_roi=ROI
        
        print("Draw a box the same size on a border in the suspected object image"
              " (try to get half of the object and half the background using the cross-hair as a guide)")
        QMessageBox.information(self,'Instructions',
                                'Draw a box the same size on a border in the suspected object image  '
                        '(try to get half of the object and half the background using the cross-hair as a guide)')  
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
                  
            if perc_diff_fm<20:
                text = "{:.0f}% - GREEN ".format(perc_diff_fm)
                "\nPercentage difference is not large enough to suggest cloning"
    
            elif 20<perc_diff_fm<100:
                text = "{:.0f}% - AMBER ".format(perc_diff_fm)
                "\nPercentage difference is large enough to cause concern, \npossible cloning present"


            elif perc_diff_fm>100:
                text = "{:.0f}% -RED "
                "\nPercentage difference is very large, \nit is likely there is cloning in this image".format(perc_diff_fm)
    
            #print(text)
            self.ui.bd_results.setText(text)
                
            if __name__ == '__blur__': 
                blur()    
        
        blur(dst_roi, src_roi, image)
    
    
    def clear_all(self):
        self.ui.image_label.clear()
        self.ui.ela_image.clear()
        self.ui.ela_image_2.clear()
        self.ui.bd_image.clear()
        self.ui.bd_results.clear()


        
if __name__ == '__main__':
    app = QApplication([])
    window = MyApp()
    window.show()
    sys.exit(app.exec_())




