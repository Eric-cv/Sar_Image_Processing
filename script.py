# coding=utf-8
# @Time     :2020/5/13 0013 10:44
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :script.py
# @Software :PyCharm

import numpy as np
import cv2, torch
from matplotlib import pyplot as plt

# c h w
# im = cv2.imread(r'images\laneseg.jpg')
# im = cv2.imread(r'images\20180718-20180724\dint_geocode.png')
im = cv2.imread(r'images\label.png')
# im = cv2.imread(r'images\car.png')X
mask = np.zeros(im.shape[:2], np.uint8)
mask[im == 128] = 255
print(type(im), im.shape, im.dtype)
cv2.imshow('mask', mask)
cv2.imwrite('./mask.png', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
# plt.figure(figsize=(20, 8), dpi=50)
# plt.imshow(im)
# plt.show()

'''
# c h w
# arr = np.array((range(28 * 3)).reshape(4, 7, 3))
# arr[3,6,:]=
arr = np.zeros((5, 5))

plt.figure(figsize=(20, 8), dpi=50)
plt.imshow(arr)
plt.show()
print(arr)
# brr=np.array(range(28)).reshape((7,4))
# print(arr, brr, sep='\n')
# print(arr.shape, brr.shape)
'''
