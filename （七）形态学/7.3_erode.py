import cv2
import numpy as np

img = cv2.imread('./j.png')

# kernal = np.ones((3,3), np.uint8)
kernal = cv2.getStructuringElement(cv2.MORPH_RECT, (7,7))
dst = cv2.erode(img, kernal, iterations=1)

cv2.imshow('img', img)
cv2.imshow('dst', dst)

cv2.waitKey(0)