import cv2 #读取格式是BGR
import numpy as np
import matplotlib.pyplot as plt

vc = cv2.VideoCapture('goddess.mp4')#可调用摄像头，0为默认摄像头，读取视频则需指定路径
if vc.isOpened():#检查视频是否可以正常打开
    open,farme = vc.read()#open为bool量，判断能否打开，farme为当前帧数图像
else:
    open = False
while open:
    ret,frame = vc.read()
    if frame is None:
        break
    if ret == True:
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('result',gray)
        if cv2.waitKey(10) & 0xFF == 27:#27意为键入ESC退出
            break
vc.release()
cv2.destroyAllWindows()

