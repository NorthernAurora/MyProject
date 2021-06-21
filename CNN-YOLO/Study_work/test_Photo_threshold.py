from turtle import title
from xmlrpc.server import DocCGIXMLRPCRequestHandler
import cv2 #读取格式是BGR
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import dst

img = cv2.imread('moongold.jpg')#读取一张图片
img_gray = cv2.imread('graygoddess.jpg')

#ret,dst = cv2.threshold(src,thresh,maxval,type)格式
#src：输入图，只能输入单通道，通常来说是灰度图
#dst：输出图
#thresh：阈值
#maxval：当像素值超过了阈值（或小于阈值，根据type来决定），所赋予的值
#type：二值化操作的类型，包含一下5种类型：cv2.THRESH_BINARY； cv2.THRESH_BINARY_INV； cv2.THRESH_TRUNC； cv2.THRESH_TOZERO；cv2.THRESH_TOZERO_INV
ret, thresh1 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)#设定一个阈值与MAX值，超过阈值则取到MAX值，小于阈值则取到0
ret, thresh2 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY_INV)#上条方法的反转
ret, thresh3 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_TRUNC)#大于阈值部分取到阈值，否则不做出改变
ret, thresh4 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_TOZERO)#大于阈值部分不变，否则取到0
ret, thresh5 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_TOZERO_INV)#上条方法的反转

titles = ['Original Image', 'BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
imges = [img,thresh1,thresh2,thresh3,thresh4,thresh5]

for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(imges[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()


