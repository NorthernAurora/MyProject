from pickletools import uint8
from turtle import title
from xmlrpc.server import DocCGIXMLRPCRequestHandler
import cv2 #读取格式是BGR
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import dst
from sklearn.preprocessing import KernelCenterer

#腐蚀操作
img_corrosion = cv2.imread('corrosion.jpg')
cv2.imshow('corrosion',img_corrosion)
cv2.waitKey(1000)
cv2.destroyAllWindows()

kernel = np.ones((5,5),np.uint8)#返回一个x*x的二维数组作为范围
print(kernel)
corrosion = cv2.erode(img_corrosion, kernel, iterations = 3)#iterations为迭代次数
cv2.imshow('corrosion',corrosion)
cv2.waitKey(1000)
cv2.destroyAllWindows()

#膨胀操作dilate

kernel = np.ones((5,5),np.uint8)
inflation = cv2.dilate(corrosion,kernel,iterations=3)
cv2.imshow('inflation',inflation)
cv2.waitKey(1000)
cv2.destroyAllWindows()

#开运算cv2.MORPH_OPEN先腐蚀，再膨胀
img_o = cv2.imread('corrosion.jpg')
kernel = np.ones((5,5),np.uint8)
#形态学表达式
opening = cv2.morphologyEx(img_o,cv2.MORPH_OPEN,kernel,iterations=3)
cv2.imshow('opening',opening)
cv2.waitKey(1000)
cv2.destroyAllWindows()
""" （１）开运算能够除去孤立的小点，毛刺和小桥，而总的位置和形状不便。
    （２）开运算是一个基于几何运算的滤波器。
    （３）结构元素大小的不同将导致滤波效果的不同。
    （４）不同的结构元素的选择导致了不同的分割，即提取出不同的特征。 
"""


#闭运算cv2.MORPH_CLOSE先膨胀，再腐蚀
img_c = cv2.imread('corrosion.jpg')
kernel = np.ones((5,5),np.uint8)
#形态学表达式
closeing = cv2.morphologyEx(img_c,cv2.MORPH_CLOSE,kernel,iterations=3)
cv2.imshow('closeing',closeing)
cv2.waitKey(1000)
cv2.destroyAllWindows()
""" （1）闭运算能够填平小湖（即小孔），弥合小裂缝，而总的位置和形状不变。
    （2）闭运算是通过填充图像的凹角来滤波图像的。
    （3）结构元素大小的不同将导致滤波效果的不同。
    （4）不同结构元素的选择导致了不同的分割。
"""

#梯度运算cv2.MORPH_GRADIENT
#梯度 = 膨胀 - 腐蚀
img_p = cv2.imread('pi.jpg')
kernel = np.ones((7,7),np.uint8)
dilate_2 = cv2.dilate(img_p,kernel,iterations = 3)#膨胀，执行3次
corrosion_2 = cv2.erode(img_p,kernel,iterations = 3)#腐蚀，执行3次
res_2 = np.hstack((dilate_2,corrosion_2))
cv2.imshow('res',res_2)
cv2.waitKey(1000)
#cv2.MORPH_GRADIENT
cv2.destroyAllWindows()
gradients = cv2.morphologyEx(img_p,cv2.MORPH_GRADIENT,kernel)#形态学函数内进行cv2.MORPH_GRADIENT
cv2.imshow('gra',gradients)
cv2.waitKey(1000)
cv2.destroyAllWindows()


#礼帽 & 黑帽
#礼帽 = 原始输入 - 开运算 cv2.MORPH_TOPHAT
#黑帽 = 闭运算 - 原始输入

#礼帽 cv2.MORPH_TOPHAT
img_h = cv2.imread('corrosion.jpg')
kernel = np.ones((11,11),np.uint8)
tophat = cv2.morphologyEx(img_h,cv2.MORPH_TOPHAT,kernel)
cv2.imshow('th',tophat)
cv2.waitKey(1000)
cv2.destroyAllWindows()

#黑帽 cv2.MORPH_BLACKHAT
blackhat = cv2.morphologyEx(img_h,cv2.MORPH_BLACKHAT,kernel)
cv2.imshow('bh',blackhat)
cv2.waitKey(0)
cv2.destroyAllWindows()


