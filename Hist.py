# coding=utf-8
# @Time     :2020/5/19 16:52
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :Hist.py
# @Software :PyCharm

import cv2
from matplotlib import pyplot as plt

img_path = r'images/20180718-20180724/dint_geocode.png'
lab_path = r'./images/label.png'
# img_path = r'images/20180805-20180823/dint_geocode1.png'
# lab_path = r'./images/label1.png'
# lab_path = r'H:/ZQ_file/Sar_seg/new_labels/dint_geocode_mask.png'
# lab_path = r'H:/ZQ_file/Sar_seg/new_labels/dint_geocode_mask1.png'

img = cv2.imread(img_path)
color = ('b', 'g', 'r')
for i, col in enumerate(color):
    hist = cv2.calcHist([img], [i], None, [256], [0, 256])
    # plt.figsize()
    plt.plot(hist, color=col)
    plt.xlim([0, 256])
    plt.show()
