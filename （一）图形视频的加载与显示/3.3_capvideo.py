import cv2

# 创建窗口
cv2.namedWindow('video', cv2.WINDOW_AUTOSIZE)

# 获取视频设备
# cap = cv2.VideoCapture(0) # 默认设备
# 获取视频文件，从视频文件中读取视频帧
cap = cv2.VideoCapture("C:\\Program Files (x86)\\DingDing\\main\\current\\plugins\\tblive\\data\\conf_res\\background_res\\01.mp4")

while True:
    # 从摄像头读视频帧
    ret, frame = cap.read()

    # 将视频帧在窗口显示
    cv2.imshow('video', frame)

    # 等待键盘事件，如果为‘q’，退出
    key = cv2.waitKey(10)
    if (key & 0xFF == ord('q')):
        break

# 释放VideoCapture
cap.release()
cv2.destroyAllWindows()