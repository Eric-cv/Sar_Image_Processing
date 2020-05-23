# coding=utf-8
# @Time     :2020/5/13 0013 10:44
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :script.py
# @Software :PyCharm

import numpy as np
import cv2, torch
from matplotlib import pyplot as plt
import imgaug as iaa

img_path1 = r'images/20180718-20180724/dint_geocode.png'
img_path2 = r'images/20180718-20180724/coh_geocode.png'

img1 = cv2.imread(img_path1)
img2 = cv2.imread(img_path2)
print(img1.shape, img2.shape)
img = np.dstack((img1, img2))
print(img.shape)


# img = np.stack((img1, img2), axis=3)
# print(img.shape)
# print(img1_tensor.shape)

# cv2.namedWindow('image', cv2.WINDOW_NORMAL)
# cv2.imshow('image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# test stack
# a = np.ones((2,4,3))
# b = np.full((2,4,3), 2)
# c = np.dstack((a,b))

'''
# c h w
# arr = np.array((range(28 * 3)).reshape(4, 7, 3))
arr = np.zeros((5, 5))

plt.figure(figsize=(20, 8), dpi=50)
plt.imshow(arr)
plt.show()
print(arr)
# brr=np.array(range(28)).reshape((7,4))
# print(arr, brr, sep='\n')
# print(arr.shape, brr.shape)
'''

