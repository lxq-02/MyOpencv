import cv2
import numpy as np

# 创建一张图片
img = np.zeros((200, 400), np.uint8)

img[50:150, 100: 200] = 255

new_img = cv2.bitwise_not(img)

cv2.imshow('img', img)
cv2.imshow('new_img', new_img)
cv2.waitKey(0)