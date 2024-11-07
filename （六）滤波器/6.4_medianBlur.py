import cv2
import numpy as np

img = cv2.imread('./papper.png')

dst = cv2.medianBlur(img, 5)

cv2.imshow('dst', dst)
cv2.imshow('img', img)
cv2.waitKey(0)