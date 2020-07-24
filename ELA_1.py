# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 16:18:25 2020

@author: anyaj
"""
from PIL import Image, ImageChops, ImageEnhance
import sys, os.path

filename = "images/SC_Jlawsky.jpg"
resaved = filename + '.resaved.jpg'
ela = filename + '.ela.png'

im = Image.open(filename)

im.save(resaved, 'JPEG', quality=80)
resaved_im = Image.open(resaved)

ela_im = ImageChops.difference(im, resaved_im)
extrema = ela_im.getextrema()
max_diff = max([ex[1] for ex in extrema])
scale = 255.0/max_diff

ela_im = ImageEnhance.Brightness(ela_im).enhance(scale)

print ("Maximum difference was %d" % (max_diff))
ela_im.save(ela)
ela_im.show()

