import cv2
import numpy as np

dog = cv2.imread('./dog.jpeg')


img = np.ones((1200, 1920, 3), np.uint8) * 50

cv2.namedWindow('orig', cv2.WINDOW_NORMAL)
cv2.resizeWindow('orig', 800, 600)
cv2.imshow('orig', dog)

result = cv2.multiply(dog, img)
cv2.namedWindow('result', cv2.WINDOW_NORMAL)
cv2.resizeWindow('result', 800, 600)
cv2.imshow('result', result)
cv2.waitKey(0)