import cv2
import numpy as np

img = np.zeros((300, 400, 3), np.uint8)

# 分离
b,g,r = cv2.split(img)

b[10:50, 20:100] = 255  # 分离之后就变成了黑白色
g[10:50, 20:100] = 255

# 合并
img2 = cv2.merge((b,g,r))

cv2.imshow('img', img)
cv2.imshow('b', b)
cv2.imshow('g', g)
cv2.imshow('img2', img2)

cv2.waitKey(0)

