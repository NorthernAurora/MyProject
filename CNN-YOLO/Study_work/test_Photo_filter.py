from turtle import title
from xmlrpc.server import DocCGIXMLRPCRequestHandler
import cv2 #读取格式是BGR
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import dst

img_z = cv2.imread('zaodian.jpg')#读取一张噪点图
cv2.imshow('img',img_z)
cv2.waitKey(1000)
cv2.destroyAllWindows()

img_zb = cv2.blur(img_z,(3,3))#进行一个均值滤波
cv2.imshow('blur',img_zb)
cv2.waitKey(1000)
cv2.destroyAllWindows()

#方块滤波
#-1表示输出的处理后图像与原图像在颜色通道上是一致的，normalize决定是否进行归一化，因为方块滤波容易产生越界，一旦选择进行归一化则与均值滤波无明显差异
box_T = cv2.boxFilter(img_z,-1,(3,3),normalize=True)
cv2.imshow('bft',box_T)
cv2.waitKey(1000)
cv2.destroyAllWindows()
#不进行归一化，对越界像素一律取到255
box_F = cv2.boxFilter(img_z,-1,(3,3),normalize=False)
cv2.imshow('bff',box_F)
cv2.waitKey(1000)
cv2.destroyAllWindows()





