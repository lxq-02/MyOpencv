import cv2
import numpy as np

import matplotlib
matplotlib.use('Qt5Agg')  # or 'Qt5Agg' if you prefer

import matplotlib.pyplot as plt



# 获取背景
# 1、通过二值法得到黑白图片
# 2、通过形态学获取背景

img = cv2.imread('water_coins.jpeg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 二值化
# 自适应性寻找阈值
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# 开运算，膨胀，去除噪点
kernel = np.ones((3,3), np.int8)
open1 = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

# 膨胀
bg = cv2.dilate(open1, kernel, iterations = 1)


# 获取前景物体
dist = cv2.distanceTransform(open1, cv2.DIST_L2, 5)

# 前景
ret, fg = cv2.threshold(dist, 0.7*dist.max(), 255, cv2.THRESH_BINARY)

# plt.imshow(dist, cmap='gray')
# plt.show()
# exit()

# 获取未知区域
fg = np.uint8(fg)
unknown = cv2.subtract(bg, fg)

# 创建连通域
ret, marker = cv2.connectedComponents(fg)
marker = marker + 1
marker[unknown==255] = 0

# 进行图像分割
result = cv2.watershed(img, marker)

img[result == -1] = [0, 0, 255]

cv2.imshow("img", img)
cv2.imshow("unknown", unknown)
cv2.imshow("fg", fg)
cv2.imshow("dist", dist)
cv2.imshow("bg", bg)
cv2.imshow("thresh", thresh)
cv2.waitKey(0)