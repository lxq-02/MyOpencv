import cv2
import numpy as np

maxCorners = 1000
qualityLevel = 0.01
minDistance = 10
img = cv2.imread('chess.png')

# 灰度化
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Harris角点检测
# dst = cv2.cornerHarris(gray, blockSize, ksize, k)
corners = cv2.goodFeaturesToTrack(gray, maxCorners, qualityLevel, minDistance)

# 得到的corners是32位，需要换为整型输出
corners = np.int0(corners)

# Shi-Tomasi绘制角点
for i in corners:
    x,y = i.ravel()     # 它是多维的，需要转化为一维
    cv2.circle(img, (x,y), 3, (255,0,0), -1)

cv2.imshow('harris', img)
cv2.waitKey(0)