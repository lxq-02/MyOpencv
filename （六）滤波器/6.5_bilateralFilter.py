import cv2
import numpy as np

img = cv2.imread('./lena.png')

dst = cv2.bilateralFilter(img, 7, 20, 50)

cv2.imshow('dst', dst)
cv2.imshow('img', img)
cv2.waitKey(0)