import cv2
import numpy as np

img = np.zeros((300, 400, 3), np.uint8)

# 画圆
cv2.circle(img, (150, 100), 100, (0, 0, 255), 5)

cv2.imshow('circle', img)
cv2.waitKey(0)