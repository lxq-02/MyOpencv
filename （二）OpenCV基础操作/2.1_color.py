import cv2

def callback():
    pass

# 色彩空间转换
# 定义一个滑块，同一个滑块对不同色彩空间的效果

cv2.namedWindow('color', cv2.WINDOW_NORMAL)

img = cv2.imread(r'lena.jpg')

# 定义需要转换的颜色空间列表
colorspaces = [cv2.COLOR_BGR2RGBA, cv2.COLOR_BGR2BGRA, cv2.COLOR_BGR2GRAY,
               cv2.COLOR_BGR2HSV_FULL, cv2.COLOR_BGR2YUV]
# 创建Trackbar，用于选择不同的颜色空间
cv2.createTrackbar('curcolor', 'color', 0, len(colorspaces) - 1, callback)


while True:
    # 获得当前trackbar的位置
    index = cv2.getTrackbarPos('curcolor', 'color')

    # 颜色空间转换API
    cvt_img = cv2.cvtColor(img, colorspaces[index])
    # 显示转换后的图像
    cv2.imshow('color', cvt_img)
    key = cv2.waitKey(10)
    if key & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()