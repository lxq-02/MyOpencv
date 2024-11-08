import cv2
import numpy as np

img = cv2.imread('./lena.png')

dst = cv2.Canny(img, 100, 200)

cv2.imshow('img', img)
cv2.imshow('dst', dst)
cv2.waitKey(0)