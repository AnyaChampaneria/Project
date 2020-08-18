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
import numpy as np

im = cv2.imread("images/SC-images/genuine/plantpots.jpg")

def pca(im):
    grayscale_image = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    # Create patches of size 25 by 25 and create a matrix from all patches
    patches = image.extract_patches_2d(grayscale_image, (25, 25), random_state = 42)
    # reshape patches into compatible size array
    patches_reshaped = patches.reshape(patches.shape[0],-1)
    #apply PCA
    pca1 = PCA(.80)
    projected = pca1.fit_transform(patches_reshaped.data)
    denoised_image = pca1.inverse_transform(projected)
    final1=image.reconstruct_from_patches_2d(denoised_image.reshape(-1,25,25), grayscale_image.shape)
    cv2.imwrite("images/temps/final1.jpg", final1)
 
    pca2 = PCA(.90)
    projected = pca2.fit_transform(patches_reshaped.data)
    denoised_image = pca2.inverse_transform(projected)
    final2=image.reconstruct_from_patches_2d(denoised_image.reshape(-1,25,25), grayscale_image.shape)
    cv2.imwrite("images/temps/final2.jpg", final2)
    #pca3 = PCA(.90)
    #projected = pca3.fit_transform(patches_reshaped.data)
    #denoised_image = pca3.inverse_transform(projected)
    #final3=image.reconstruct_from_patches_2d(denoised_image.reshape(-1,25,25),grayscale_image.shape)

    f = plt.figure()
    f.add_subplot(1,2, 1)
    plt.axis("off")
    plt.imshow(np.rot90(final1,0), cmap="gray")
    f.add_subplot(1,2, 2)
    plt.axis("off")
    plt.imshow(np.rot90(final2,0), cmap="gray")
    
    #cv2.imshow('img',f)
    #f.add_subplot(1,3, 3)
    #plt.axis("off")
   # plt.imshow(np.rot90(final3,0), cmap="gray")
    #plt.show(block=True)

if __name__ == '__pca__': 
    pca()

#pca(im)


