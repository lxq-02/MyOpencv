import cv2
import numpy as np
 
img = cv2.imread('key.png')
 
mean_img = cv2.pyrMeanShiftFiltering(img, 20, 30)
 
imgcanny = cv2.Canny(mean_img, 150, 300)
 
contours, _, _ = cv2.findContours(imgcanny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
 
cv2.drawContours(img, contours, -1, (0, 0, 255))
cv2.drawContours(image, contours, contourIdx, color)
 
cv2.imshow('img', img)
cv2.imshow('mean_img', mean_img)
cv2.imshow('canny', imgcanny)
cv2.waitKey()