import cv2
import numpy as np

img = np.zeros((300, 400, 3), np.uint8)

# shape属性中包括了三个信息
# 高度、长度、通道数
print(img.shape)

# 图像占用多大空间
# 高度 * 长度 * 通道数
print(img.size)

# 图像中每个元素的类型
print(img.dtype)