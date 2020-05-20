# coding=utf-8
# @Time     :2020/5/20 9:57
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :Slice_ROI_Predict.py
# @Software :PyCharm

import cv2, math, os
import numpy as np

img_path = r'images/california1.png'
# img_path = r'images/20180718-20180724/dint_geocode.png'
# img_path = r'images/20180805-20180823/dint_geocode1.png'

img = cv2.imread(img_path)
img_name = os.path.split(img_path)[1]
image = img.copy()
list = []


def EVENT_LBUTTONDOWN(event, x, y, flags, param):
    global list
    if event == cv2.EVENT_LBUTTONDOWN:
        text = "(%d,%d)" % (x, y)
        cv2.circle(img, (x, y), 1, (255, 0, 0), thickness=3)
        cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_PLAIN,
                    3.0, (0, 0, 0), thickness=5)
        cv2.imshow("image", img)
        list.append(x)
        list.append(y)

        for i in range(int(len(list) * 0.25)):
            i = i * 4
            x1, y1, x2, y2 = list[i], list[i + 1], list[i + 2], list[i + 3]
            width = x2 - x1
            height = y2 - y1
            if width % 16 != 0 or height % 16 != 0:
                width = math.floor(width / 16) * 16
                height = math.floor(height / 16) * 16
                x2 = x1 + width
                y2 = y1 + height
            list[i], list[i + 1], list[i + 2], list[i + 3] = x1, y1, x2, y2


def get_cooridinate(img, list, img_name):
    for i in range(int(len(list) * 0.25)):
        i = i * 4
        x1, y1, x2, y2 = list[i], list[i + 1], list[i + 2], list[i + 3]
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 3)
        img1 = img[y1:y2, x1:x2]
        cv2. imwrite('./ROI_Predict/ROI_{}'.format(img_name), img1)
    return list


def show_roi_grid(img, list, img_name):
    cv2.namedWindow("image", cv2.WINDOW_NORMAL)
    cv2.imshow("image", img)
    cv2.setMouseCallback("image", EVENT_LBUTTONDOWN)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    get_cooridinate(img, list, img_name)
    cv2.namedWindow("image", cv2.WINDOW_NORMAL)
    cv2.imshow("image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


show_roi_grid(img, list, img_name)


