#1. 引入一幅图片，dog
#2. 要有一个LOGO，需要自己创建
#3. 计算图片在什么地方添加，在添加的地方变成黑色
#4. 利用add，将logo 与 图处叠加到一起

import cv2
import numpy as np

#导入图片
dog = cv2.imread('./dog.jpeg')

#创建LOGO和mask
logo = np.zeros((200, 200, 3), np.uint8)
mask = np.zeros((200, 200), np.uint8)

#绘制LOGO
logo[20:120, 20:120] = [0, 0, 255]  # 红色块
logo[80:180, 80:180] = [0, 255, 0]  # 绿色块

mask[20:120, 20:120] = 255  # 红色区域的 mask
mask[80:180, 80:180] = 255  # 绿色区域的 mask

#对mask按位求反，01互换，与dog的图片进行操作，方块的位置就变为了0
m = cv2.bitwise_not(mask)

#选择dog添加logo的位置
roi = dog[0:200, 0:200]

# 用掩码对原图区域进行与操作，保留原图的背景
tmp = cv2.bitwise_and(roi, roi, mask = m)

# 将 LOGO 添加到原图的对应区域
dst = cv2.add(tmp, logo)

# 将修改后的区域重新放回原图
dog[0:200,0:200] = dst

cv2.imshow('dog', dog)
cv2.imshow('dst', dst)
cv2.imshow('tmp', tmp)
cv2.imshow('m', m)
cv2.imshow('mask', mask)
cv2.imshow('logo', logo)
cv2.waitKey(0)
