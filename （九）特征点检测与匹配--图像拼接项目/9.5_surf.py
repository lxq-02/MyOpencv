import cv2
import numpy as np

# 读图片
img = cv2.imread('chess.png')

# 灰度化
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 创建sift对象
# sift = cv2.xfeatures2d.SIFT_create()
# 船舰surf对象
surf = cv2.xfeatures2d.SURF_create()

# 进行检测
# kp, des = sift.detectAndCompute(gray, None)
# 使用surf进行检测
kp, des = surf.detectAndCompute(gray, None)

# 绘制Keypoints
cv2.drawKeypoints(gray, kp, img)

cv2.imshow('img', img)
cv2.waitKey(0)