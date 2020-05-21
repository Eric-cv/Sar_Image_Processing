# coding=utf-8
# @Time     :2020/5/19 16:52
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :Hist.py
# @Software :PyCharm

import cv2
from matplotlib import pyplot as plt

# img_path = r'images/cat.jpg'
img_path1 = r'images/20180718-20180724/dint_geocode.png'
img_path2 = r'images/20180718-20180724/coh_geocode.png'

img1 = cv2.imread(img_path1)
img2 = cv2.imread(img_path2)

color = ('b', 'g', 'r')
plt.figure(figsize=(10, 8), dpi=80)
ax1 = plt.subplot(211)
for i, col in enumerate(color):
    hist1 = cv2.calcHist([img1], [i], None, [256], [0, 256])

    plt.plot(hist1, color=col)
    plt.xlim([0, 256])
    plt.grid(alpha=0.8)
    plt.xlabel('pixel value')
    plt.ylabel('pixel quantity')
    plt.title('Hist of dint_geocode')

ax2 = plt.subplot(212)
for i, col in enumerate(color):
    hist2 = cv2.calcHist([img2], [i], None, [256], [0, 256])
    # fig = plt.figure(figsize=(20, 8), dpi=80)
    plt.plot(hist2, color=col)
    plt.xlim([0, 256])
    plt.grid(alpha=0.8)
    plt.xlabel('pixel value')
    plt.ylabel('pixel quantity')
    plt.title('Hist of coh_geocode')

plt.show()