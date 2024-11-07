import cv2
import numpy as np

img = cv2.imread('./chess.png')

# 拉普拉斯
ldst = cv2.Laplacian(img, cv2.CV_64F, ksize=5)

cv2.imshow('img', img)
cv2.imshow('ldst', ldst)
cv2.waitKey(0)