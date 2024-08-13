# 下面通过一个具体的案例实现图像内黄色信息的识别，并加入滑动条的功能，可以让用户更直观地体验HSV颜色空间。
import cv2

# import numpy as np

# 定义窗口名称
winName = "Colors"


def nothing(x):
    pass


img1 = cv2.imread("photo/HSV.png")

# 颜色空间的转换
img_hsv = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)

# 新建窗口
cv2.namedWindow(winName)


# 新建6个滑动条，表示颜色范围的上下边界，这里滑动条的初始化位置即为黄色的颜色范围
cv2.createTrackbar("LowerbH", winName, 26, 255, nothing)
cv2.createTrackbar("UpperbH", winName, 34, 255, nothing)
cv2.createTrackbar("LowerbS", winName, 42, 255, nothing)
cv2.createTrackbar("UpperbS", winName, 255, 255, nothing)
cv2.createTrackbar("LowerbV", winName, 46, 255, nothing)
cv2.createTrackbar("UpperbV", winName, 255, 255, nothing)

while 1:
    # 函数cv2.getTrackbarPos()范围当前滑块对应的值
    lowerbH = cv2.getTrackbarPos("LowerbH", winName)
    lowerbS = cv2.getTrackbarPos("LowerbS", winName)
    lowerbV = cv2.getTrackbarPos("LowerbV", winName)
    upperbH = cv2.getTrackbarPos("UpperbH", winName)
    upperbS = cv2.getTrackbarPos("UpperbS", winName)
    upperbV = cv2.getTrackbarPos("UpperbV", winName)

    # 得到目标颜色的二值图像，用作cv2.bitwise_and()的掩模
    # cv2.inRange(src,lowerb,upperb):src输入图像，lowerb颜色范围下界，upperb颜色范围上界
    # 在范围内的为白色，不在的为黑色
    img_target = cv2.inRange(
        img1, (lowerbH, lowerbS, lowerbV), (upperbH, upperbS, upperbV)
    )
    cv2.imshow("二值化", img_target)
    # 输入图像与输入图像在掩模条件下按位与，得到掩模范围内的原图像
    img_specifiedColor = cv2.bitwise_and(img1, img1, mask=img_target)

    cv2.imshow(winName, img_specifiedColor)

    if cv2.waitKey(1) == ord("q"):
        break
cv2.destroyAllWindows()
