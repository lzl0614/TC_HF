"""openCV第一节 本篇介绍了对视频的简单处理"""

import cv2

# cap = cv2.VideoCapture(0)  # 从摄像头读取内容 0为摄像头编号，只有一个摄像头即为0
cap = cv2.VideoCapture("vedio/2.mp4")  # 从视频读取内容

if cap.isOpened():
    oepn, frame = cap.read()  # cap2.read代表视频从第一帧开始一帧一帧的开始读
    print("读取成功")
    # oepn是Boolean类型,返回true 或false  frame表示帧的结果,即为图像
else:
    open = False
    print("读取失败")

# cap.grap()  # 从设备或者视频上获取一帧,获取成功返回true
# cap.retrieve(frame)  # 在grap()后使用,对获取到的帧进行解码 ,也返回true或者false
# cap.read(frame)  # 结合grap和retrieve的功能,抓取下一帧并解码
while open:
    ret, frame = cap.read()
    if frame is None:  # 如果读取第一帧是否为空
        break
    if ret is True:
        # 最简单的操作,把视频每一帧图片转换为灰度图
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("展示的名字", gray)
        # 27代表键盘的退出键esc,视频展示的时候可以按esc退出
        if cv2.waitKey(100) & 0xFF == 27:
            break
cap.release()
cv2.destroyAllWindows()
