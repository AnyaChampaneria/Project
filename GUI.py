# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 12:43:11 2020

@author: anyaj
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
import cv2  # Not actually necessary if you just want to create an image.
import numpy as np
from ROI import roi

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
        img = (self.image_path_2_.text())
        print(img)
        
#if __name__ == '__MyApp__':
app = QApplication([])
window = MyApp()
window.show()
sys.exit(app.exec_())

