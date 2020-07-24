# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 16:21:56 2020

@author: anyaj
"""

#!/usr/bin/env python

from PIL import Image, ImageChops


#ORIG = './books-edited.jpg'
ORIG = "images/SC_Jlawsky.jpg"
TEMP = 'temp.jpg'
SCALE = 10


def ELA():
    original = Image.open(ORIG)
    original.save(TEMP, quality=90)
    temporary = Image.open(TEMP)

    diff = ImageChops.difference(original, temporary)
    d = diff.load()
    WIDTH, HEIGHT = diff.size
    for x in range(WIDTH):
        for y in range(HEIGHT):
            d[x, y] = tuple(k * SCALE for k in d[x, y])

    diff.show()

if __name__ == '__main__':
    ELA()

