import cv2
import numpy as np

img = np.zeros((300, 400, 3), np.uint8)

cv2.rectangle(img, (10, 10), (200, 100), (0, 0, 255), -1)

cv2.imshow('draw', img)
cv2.waitKey(0)