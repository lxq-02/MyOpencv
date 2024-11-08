import cv2
import numpy as np

img = cv2.imread('./tophat.png')

kernal = cv2.getStructuringElement(cv2.MORPH_RECT, (19,19))

# 顶帽运算
dst = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernal)

cv2.imshow('img', img)
cv2.imshow('dst', dst)

cv2.waitKey(0)