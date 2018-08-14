## kitti dataset ground truth interpolation kit
# 2018.08.12
# Kuo-Shiuan Peng
import os
import numpy as np
import scipy as sp
from matplotlib import pyplot as plt
import cv2
from PIL import Image

kernel_sz = (5, 5)
kernel_type = "circle"
dilation_iter = 1
showOut = False

path2Work 	= 'kitti_gt/'
path2Img  	= 'disp_gt.png'
output_name = 'disp_gt_interp'
img = cv2.imread(path2Work+ path2Img)

if kernel_type == "ellipse":
	kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, kernel_sz)
elif kernel_type == "circle":
	kernel = np.ones(kernel_sz,np.uint8)
	kernel[0,0] = 0
	kernel[1,0] = 0
	kernel[0,4] = 0
	kernel[4,4] = 0
else: # default kernel = rect
	kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernel_sz)


img_dilation = np.array(cv2.dilate(img[:,:,0], kernel, iterations=dilation_iter))

img_dilation = cv2.morphologyEx(img_dilation, cv2.MORPH_CLOSE, kernel)

plt.imsave(os.path.join("{}.png".format(output_name)), img_dilation, cmap='plasma')

if showOut:
	plt.imshow(img_dilation, cmap = 'plasma')
	plt.show()


