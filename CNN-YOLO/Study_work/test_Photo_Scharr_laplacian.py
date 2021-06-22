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

#Scharr算子
"""
     | -3   0   +3 |                     | -3 -10  -3 |
     |             |                     |            |
Gx = | -10  0  +10 |  *  A    and   Gy = | 0    0   0 |  *  A
     |             |                     |            |
     | -3   0   +3 |                     | +3 +10  +3 |
相比Sobel算子Scharr算子更加敏感
"""
#laplacian算子
"""
     | 0   1   0 | 
     |           |
Gx = | 1  -4   1 |  
     |           | 
     | 0   1   0 |
二阶导算子，相当于一阶导的变化率，对噪音点敏感，通常结合其他方法使用
"""

#Scharr算子和Sobel算子使用一致

#laplacian算子
img = cv2.imread('pi.jpg')
lap = cv2.Laplacian(img,cv2.CV_64F)
cv2.imshow('1',lap)
cv2.waitKey(0)
cv2.destroyAllWindows()