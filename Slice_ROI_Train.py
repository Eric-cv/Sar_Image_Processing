# coding=utf-8
# @Time     :2020/5/16 9:47
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :Slice_ROI_Train.py
# @Software :PyCharm
import cv2, math, os
import numpy as np

img_path = r'images/20180718-20180724/dint_geocode.png'
img_path1 = r'images/20180718-20180724/coh_geocode.png'
# img_path1 = None
lab_path = r'./images/label.png'
# img_path = r'images/20180805-20180823/dint_geocode1.png'
# lab_path = r'./images/label1.png'
# lab_path = r'H:/ZQ_file/Sar_seg/new_labels/dint_geocode_mask.png'
# lab_path = r'H:/ZQ_file/Sar_seg/new_labels/dint_geocode_mask1.png'
img = cv2.imread(img_path)
lab = cv2.imread(lab_path, cv2.IMREAD_GRAYSCALE)
img_name = os.path.split(img_path)[1]
image = img.copy()
label = lab.copy()
if img_path1:
    img1 = cv2.imread(img_path1)
    image1 = img1.copy()
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


def get_cooridinate(img, list):
    for i in range(int(len(list) * 0.25)):
        i = i * 4
        x1, y1, x2, y2 = list[i], list[i + 1], list[i + 2], list[i + 3]
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 3)
    return list


def show_roi_grid(img, list):
    cv2.namedWindow("image", cv2.WINDOW_NORMAL)
    cv2.imshow("image", img)
    cv2.setMouseCallback("image", EVENT_LBUTTONDOWN)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    get_cooridinate(img, list)
    cv2.namedWindow("image", cv2.WINDOW_NORMAL)
    cv2.imshow("image", img)
    ROI_path = 'ROI'
    ROI_list = os.listdir(ROI_path)
    # if len(ROI_list):
    #     for i in range(len(ROI_list)):
    #         os.remove(os.path.join(ROI_path, ROI_list[i]))
    # cv2.imwrite('./ROI/Whole_ROI_{}'.format(img_name), img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return list


# get ROI and cooridinate list
ROI_coordinate_list = show_roi_grid(img, list)

# img_save_path = './sar_images/image2/whole'
# lab_save_path = './sar_labels/label2/whole'
# img_save_path1 = './sar_images/image2/whole'
# lab_save_path1 = './sar_labels/label2/whole'

img_save_path = './sar_images/image3/part'
lab_save_path = './sar_labels/label3/part'
img_save_path1 = './sar_images/image3/part'
lab_save_path1 = './sar_labels/label3/part'
# make save dir
if not os.path.exists(img_save_path):
    os.makedirs(img_save_path)
if not os.path.exists(lab_save_path):
    os.makedirs(lab_save_path)

img_list = os.listdir(img_save_path)
lab_list = os.listdir(lab_save_path)

# remove images before
if len(img_list):
    for i in range(len(img_list)):
        os.remove(os.path.join(img_save_path, img_list[i]))
        os.remove(os.path.join(lab_save_path, lab_list[i]))
    print('Removed {} piece of images in sar_images dir'.format(len(img_list)))
    print('Removed {} piece of images in sar_labels dir'.format(len(lab_list)))

else:
    print('No images')

if img_path1:
    # make save dir
    if not os.path.exists(img_save_path1):
        os.makedirs(img_save_path1)
    if not os.path.exists(lab_save_path1):
        os.makedirs(lab_save_path1)
    img_list1 = os.listdir(img_save_path1)
    lab_list1 = os.listdir(lab_save_path1)
    # remove images before
    if len(img_list1):
        for i in range(len(img_list1)):
            os.remove(os.path.join(img_save_path1, img_list1[i]))
            os.remove(os.path.join(lab_save_path1, lab_list1[i]))
        print('Removed {} piece of images in sar_images dir'.format(len(img_list1)))
        print('Removed {} piece of images in sar_labels dir'.format(len(lab_list1)))

    else:
        print('No images')

# slice and save images
# i, sum = 0, 0
i, sum = 560, 2875
ROI_length = 256
# ROI_length = 112
# ROI_length = 96
coordinate = []
for num in range(int(len(list) * 0.25)):
    num = num * 4
    x1, y1, x2, y2 = list[num], list[num + 1], list[num + 2], list[num + 3]

    for row in range(y1, y2, 25):
        for column in range(x1, x2, 25):
            img1 = image[row:row + ROI_length, column:column + ROI_length]
            lab1 = label[row:row + ROI_length, column:column + ROI_length]
            if img_path1:
                img2 = image1[row:row + ROI_length, column:column + ROI_length]
            sum += 1
            if np.sum(lab1):
                # if np.sum(lab1) > 38 * lab1.size * 0.165 and np.sum(lab1) < 38 * lab1.size * 0.5: # 112
                if np.sum(lab1) > 38 * lab1.size * 0.0412 and np.sum(lab1) < 38 * lab1.size * 0.1:  # 256 part
                # if np.sum(lab1) > 38 * lab1.size * 0.2 and np.sum(lab1) < 38 * lab1.size * 0.8:  # 256 whole
                    i += 1
                    coordinate.append((column, row, column + ROI_length, row + ROI_length))
                    cv2.imwrite(os.path.join(img_save_path, 'image_dint_{}.png'.format(i)), img1)
                    cv2.imwrite(os.path.join(lab_save_path, 'label_dint_{}.png'.format(i)), lab1)
                    if img_path1:
                        cv2.imwrite(os.path.join(img_save_path1, 'image_coh_{}.png'.format(i)), img2)
                        cv2.imwrite(os.path.join(lab_save_path1, 'label_coh_{}.png'.format(i)), lab1)

                else:
                    # print(np.sum(lab1))
                    # print('all label is 38')
                    pass
            else:
                # print(np.sum(lab1))
                # print('all label is 0')
                pass

    print('Total images saved: {} '.format(i))
    print('Total images abandoned: {}'.format(sum - i))
    print('Total images: {}'.format(sum))

print('finished')

for i in range(len(coordinate)):
    x1, y1, x2, y2 = coordinate[i][0], coordinate[i][1], coordinate[i][2], coordinate[i][3]
    cv2.namedWindow("image", cv2.WINDOW_NORMAL)
    cv2.imshow("image", img)
    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 3)
print(len(coordinate))
cv2.imwrite('./ROI/ROI_length_{}_{}'.format(ROI_length, img_name), img)
cv2.waitKey(0)
cv2.destroyAllWindows()
