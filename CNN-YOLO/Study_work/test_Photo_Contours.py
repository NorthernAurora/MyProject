from pickletools import uint8
from re import A
from textwrap import dedent
from turtle import shape, title
from xmlrpc.server import DocCGIXMLRPCRequestHandler
import cv2 #读取格式是BGR
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import dst
from sklearn.preprocessing import KernelCenterer

#轮廓检测
#基本结构：cv2.findContours(img,mode,method)
""" 
mode:轮廓检索模式
    RETR_EXTERNAL:只检索最外面的轮廓
    RETR_LIST:检索所有的轮廓，并将其保存到一条链表当中
    RETR_CCOMP:检索所有轮廓，并将他们组织为两层，顶层是各部分的外部边界，第二层是空洞的边界
    RETR_TREE:检索所有轮廓，并重构嵌套轮廓的整个层次
method：轮廓逼近方法
    CHAIN_APPROX_NONE:以Freeman链码的方式输出轮廓，所有其他发发输出多边形(顶点和序列)
    CHAIN_APPROX_SIMPLE:压缩水平的、垂直的和倾斜的部分，也就是说，函数只保留他们重点的部分 
"""

img = cv2.imread('sea.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#转化为灰度图
ret,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)#转换为二值图
#cv2.imshow('1',thresh)
#cv2.waitKey(1000)
#cv2.destroyAllWindows()
contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)#边缘检测，contours存储轮廓点，hierarchy存储图像层级
draw_img = img.copy()#复制一张图片，否则用原图做修改会导致原图变化
res = cv2.drawContours(draw_img,contours,-1,(0,0,255),2)
cv2.imshow('11',res)
cv2.waitKey(0)
cv2.destroyAllWindows()
