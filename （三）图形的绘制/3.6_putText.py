import cv2
import numpy as np

img = np.zeros((300, 400, 3), np.uint8)

# 画文本
cv2.putText(img, "Hello world!", (50, 200), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255))
cv2.imshow('putText', img)
cv2.waitKey(0)