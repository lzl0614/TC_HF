""""
    图像的平滑处理 主要介绍了图像的滤波方式
    高频: 图像中变化剧烈的部分
    低频: 图像中变化缓慢 平坦的部分
    根据图像的高低频特征 设置高通和低通滤波器 高通滤波可以检测图像中尖锐变化明显的部分
        低通滤波可以让图像变得平滑 消除噪声干扰
    低通滤波部分 (图像平滑去噪)
    高通部分 (边缘检测)
    主要滤波方式
        线性滤波: 均值滤波 方框滤波 高斯滤波
        非线性滤波: 中值滤波
"""

import cv2
import numpy as np

img = cv2.imread("photo/01.jpg")
# 均值滤波 -----选取指定大小方框内的平均值
blur = cv2.blur(img, (3, 3))
# 取 3*3的数据 进行累加均值求和 可以看到下面图片左边噪声明显 右边是用均值滤波平滑处理的结果
res1 = np.hstack((img, blur))
# cv2.imshow("res1", res1)


# 方框滤波 -----基本和均值一样 可以选择归一化
# 归一化 (3,3)的9个数加起来/9 是True的情况 和均值滤波基本一样
box1 = cv2.boxFilter(img, -1, (3, 3), normalize=True)
# 不选择归一化 是False的情况 则是不/9 那么容易越界 相加的和如果大于255 则会被定为255(白色)
box2 = cv2.boxFilter(img, -1, (3, 3), normalize=False)
res2 = np.hstack((img, box1, box2))
# cv2.imshow("res2", res2)


# 高斯滤波 -----高斯模糊的卷积核里的数值是满足高斯分布的 相当于更重视中间的
aussian = cv2.GaussianBlur(img, (3, 3), 1)
# 在(3*3)中 更重视正离中间更近的 75 113 104 24 的值 给权重0.8 离得比较远的四个角点的值121 78 235 154  给权重0.6
# 计算为 [204 + (121+78+154+235)*0.6 + (75+113+104+24)*0.8]/9
"""
    121  75  78
     24 204 113
    154 104 235
"""
res3 = np.hstack((img, aussian))
# cv2.imshow("res3", res3)


# 中值滤波-----相当于用中间值代替 上面(3*3)里面  24 75 78 104   113  121 154 204 235
# 中值滤波直接选用九个值的中间值 113
median = cv2.medianBlur(img, 5)
res4 = np.hstack((img, median))
# cv2.imshow("res4", res4)

res5 = np.hstack((blur, aussian, median))

cv2.imshow("res5", res5)
cv2.waitKey(0)  # 等待时间,毫秒级,0表示可以任意键结束
cv2.destroyAllWindows()
