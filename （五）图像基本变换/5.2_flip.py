import cv2
import numpy as np

# 加载图像
dog = cv2.imread('./dog.jpeg')

# 检查图像是否加载成功
if dog is None:
    print("错误: 找不到图像文件。")
    exit()

# 对图像进行翻转操作
new = cv2.flip(dog, 0)  # 垂直翻转
new_2 = cv2.flip(dog, 1)  # 水平翻转

# 调整图像大小
dog = cv2.resize(dog, None, fx=0.3, fy=0.3, interpolation=cv2.INTER_AREA)
new = cv2.resize(new, None, fx=0.3, fy=0.3, interpolation=cv2.INTER_AREA)
new_2 = cv2.resize(new_2, None, fx=0.3, fy=0.3, interpolation=cv2.INTER_AREA)

# 创建窗口并设置显示位置
cv2.namedWindow('dog')
cv2.moveWindow('dog', 0, 0)  # 将 'dog' 窗口放置在屏幕的左上角

cv2.namedWindow('new')
cv2.moveWindow('new', 400, 0)  # 将 'new' 窗口放置在屏幕上方，横向偏移400像素

cv2.namedWindow('new_2')
cv2.moveWindow('new_2', 800, 0)  # 将 'new_2' 窗口放置在屏幕的右上方，横向偏移800像素

# 显示图像
cv2.imshow('dog', dog)
cv2.imshow('new', new)
cv2.imshow('new_2', new_2)

# 等待按键，并关闭所有窗口
cv2.waitKey(0)
cv2.destroyAllWindows()
