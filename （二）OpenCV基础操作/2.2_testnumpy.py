import numpy as np
import cv2

# # 通过array定义矩阵
# a = np.array([1, 2, 3])

# b = np.array([[1, 2, 3], [4, 5, 6]])

# print(a)
# print(b)

# # 高         宽
# # 行的个数， 列的个数， 通道数/层数
# # np.uint8 矩阵中的数据类型
# # opencv中是8*8的3个
img = np.zeros((480, 640, 3), np.uint8)
# print(c)

# # 定义ones矩阵，默认1个通道
# d = np.ones((8, 8), np.uint8)
# print(d)


# # 定义full矩阵
# e = np.full((8, 8), 255, np.uint8)
# print(e)

# # 定义单位矩阵identity
# # 斜对角为1，其他为0
# f = np.identity(4)
# print(f)

# # 定义eye矩阵
# g = np.eye(5, 7, k = 3)
# print(g)

# # 检索图片中的某个值
# print(img[100, 100])
# count = 0
# while count < 200:
#     #BGR 分三层，以下是两种写法
#     img[count, 100, 0] = 255
#     img[count, 100] = [0, 0, 255]
#     count = count + 1

# 子矩阵
roi = img[100:400, 100:600]
roi[:,:] = [0,0,255]
roi[10:100,10:200] = [0, 255, 0]

cv2.imshow('img', roi)
while True:
    key = cv2.waitKey(0)

    if (key & 0xFF == ord('q')):
        cv2.destroyAllWindows()
        break