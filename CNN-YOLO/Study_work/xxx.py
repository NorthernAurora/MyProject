from pickletools import uint8
from turtle import title
from xmlrpc.server import DocCGIXMLRPCRequestHandler
import cv2 #读取格式是BGR
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import dst
from sklearn.preprocessing import KernelCenterer

#开运算cv2.MORPH_OPEN
img_o = cv2.imread('corrosion.jpg')
kernel = np.ones((5,5),np.uint8)
#形态学表达式

opening = cv2.morphologyEx(img_o,cv2.MORPH_OPEN,kernel)
cv2.imshow('opening',opening)
cv2.waitKey(0)
cv2.destroyAllWindows()