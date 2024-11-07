import cv2
import numpy as np

dog = cv2.imread('./dog.jpeg')
h, w, ch = dog.shape
M = np.float32([[1, 0, 500], [0, 1, 0]])
new = cv2.warpAffine(dog, M, (w, h))

cv2.imshow('dog', dog)
cv2.imshow('new', new)
cv2.waitKey(0)