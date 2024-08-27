import cv2  # 导入 OpenCV 库

# 创建一个名为 'new' 的窗口，并设置窗口模式为可调节大小
cv2.namedWindow('new', cv2.WINDOW_NORMAL)

# 将窗口 'new' 的大小调整为 640x480 像素
cv2.resizeWindow('new', 640, 480)

# 显示内容在窗口 'new' 中，这里的参数 0 实际上是不合适的，通常应传入一张图像或一个数组
cv2.imshow('new', 0)

# 等待用户按键，直到有按键按下时才继续执行。返回值是按键的 ASCII 码
key = cv2.waitKey(0)

# 检查按键是否为 'q'
if (key == 'q'):
    exit()  # 如果按下 'q' 键，退出程序

# 关闭所有创建的窗口，释放资源
cv2.destroyAllWindows()