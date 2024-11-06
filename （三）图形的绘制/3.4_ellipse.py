import cv2
import numpy as np

img = np.zeros((300, 400, 3), np.uint8)

# 画椭圆
cv2.ellipse(img, (200, 100),(50, 100), 30, 0, 150, (0, 0, 255), 4)

cv2.imshow('circle', img)
cv2.waitKey(0)