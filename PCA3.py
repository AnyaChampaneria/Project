# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 12:23:07 2020

@author: anyaj
"""
#from sklearn.datasets import load_sample_image
from sklearn.feature_extraction import image
from sklearn.decomposition import PCA
import cv2
import matplotlib.pyplot as plt

im = cv2.imread("images/SC_fishandwhale.jpg")
grayscale_image = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
# Create patches of size 25 by 25 and create a matrix from all patches
patches = image.extract_patches_2d(grayscale_image, (25, 25), random_state = 42)
print(im.shape)
print(patches.shape)
# reshape patches because I got an error when applying fit_transform(ValueError: FoundValueError: Found array with dim 3. Estimator expected <= 2.)
#patches_reshaped = patches.reshape(2,-1)
patches_reshaped = patches.reshape(patches.shape[0],-1)
print(patches_reshaped.shape)
# this should return a (53824, 625) shaped data
#apply PCA
pca = PCA(.80)
projected = pca.fit_transform(patches_reshaped.data)
denoised_image = pca.inverse_transform(projected)
final=image.reconstruct_from_patches_2d(denoised_image.reshape(-1,25,25), grayscale_image.shape)
print(denoised_image.shape)
#cv2.imshow('Image', final)
key = cv2.waitKey(0)

