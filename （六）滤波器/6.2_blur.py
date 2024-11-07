import cv2
import numpy as np

img = cv2.imread('dog.jpeg')

dst = cv2.blur(img, (5,5))

cv2.imshow('dst', dst)
cv2.imshow('img', img)
cv2.waitKey(0)