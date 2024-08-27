import cv2

# 创建VideoWriter对象
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
# 最后一个参数是摄像头采集的分辨率
vw = cv2.VideoWriter('./out.mp4', fourcc, 25, (1280, 720))

# 创建窗口
cv2.namedWindow('video', cv2.WINDOW_NORMAL)
cv2.resizeWindow('video', 640, 360)

# 获取视频设备
cap = cv2.VideoCapture(0) # 默认设备

# 判断摄像头是否为打开状态
while cap.isOpened():
    # 从摄像头读视频帧
    ret, frame = cap.read()

    if ret == True:
        # 将视频帧在窗口显示
        cv2.imshow('video', frame)
        # 重新将窗口设置为指定大小
        cv2.resizeWindow('video', 640, 360)

        # 写数据到多媒体文件
        vw.write(frame)

        # 等待键盘事件，如果为‘q’，退出
        key = cv2.waitKey(10)
        if (key & 0xFF == ord('q')):
            break
    else:
        break

# 释放VideoCapture
cap.release()
vw.release()
cv2.destroyAllWindows()