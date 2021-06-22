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

#Canny边缘检测
""" 
1)使用高斯滤波，以平滑图像，滤除噪声
2)计算图像中每个像素点的梯度强度和方向(Sobel算子)
3)应用非极大值抑制(Non-Maximum Suppression)，以消除边缘检测带来的杂散响应
4)应用双阈值(Double-Threshold)检测来确定真实的和潜在的边缘。
5)通过抑制孤立的弱边缘最终完成边缘检测 
"""

img = cv2.imread('sea.jpg',cv2.IMREAD_GRAYSCALE)
img_v = cv2.Canny(img,50,70)#差值越小越敏感
cv2.imshow('c',img_v)
cv2.waitKey(0)
cv2.destroyAllWindows()

