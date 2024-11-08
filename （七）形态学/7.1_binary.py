import cv2
import numpy as np

img = cv2.imread('./dog.jpeg')
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, dst = cv2.threshold(img1, 180, 255, cv2.THRESH_BINARY)

cv2.imshow('img', img)
cv2.imshow('gray', img1)
cv2.imshow('dst', dst)

cv2.waitKey(0)