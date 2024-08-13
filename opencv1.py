"""openCV第一节 本篇介绍了一些简单的图像处理 包括图片的读取 类型转换 区域选取 放大缩小 RGB分割 图像保存 等"""

import cv2
import numpy as np

# 读取图片
img1 = cv2.imread("photo//01.jpg")
print("长宽和图片类型", img1.shape)  # 输出(hwc)长宽和图片类型
print("图片类型", img1.dtype)  # 输出图片类型,如dtype('uint8')
# 输出读取数据类型，通过 cv2.imread() 读取的图像通常输出numpy.ndarray
print("读取数据类型", type(img1))
print("像素点大小", img1.size)  # 输出像素点大小,总像素点大小为559872
# 可以混合多张图片展示,图片的通道数要相同，灰度通道为1，彩色为3 （RGB）
res1 = np.hstack((img1, img1))
# cv2.imshow("两张", res1) # 展示图片

# IMREAD_GRAYSCALE 灰度图像 IMREAD_COLOR 彩色图像
img2 = cv2.imread("photo//01.jpg", cv2.IMREAD_GRAYSCALE)  # 读取图片转化为灰度图
# img2 = cv2.imread("photo//01.jpg", 0) 值为0也是灰度图
img3 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)  # 将img2转化为灰度图
res2 = np.hstack((img2, img3))
# cv2.imshow("灰度图", res2) # 展示图片
# 截取图像中感兴趣区域
roi = img1[0:200, 0:200]  # 截取宽像素0-50,长像素0-200的位置 0，0为左上角
# 打印图像形状 这里打印的roi的，所以是 (200, 200, 3) 3表示 r g b 3个通道
print("roi图像形状", roi.shape)
b, g, r = cv2.split(img1)  # 切分
img4 = cv2.merge((b, g, r))  # 组合
# 打印b通道图像形状 这里打印的单通道的，所以是(432, 432) 表示 b 1个通道
print("b通道图像形状", b.shape)
# 修改颜色通道是在通向上进行处理，为了不破坏原图像，所以这里要建立一个副本
cur_imgr = img1.copy()
cur_imgr[:, :, 0] = 0  # 将图像的蓝色通道全部设为 0（第一个通道b，所以为[:,:,0]）
cur_imgr[:, :, 1] = 0  # 将图像的绿色通道全部设为 0
# cv2.imshow("R", cur_imgr)  # 展示图片

cur_imgg = img1.copy()
cur_imgg[:, :, 0] = 0  # 将图像的蓝色通道全部设为 0
cur_imgg[:, :, 2] = 0  # 将图像的红色通道全部设为 0
# cv2.imshow("G", cur_imgg)  # 展示图片

cur_imgb = img1.copy()
cur_imgb[:, :, 1] = 0  # 将图像的绿色通道全部设为 0
cur_imgb[:, :, 2] = 0  # 将图像的红色通道全部设为 0
# cv2.imshow("B", cur_imgb)  # 展示图片
# 拼接三张一起展示
res3 = np.hstack((cur_imgr, cur_imgg, cur_imgb))
# cv2.imshow("RGB", res3)  # 展示图片
img5 = cv2.resize(img1, (800, 411))  # 对图像进行放大处理，指定大小
# cv2.imshow("放大后", img5)  # 展示图片
# 这样是2倍的长宽扩大,像素数量会增多，从原来的（432，432）变为（864，864）
img6 = cv2.resize(img1, (0, 0), fx=2, fy=2)
cv2.imshow("二倍", img6)  # 展示图片
print("二倍图像形状", img6.shape)

cv2.waitKey(0)  # 等待时间,毫秒级,0表示可以任意键结束
cv2.destroyAllWindows()

# 保存图片
save_path = "L:/vscode/RGB.jpg"  # 指定保存路径和文件名
cv2.imwrite(save_path, res3)
