"""
    本篇主要对图像阈值进行了一些介绍
    图像可以根据灰度差异来分割不同的部分
    阈值化处理的图像一般为单通道图像（灰度图）
    阈值化处理易受光照影响 这点需要注意

    ret, dst = cv2.threshold(src, thresh, mmaxval, type)
        src:输入图像
        dst:输出图像
        thresh : 阈值 0-255 一般选127
        maxval : 超过阈值的像素赋的值 一般选255 由 type 来决定
        type 二值化操作的类型 共5种:
            cv2.THRESH_BINARY 超过阈值( thrash )部分设置为 maxval (最大值) 其他取0   (255为白色 0为黑色)
            cv2.THRESH_BINARY_INV 是 THRESH_BINARY 的反转 超出部分设置为0 其他为 maxval
            cv2.THRESH_TRUNC 大于阈值的部分设为阈值 其他不变化
            cv2.THRESH_TOZERO 大于阈值的部分不改变 其他设为0
            cv2.THRESH_TOZERO_INV 是THRESH_TOZERO的反转 大于阈值部分设为0 其他不改变

    # 自动阈值 cv2.THRESH_OTSU 使用自动阈值第二个参数设为0
    ret, dst = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
"""

import cv2
import matplotlib.pyplot as plt


img = cv2.imread("photo/01.jpg")  # 读取图像
# 使用 plt 进行显示记得讲BGR转化为RGB
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_ary = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 转化为灰度图
# 超过177的为白色 其余为黑色
ret, thresh1 = cv2.threshold(img_ary, 127, 255, cv2.THRESH_BINARY)
# cv2.imshow("thresh1", thresh1)
# 超过177的为黑色 其余为白色 为 THRESH_BINARY 的翻转
ret, thresh2 = cv2.threshold(img_ary, 127, 255, cv2.THRESH_BINARY_INV)
# cv2.imshow("thresh2", thresh2)

# 大于阈值的部分设为阈值 其他不变化
ret, thresh3 = cv2.threshold(img_ary, 127, 255, cv2.THRESH_TRUNC)
# cv2.imshow("thresh3", thresh3)

# 大于阈值的部分不改变 其他设为0
ret, thresh4 = cv2.threshold(img_ary, 127, 255, cv2.THRESH_TOZERO)
# cv2.imshow("thresh4", thresh4)
# 大于阈值的部分设为0 其他设为不变 是THRESH_TOZERO的翻转
ret, thresh5 = cv2.threshold(img_ary, 127, 255, cv2.THRESH_TOZERO_INV)
# cv2.imshow("thresh5", thresh5)
ret, dst = cv2.threshold(img_ary, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow("dst", dst)
titles = ["Original Image", "BINARY", "BINARY_INV", "TRUNC", "TOZERO", "TOZERO_INV"]
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
for i in range(6):
    plt.subplot(2, 3, i + 1), plt.imshow(images[i], "gray")
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()


cv2.waitKey(0)  # 等待时间,毫秒级,0表示可以任意键结束
cv2.destroyAllWindows()
