from statistics import median
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

#高斯滤波，通过高斯函数构建权重矩阵，像素的影响力受权重矩阵影响

""" img = cv2.GaussianBlur(src, (blur1, blur2), 0)，其中src是要进行滤波的原图像，（blur1，blur2）是高斯核的大小，
blur1和blur2的选取一般是奇数，blur1和blur2的值可以不同。参数0表示标准差取0。
当blur1=blur2=1时，相当于不对原始图像做操作。blur1和blur2越大，图像的模糊程度越大。
但不是blur1和blur2越大越好，blur1和blur2太大，不仅会滤除噪音，还会平滑掉图像中有用的信息。所以blur的选取要进行测试。
如果要进行滤波的图像的长宽比大致为1:1，那么选取blur时，一般设置blur1=blur2。
如果要进行滤波的图像的长宽比大致为m:n，那么选取blur时，blur1:blur2=m:n """

aussian = cv2.GaussianBlur(img_z,(5,5),1)
cv2.imshow('aus',aussian)
cv2.waitKey(1000)
cv2.destroyAllWindows()

#中值滤波
medians = cv2.medianBlur(img_z,5)#取中间值作为平滑处理值
cv2.imshow('med',medians)
cv2.waitKey(1000)
cv2.destroyAllWindows()

#展示效果
res = np.vstack((img_z,aussian,medians))#竖向拼接，hstack为横向拼接
print(res)
cv2.imshow('aussian and medians',res)
cv2.waitKey(1000)
cv2.destroyAllWindows()

