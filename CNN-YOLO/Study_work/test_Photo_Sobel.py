from pickletools import uint8
from re import A
from textwrap import dedent
from turtle import title
from xmlrpc.server import DocCGIXMLRPCRequestHandler
import cv2 #读取格式是BGR
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import dst
from sklearn.preprocessing import KernelCenterer

#Sobel算子
"""
     | -1  0  +1 |                     | -1 -2  -1 |
     |           |                     |           |
Gx = | -2  0  +2 |  *  A    and   Gy = | 0   0   0 |  *  A
     |           |                     |           |
     | -1  0  +1 |                     | +1 +2  +1 |
Gx实质为通过卷积核反应左右像素点差异，Gy则反应上下像素点差异（若小于0则进行截断操作，即归0，Gx与Gy一致）
"""
img = cv2.imread('pi.jpg',cv2.IMREAD_GRAYSCALE)#彩色图片按照灰度图读入
""" 
dst = cv2.Sobel(img,ddepth,dx,dy,ksize)相应参数

ddepth:图像的深度，默认-1，意为输入与输出一致
dx和dy分别表示水平和竖直方向
ksize:是Sobel算子的大小 
"""
sobel_x = cv2.Sobel(img,cv2.CV_64F,1,0,ksize = 3)#Gx
cv2.imshow('sobel',sobel_x)
cv2.waitKey(1000)
cv2.destroyAllWindows()
#白（255）-> 黑（0）是正数，黑 -> 白 是负数，所有负数会被截断为0，所以要进行一个绝对值操作
sobel_x = cv2.convertScaleAbs(sobel_x)#绝对值操作
cv2.imshow('absx',sobel_x)
cv2.waitKey(1000)
cv2.destroyAllWindows()

sobel_y = cv2.Sobel(img,cv2.CV_64F,0,1,ksize = 3)#Gy
sobel_y = cv2.convertScaleAbs(sobel_y)#绝对值操作
cv2.imshow('absy',sobel_y)
cv2.waitKey(1000)
cv2.destroyAllWindows()
#分别计算x和y，再求和
sobel_xy = cv2.addWeighted(sobel_x,0.5,sobel_y,0.5,0)#0为偏置
cv2.imshow('xy',sobel_xy)
cv2.waitKey(1000)
cv2.destroyAllWindows()

sobel_xy2 = cv2.Sobel(img,cv2.CV_64F,1,1,ksize = 1)
cv2.imshow('xy2',sobel_xy2)
cv2.waitKey(0)
cv2.destroyAllWindows()



