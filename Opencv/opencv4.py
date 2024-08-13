"""opencv4 对图像的像素进行处理，加上值使像素变化"""

import cv2

# import numpy as np

img1 = cv2.imread("photo//01.jpg")
# 不安全的加法操作，可能导致溢出
img2 = img1 + 10  # 不会在255进行截断，即190+190=380会变为380-256即为124

# 安全的加法操作，使用 cv2.add 函数
img3 = cv2.add(img1, 10)  # 会在255进行截断，即190+190会变为255

# cv2.imshow("+0", img1)
# cv2.imshow("+10", img2)
img4 = img1 + img2
# cv2.imshow("img4", img4)
# 融合　0.4,0.6相当于权重,0代表偏置向b ,例如 c= x1*0.4+ x2*0.6+b ; x1,x2是两张图片某个点的像素值,c是融合以后的点的像素值
# res = cv2.addWeighted(src1, alpha, src2, beta, gamma)
# 在最后的计算结果上加上一个gamma 通过增加或减少 gamma 的值，可以使混合后的图像变得更亮或更暗。
res = cv2.addWeighted(img1, 0.4, img2, 0.6, 0)
cv2.imshow("res", res)
cv2.waitKey(0)  # 等待时间,毫秒级,0表示可以任意键结束
cv2.destroyAllWindows()
