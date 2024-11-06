import cv2
import numpy as np

img = np.zeros((300, 400, 3), np.uint8)

# 画多边形
# 这个点集必须是32位
pts = np.array([(300, 10), (150, 100), (370, 100)], np.int32)
cv2.polylines(img, [pts], True, (0, 0, 255))

# 填充多边形
cv2.fillPoly(img, [pts], (0, 255, 0))
cv2.imshow('polylines', img)
cv2.waitKey(0)