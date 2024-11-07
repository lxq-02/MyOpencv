import cv2
import numpy as np

img = cv2.imread('dog.jpeg')

kernal = np.ones((5,5), np.float32) / 25

dst = cv2.filter2D(img, -1, kernal)

cv2.imshow('dst', dst)
cv2.imshow('img', img)
cv2.waitKey(0)