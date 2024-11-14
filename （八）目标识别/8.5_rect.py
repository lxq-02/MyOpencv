import cv2
import numpy as np

# 读文件
img = cv2.imread('./hello.jpeg')
print(img.shape)

# 转变为单通道
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 二值化
ret, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

# 轮廓查找
contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# 绘制轮廓
cv2.drawContours(img, contours, 0, (0, 0, 255), 1)

# 最小矩形
r = cv2.minAreaRect(contours[1])    # 得到的点是浮点型
box = cv2.boxPoints(r)          # 得到的点是带角度的，将角度去除
box = np.int0(box)              # 转换为int
cv2.drawContours(img, [box], 0, (0, 0, 255), 2)

# 最大矩形
x,y,w,h = cv2.boundingRect(contours[1])
cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)

cv2.imshow('img', img)
cv2.waitKey(0)