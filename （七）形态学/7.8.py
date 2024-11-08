import cv2
import numpy as np

img = cv2.imread('./dotinj.png')

kernal = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))

# 黑帽运算
dst = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernal)

cv2.imshow('img', img)
cv2.imshow('dst', dst)

cv2.waitKey(0)