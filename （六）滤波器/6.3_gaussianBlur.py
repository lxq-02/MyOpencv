import cv2
import numpy as np

img = cv2.imread('./gaussian.png')

dst = cv2.GaussianBlur(img, (5,5), sigmaX=1)

cv2.imshow('dst', dst)
cv2.imshow('img', img)
cv2.waitKey(0)