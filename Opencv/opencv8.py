"""
    形态学操作: 膨胀 腐蚀
    膨胀腐蚀是基于高亮部分(白色)的操作
    膨胀是对高亮部分进行膨胀 类似于“领域扩张”
    腐蚀是高亮部分被腐蚀 类似于“领域被蚕食”
    作用:
        消除噪声
        分割独立元素或连接元素
        寻找图像中的明显极大值、极小值区域
        求图像的梯度
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("photo/08.png")
# 构建卷积核
kernel = np.ones((3, 3), np.uint8)  # 3x3大小范围
# 腐蚀操作
"""
    腐蚀操作原理：
    # kernel = np.ones((3, 3), np.uint8)
    kernel: 这是一个3x3的矩阵 其数据类型为np.uint8
    这个核用于定义腐蚀操作的范围和形状
    使用np.ones创建的矩阵意味着所有的元素都是1 1的话在黑白中是黑色
    在黑色与白色的边缘 3*3正好包含在两边 于是开始腐蚀边缘
    如果卷积核(kernel)变得非常大 那么腐蚀的效果更明显
        在进行腐蚀操作时 核会在输入图像上滑动 并将核覆盖的区域与核进行逐元素的比较
        对于二值图像(元素值为0或1)
        如果核覆盖的所有像素都为1 则目标图像中对应的中心像素点保持1
        如果核覆盖的任何一个像素为0 则目标图像中对应的中心像素点变为0
    cv2.getStructuringElement(shape, ksize, anchor)
        使用示例:
            # 创建一个矩形核，锚点位于左上角
            kernel_rect = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5), anchor=(0, 0))
    shape:
        # 矩形结构元素，这是最常见的选择，所有像素的权重都相等。
        cv2.MORPH_RECT
        # 生成一个椭圆形的核 椭圆结构元素，通常用于图像处理中的各向同性滤波。
        cv2.MORPH_ELLIPSE
        # 生成一个交叉形的核 其形状类似一个“+”号，这种结构元素在处理一些特定类型的噪声或细节时可能很有用。
        cv2.MORPH_CROSS
    anchor(可选):
        结构元素的锚点位置 即结构元素的参考点
        通常是元素的中心 但在某些情况下 你可能希望更改锚点的位置
        它是一个包含两个元素的元组 表示锚点的 x 和 y 坐标
        如果不提供此参数 则默认为元素的中心
    # erosion = cv2.erode(img, kernel, iterations=1)
    img: 这是要进行腐蚀操作的输入图像。
    kernel: 用于腐蚀的核，决定了腐蚀操作的范围和形状。
    iterations=1: 腐蚀操作的迭代次数 这里设置为1 表示腐蚀操作只执行一次
"""
# 腐蚀操作的前提一般要求图片是二值的,如黑白
erosion = cv2.erode(img, kernel, iterations=1)  # 腐蚀操作
# 上图左边是原图 右边是腐蚀结果 将细长的线条处理掉了 同时线条也变细了 (部分白色被腐蚀掉了)
cv2.imshow("erosion", erosion)
cv2.waitKey(0)
cv2.destroyAllWindows()
erosion_1 = cv2.erode(img, kernel, iterations=1)  # 腐蚀操作
erosion_2 = cv2.erode(img, kernel, iterations=2)
erosion_3 = cv2.erode(img, kernel, iterations=3)
plt.subplot(221), plt.imshow(img, "gray"), plt.title("img")
plt.subplot(222), plt.imshow(erosion_1, "gray"), plt.title("one")
plt.subplot(223), plt.imshow(erosion_2, "gray"), plt.title("two")
plt.subplot(224), plt.imshow(erosion_3, "gray"), plt.title("three")
# 显示所有图像
plt.show()

# 膨胀操作 与腐蚀相反
# 膨胀4次
dige_dilate1 = cv2.dilate(img, kernel, iterations=1)
dige_dilate2 = cv2.dilate(dige_dilate1, kernel, iterations=2)
dige_dilate3 = cv2.dilate(dige_dilate2, kernel, iterations=3)
dige_dilate4 = cv2.dilate(dige_dilate3, kernel, iterations=4)

cv2.imshow("dilate", dige_dilate4)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 开运算 闭运算 形态学梯度 顶帽和黑帽
"""
    开运算: 先腐蚀 再膨胀
        开运算能除去孤立的小点 毛刺和小桥 而总的位置和形状不变
        可以清除一些小东西(小的亮斑) 在纤细处分离物体 放大(提亮)局部低亮度的区域
        在平滑大物体边界时 不 明显改变面积
    闭运算: 先膨胀 再腐蚀
        闭运算可以填平小孔(黑色区域) 弥合小裂缝 而总的位置和形状不变
        可以清除小黑点
"""
kernel2 = np.ones((5, 5), np.uint8)
# 开运算
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel2)
res2 = np.hstack((img, opening))
cv2.imshow("opening", res2)
cv2.waitKey(0)
cv2.destroyAllWindows()
# 闭运算
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel2)
res3 = np.hstack((img, closing))
cv2.imshow("closing", res3)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
    梯度运算
        梯度=膨胀-腐蚀
        对二值图可以将团块(blob)边缘凸显出来
        可以用其来保留边缘轮廓
"""
kernel3 = np.ones((3, 3), np.uint8)
dilate = cv2.dilate(img, kernel3, iterations=3)  # 膨胀
erosion = cv2.erode(img, kernel3, iterations=5)  # 腐蚀
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel3)  # 梯度

plt.subplot(221), plt.imshow(img, "gray"), plt.title("img")
plt.subplot(222), plt.imshow(dilate, "gray"), plt.title("dilate")
plt.subplot(223), plt.imshow(erosion, "gray"), plt.title("erosion")
plt.subplot(224), plt.imshow(gradient, "gray"), plt.title("gradient")
# 显示所有图像
plt.show()

"""
    顶帽 = 原始输入 - 开运算结果
        又称'礼帽'
        开运算是先进行腐蚀操作 再进行膨胀操作
        因此 顶帽操作可以得到图像中较暗的小区域 而不考虑更亮的大区域
        顶帽操作通常用于提取图像中的细微细节 小结构或者噪声 使其在更高级的图像处理任务中更易于处理
        在图像处理中 顶帽操作常用于检测图像中的微小物体 微小纹理或者微小的局部变化
        此外 顶帽操作也可以用于图像增强 突出图像中的细节
    黑帽 = 闭运算结果 - 原始输入
        闭运算是先进行膨胀操作 再进行腐蚀操作
        黑帽操作可以得到图像中较亮的小区域 而不考虑更暗的大区域
        黑帽操作通常用于提取图像中的大型结构 背景或者光照不均匀造成的影响
        在图像处理中 黑帽操作常用于检测图像中的大型物体或者大型结构 并进行后续的分析和处理
        此外 黑帽操作也可以用于图像增强 突出图像中的大型结构和背景
"""
kernel4 = np.ones((3, 3), np.uint8)
# 顶帽
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel4)
# 黑帽
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel4)
res4 = np.hstack((tophat, blackhat))
cv2.imshow("res4", res4)
cv2.waitKey(0)
cv2.destroyAllWindows()
