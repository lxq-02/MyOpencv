import cv2
import numpy as np

img = np.zeros((300, 400, 3), np.uint8)

# 画线坐标（x, y)，不是设置页面的（y,x)
cv2.line(img, (10, 20), (300, 100), (0, 0, 255), 5, 16)
cv2.line(img, (50, 20), (350, 100), (0, 0, 255), 5, 4)

cv2.imshow('draw', img)
cv2.waitKey(0)