import cv2
import numpy as np

dog = cv2.imread('./dog.jpeg')
new = cv2.rotate(dog, cv2.ROTATE_90_CLOCKWISE)
new2 = cv2.rotate(dog, cv2.ROTATE_180)


# 调整图像大小
dog = cv2.resize(dog, None, fx=0.2, fy=0.2, interpolation=cv2.INTER_AREA)
new = cv2.resize(new, None, fx=0.2, fy=0.2, interpolation=cv2.INTER_AREA)
new2 = cv2.resize(new2, None, fx=0.2, fy=0.2, interpolation=cv2.INTER_AREA)

# 创建窗口并设置显示位置
cv2.namedWindow('dog')
cv2.moveWindow('dog', 0, 0)  # 将 'dog' 窗口放置在屏幕的左上角

cv2.namedWindow('new')
cv2.moveWindow('new', 400, 0)  # 将 'new' 窗口放置在屏幕上方，横向偏移400像素

cv2.namedWindow('new2')
cv2.moveWindow('new2', 800, 0)  # 将 'new_2' 窗口放置在屏幕的右上方，横向偏移800像素


cv2.imshow('dog', dog)
cv2.imshow('new', new)
cv2.imshow('new2', new2)

cv2.waitKey(0)