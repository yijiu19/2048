import cv2
import win32api


def cvview(event):
    # 加载摄像头
    cap = cv2.VideoCapture(0)
    # 设置背景帧
    _, first_frame = cap.read()
    previous_gray = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)
    # 初始化检测点
    previous_points = cv2.goodFeaturesToTrack(previous_gray, maxCorners=10, qualityLevel=0.01, minDistance=30, blockSize=3)

    # 循环检测
    while True:
        # 读取摄像头
        _, frame = cap.read()
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # 计算光流
        new_points, status, error = cv2.calcOpticalFlowPyrLK(previous_gray, gray_frame, previous_points, None)

        # 得到移动点
        x_movement, y_movement = 0, 0
        for i, (new, old) in enumerate(zip(new_points, previous_points)):
            a, b = new.ravel()
            c, d = old.ravel()
            x_movement += (a - c)
            y_movement += (b - d)
        if x_movement > 80:
            pass
            win32api.keybd_event(65, 0, 0, 0)
            # return "a"
        elif x_movement < -80:
            pass
            win32api.keybd_event(68, 0, 0, 0)
            # return "d"

        # 更新前一帧
        previous_gray = gray_frame.copy()
        previous_points = new_points.reshape(-1, 1, 2)

        # 释放摄像头
    cap.release()
    cv2.destroyAllWindows()
