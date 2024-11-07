import cv2
import numpy as np

dog = cv2.imread('./dog.jpeg')
h, w, ch = dog.shape
# 中心点为x,y
M = cv2.getRotationMatrix2D((w/2, h/2), 15, 0.5)
# 如果想改变新图像的尺寸，需要修改dsize
new = cv2.warpAffine(dog, M, (int(w/2), int(h/2)))

# cv2.imshow('dog', dog)
cv2.imshow('new', new)
cv2.waitKey(0)