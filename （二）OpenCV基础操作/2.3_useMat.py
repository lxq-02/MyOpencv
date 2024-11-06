import cv2
import numpy as np

img = np.zeros((300, 400, 3), np.uint8)

# 浅拷贝
img2 = img

# 深拷贝
img3 = img.copy()

img[10:50, 10:100] = [0, 0, 255]

cv2.imshow('img', img)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)

cv2.waitKey(0)

