import cv2
import numpy as np

cap = cv2.VideoCapture('./vtest.avi')

# mog = cv2.bgsegm.createBackgroundSubtractorMOG()
# 好处，可以计算出阴影部分
# 缺点，会产生很多噪点
# mog = cv2.createBackgroundSubtractorMOG2()

# 好处，可以计算出阴影部分，同时减少了噪点
# 缺点，如果采用默认值，则在开始好长时间内没人作任何信息显示
# 解决办法，调整初始参考帧数量
mog = cv2.bgsegm.createBackgroundSubtractorGMG()

while(True):
    ret, frame = cap.read()
    fgmask = mog.apply(frame)

    cv2.imshow('img', fgmask)

    k = cv2.waitKey(10)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()