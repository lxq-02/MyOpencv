import cv2
import numpy as np

# img = cv2.imread('./dotinj.png')
img = cv2.imread('./j.png')

kernal = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))

# 开运算
# dst = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernal)
# 闭运算
# dst = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernal)

# 梯度
dst = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernal)

cv2.imshow('img', img)
cv2.imshow('dst', dst)

cv2.waitKey(0)