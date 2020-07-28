# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 15:29:23 2020

@author: anyaj
"""
import numpy as np
import pywt, cv2

def w2d(image, mode='haar', level=1):
    im_array = np.float32(image)
    im_array /= 255
    coeffs = pywt.wavedec2(im_array, mode, level=level)
    coeffs_h = list(coeffs)

    coeffs_h[0] *= 0
    im_array_h = pywt.waverec2(coeffs_h, mode)
    im_array_h *= 255
    return im_array_h


img = cv2.imread("images/SC_fishandwhale.jpg")
quality = 3

b = w2d(img[:, :, 0], 'db1', quality)
g = w2d(img[:, :, 1], 'db1', quality)
r = w2d(img[:, :, 2], 'db1', quality)

dst = cv2.merge((b, g, r))
cv2.imshow("orig", dst)
cv2.waitKey(0)

