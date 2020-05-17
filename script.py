# coding=utf-8
# @Time     :2020/5/13 0013 10:44
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :script.py
# @Software :PyCharm

import numpy as np
import cv2
from matplotlib import pyplot as plt

# img_path = r'./images/dint_geocode1.png'
# im = plt.imread(img_path)
# im = cv2.imread(r'images\car.png')
# im = cv2.imread(r'images\laneseg.jpg')
# im = cv2.imread(r'images\20180718-20180724\dint_geocode1.png')

image = cv2.imread(r'images\dint_geocode.png')
label = cv2.imread(r'images\label.png', cv2.IMREAD_GRAYSCALE)

# plt.figure(figsize=(100, 80), dpi=80)
# plt.imshow(im)
# plt.xticks(range(0, 3200, 100))
# plt.yticks(range(0, 2200, 100))
# plt.grid(alpha=5)
# plt.show()

# print(type(im), im.shape, im.dtype)
# cv2.namedWindow('mask', cv2.WINDOW_NORMAL)
# cv2.imshow('mask', mask)
# cv2.namedWindow('image', cv2.WINDOW_NORMAL)
# cv2.imshow('image', im)
# # cv2.imshow('image', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

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
