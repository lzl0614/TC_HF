"""
    openCV对图像视频的高级处理
    边缘检测技术(带方向的)——图像梯度=sobel算子/scharr算子/laplasian算子
    三种算子原理参照 photo/09-1.png
    dst = cv2.Sobel(src, ddepth, dx, dy, ksize)
    src: 图像
    ddepth: 图像的深度 传递-1表示输出图像与输入图像具有相同的深度
            推荐 cv2.CV_64F 指定输出图像的数据类型为 64位浮点数  避免信息丢失
            (Sobel操作可能产生负值 而普通的8位无符号整数(0到255)无法表示负值)
    dx 和 dy 分别表示水平和竖直方向求导的阶数
    ksize 是 Sobel 算子的大小 必须是1、3、5或7。核的大小影响边缘检测的细节级别
"""

import cv2
import numpy as np

# import numpy as np

# 原始图片
img = cv2.imread("photo/09.png", cv2.IMREAD_GRAYSCALE)  # IMREAD_GRAYSCALE 灰度图像显示
cv2.imshow("img", img)
cv2.waitKey()
cv2.destroyAllWindows()
# x水平方向
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)  # ksize必须为1,3,5,7
# 只显示一半是因为另一半是负值 后面取绝对值后显示完整
cv2.imshow("sobelx", sobelx)
cv2.waitKey()
cv2.destroyAllWindows()
"""
CV_8UC1,CV_8SC1,CV_32FC1

如果你现在创建了一个存储--灰度图片的Mat对象,这个图像的大小为宽100,高100,
那么,现在这张灰度图片中有10000个像素点 它每一个像素点在内存空间所占的空间大小是8bite,
8位--所以它对应的就是CV_8。

S|U|F:
S--代表---signed int---有符号整形
U--代表--unsigned int--无符号整形
F--代表--float---------单精度浮点型

C<number_of_channels>----代表---一张图片的通道数,比如:
channels = 1: 灰度图片--grayImg---是--单通道图像
channels = 3: RGB彩色图像---------是--3通道图像
channels = 4: 带Alph通道的RGB图像--是--4通道图像
    Alpha 通道的每个像素可以存储透明度信息，范围通常是从 0(完全透明)到 255完全不透明)

例:CV_8UC1 指的是 8 位无符号( U )整数的单通道( C1 )数据类型

imshow函数在显示图像时 会将各种类型的数据都映射到[0, 255]。
如下:
·  如果载入的图像是8位无符号类型(8-bit unsigned) 就显示图像本来的样子。
·  如果图像是16位无符号类型(16-bit unsigned)或32位整型(32-bit integer 有符号位) 便用像素值除以256。
        也就是说 该值的范围是 [0,255 x 256]映射到[0,255]。
·  如果图像是32位或64位浮点型(32-bit floating-point or 64-bit floating-point) 像素值便要乘以255。
        也就是说 该值的范围是 [0,1]映射到[0,255]。

 如: CV_8U的灰度或BGR图像的颜色分量都在0~255之间。直接imshow可以显示图像
 CV_32F或者CV_64F取值范围为0~1.0 imshow的时候会把图像乘以255后再显示。
"""

# 图像外圈是黑像素相减0-0 里面白色内圈是白色像素相减255-255 都没有颜色梯度
# 左边边界是255-0 白色到黑色 所以最后显示白色
# 白到黑是正数 黑到白是负数 负数会被截断为0(如果是-1，-50这些 就会变成0) 所以要取绝对值
sobelx = cv2.convertScaleAbs(sobelx)  # 将Sobel结果转换为正值并改为 uint8 类型
cv2.imshow("sobelx", sobelx)
cv2.waitKey()
cv2.destroyAllWindows()
"""
    在经过处理后 使用convertScaleAbs()函数将其转换回原来的uint8形式
    否则无法显示图像 而只是一副灰色的窗口
"""
# y竖直方向
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
sobely = cv2.convertScaleAbs(sobely)
cv2.imshow("sobely", sobely)
cv2.waitKey()
cv2.destroyAllWindows()

"""
    应用 相当于画轮廓
"""
# 示例
img1 = cv2.imread("photo/01.jpg", cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("photo/02.png", cv2.IMREAD_GRAYSCALE)
sobelx1 = cv2.Sobel(img1, cv2.CV_64F, 1, 0, ksize=3)
sobelx1 = cv2.convertScaleAbs(sobelx1)
sobely1 = cv2.Sobel(img1, cv2.CV_64F, 0, 1, ksize=3)
sobely1 = cv2.convertScaleAbs(sobely1)
# 融合 权重为各0.5 最后结果无另加值 gamma为0
sobelxy = cv2.addWeighted(sobelx1, 0.5, sobely1, 0.5, 0)
cv2.imshow("sobelxy", sobelxy)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
    Sobel 算子虽然可以有效地提取图像边缘 但是对图像中较弱的边缘 (不明显的) 提取效果较差
        原因
            Sobel 算子在计算相对较小的核的时候，其 * 式计算导致的精度比较低
            例如一个3 * 3的 Sobel 算子 在梯度角度接 * 水平或垂直方向时 其不精确性就很明显
    Scharr 算子是对 Sobel 算子差异性的增强 两者之间的在检测图像边缘的原理和使用方式上相同
    但是 Scharr 算子的主要思路是通过将模板中的权重系数放大来增大像素间的差异
    Scharr 算子又称为 Scharr 滤波器 也是计算 x 或 y 方向上的图像差分 在openCV中主要是配合Sobel算子的运算而存在
"""

scharrx = cv2.Scharr(img1, cv2.CV_64F, 1, 0)
scharry = cv2.Scharr(img1, cv2.CV_64F, 0, 1)
scharrx = cv2.convertScaleAbs(scharrx)
scharry = cv2.convertScaleAbs(scharry)
scharrxy = cv2.addWeighted(scharrx, 0.5, scharry, 0.5, 0)
# 拉普拉斯 Laplacian: 先过滤噪声 再进行边缘检测
laplacian = cv2.Laplacian(img1, cv2.CV_64F)
laplacian = cv2.convertScaleAbs(laplacian)
res = np.hstack((sobelxy, scharrxy, laplacian))
cv2.imshow("res", res)
cv2.waitKey()
cv2.destroyAllWindows()
"""
    LOG算子 即拉普拉斯-高斯算子( Laplacian of Gaussian ) 是用于图像边缘检测的经典方法之一
    它结合了高斯平滑( Gauss )与拉普拉斯变换( Laplacian ) 以减少噪声对边缘检测的影响 同时增强边缘信息
    首先对图像进行高斯滤波 然后再求其拉普拉斯二阶导数 根据二阶导数的过零点来检测图像的边界
    即通过检测滤波结果的零交叉来获得图像或物体的边缘
    它具有抗干扰能力强 边界定位精度高 边缘连续性好 能有效提取对比度弱的边界等特点
"""

# 1. 使用高斯滤波器平滑图像，减少噪声
# 参数(3, 3)为高斯核的大小，0表示根据高斯核自动计算标准差
blurred_img = cv2.GaussianBlur(img1, (3, 3), 0)

# 2. 对平滑后的图像进行拉普拉斯变换
log = cv2.Laplacian(blurred_img, cv2.CV_64F)
# 3. 将结果转换为8位无符号整数，并取绝对值
log = cv2.convertScaleAbs(log)
# 显示或保存结果
cv2.imshow("Laplacian of Gaussian", log)
cv2.waitKey(0)
cv2.destroyAllWindows()
