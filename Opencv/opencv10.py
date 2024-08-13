"""
    Canny边缘检测
    边缘检测基本流程
    1.使用高斯滤波器 平滑图像消除噪声
    2.计算图像中每个像素点的梯度强度和方向
    3.应用非极大值( Non-MaximumSuppression )抑制 以消除边缘检测带来的杂散响应
    4.应用双阈值( Double-Threshold )检测来确定真实的和潜在的边缘
    5.通过抑制孤立的弱边缘最终完成边缘检测

    双阈值 maxVal minVal
    梯度值 > maxVal :则处理为边界
    minVal < 梯度值 < maxVal: 连有边界则保留 否则舍弃
    梯度值 < minVal: 则舍弃

    cv2.Canny(img, minval, maxval)
    maxval 通常大于 minval 并且在实际应用中 典型的做法是 maxval 设置为 minval 的2到3倍。
"""

import cv2
import numpy as np

img = cv2.imread("photo/01.jpg", 0)
v1 = cv2.Canny(img, 80, 150)
v2 = cv2.Canny(img, 50, 100)
res = np.hstack((v1, v2))
cv2.imshow("res", res)
cv2.waitKey(0)
cv2.destroyAllWindows()
# minval 越小 maxval 越小 这样就相当于放松了条件 标准越小
# 表明希望检测出来的边界越多 得到的边界越多
