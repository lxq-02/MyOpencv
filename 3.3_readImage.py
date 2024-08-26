import cv2

cv2.namedWindow('3.3_image', cv2.WINDOW_NORMAL)
img = cv2.imread('D:/0.jpg')

while True:
    cv2.imshow('3.3_image', img)

    key = cv2.waitKey(0)

    # waitKey返回值是16位，取最后8位
    if (key & 0xFF == ord('q')):
        print(123)
        break
    elif (key & 0xFF == ord('s')):
        print('sss')
        # 当用户点击s时，保存为1.jpg
        cv2.imwrite('D:\\1.jpg', img)
    else:
        print('other')
cv2.destroyAllWindows()