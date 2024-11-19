import cv2
import numpy as np

# 读图片
img = cv2.imread('chess.png')

# 灰度化
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 创建orb对象
orb = cv2.ORB_create()

# 使用orb进行检测
kp, des = orb.detectAndCompute(gray, None)

# 绘制Keypoints
cv2.drawKeypoints(gray, kp, img)

cv2.imshow('img', img)
cv2.waitKey(0)