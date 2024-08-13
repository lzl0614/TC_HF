"""
    openCV3,对图像进行扩充，介绍了五种扩充方法
    cv2.BORDER_REPLICATE 复制法：复制最边缘的像素
    cv2.BORDER_REFLECT 反射法：对感兴趣的图像中的像素在两边进行复制.例如:如|abcdefgh| -> |hgfedcb|abcdefgh|hgfedcb|
    cv2.BORDER_REFLECT_101 反射法：与 BORDER_REFLECT 类似，但在边界处会有一个镜像反转 也就是以最边缘像素为轴，对称
    cv2.BORDER_WRAP 外包装法：复制图像的另一侧像素填充（如|abcdefgh| -> |ghabcdef|abcdefgh|ghabcdef|)
    cv2.BORDER_CONSTANT 常量法：使用常量值填充边框， value=0表示用黑色填充
"""

import cv2
import matplotlib.pyplot as plt

# 读取图像
img = cv2.imread("photo//01.jpg")
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 将img转化为灰度图
# 在 OpenCV 窗口中显示原始图像
cv2.imshow("⚪", img)

# 定义边框尺寸
top_size, bottom_size, left_size, right_size = (50, 50, 50, 50)

# 使用不同的边框类型
# cv2.BORDER_REPLICATE: 复制最边缘的像素值进行填充
replicate = cv2.copyMakeBorder(
    img, top_size, bottom_size, left_size, right_size, borderType=cv2.BORDER_REPLICATE
)
# cv2.BORDER_REFLECT: 边缘像素进行反射填充（如|abcdefgh| -> |hgfedcb|abcdefgh|hgfedcb|）
reflect = cv2.copyMakeBorder(
    img, top_size, bottom_size, left_size, right_size, cv2.BORDER_REFLECT
)
# cv2.BORDER_REFLECT_101: 与 BORDER_REFLECT 类似，但在边界处会有一个镜像反转
reflect101 = cv2.copyMakeBorder(
    img, top_size, bottom_size, left_size, right_size, cv2.BORDER_REFLECT_101
)
# cv2.BORDER_WRAP: 复制图像的另一侧像素填充（如|abcdefgh| -> |ghabcdef|abcdefgh|ghabcdef|）
wrap = cv2.copyMakeBorder(
    img, top_size, bottom_size, left_size, right_size, cv2.BORDER_WRAP
)
# cv2.BORDER_CONSTANT: 使用常量值填充边框， value=0表示用黑色填充
constant = cv2.copyMakeBorder(
    img, top_size, bottom_size, left_size, right_size, cv2.BORDER_CONSTANT, value=0
)

# 将图像从 BGR 转换为 RGB ，以便在 Matplotlib 中正确显示
# OpenCV 读取的图像是 BGR 格式，而 Matplotlib 显示图像需要 RGB 格式
# cv2.COLOR_BGR2RGB 将图像从BRG转化为RBG
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
replicate_rgb = cv2.cvtColor(replicate, cv2.COLOR_BGR2RGB)
reflect_rgb = cv2.cvtColor(reflect, cv2.COLOR_BGR2RGB)
reflect101_rgb = cv2.cvtColor(reflect101, cv2.COLOR_BGR2RGB)
wrap_rgb = cv2.cvtColor(wrap, cv2.COLOR_BGR2RGB)
constant_rgb = cv2.cvtColor(constant, cv2.COLOR_BGR2RGB)

# 使用 Matplotlib 显示原图及其不同的边框效果
# 注意: 如果图像是彩色的，则不需要指定 'gray' 参数
# 注意：如果是灰度图像使用plt.subplot(231), plt.imshow(img_gray, cmap="gray"), plt.title("ORIGINAL")
# 231：2 行 3 列 第1个（从左到右、从上到下按顺序编号）
plt.subplot(231), plt.imshow(img_rgb), plt.title("ORIGINAL")  # 原图
plt.subplot(232), plt.imshow(replicate_rgb), plt.title("REPLICATE")  # 复制填充边框
plt.subplot(233), plt.imshow(reflect_rgb), plt.title("REFLECT")  # 反射填充边框
plt.subplot(234), plt.imshow(reflect101_rgb), plt.title("REFLECT_101")  # 镜像反射填充
plt.subplot(235), plt.imshow(wrap_rgb), plt.title("WRAP")  # 环绕填充边框
plt.subplot(236), plt.imshow(constant_rgb), plt.title("CONSTANT")  # 常量填充边框

# 显示所有图像
plt.show()

# 关闭 OpenCV 窗口
cv2.waitKey(0)
cv2.destroyAllWindows()
