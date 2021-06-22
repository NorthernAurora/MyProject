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

img = cv2.imread('sea.jpg')
#print(img.shape)
up_down = cv2.pyrDown(img)#下采样，上采样为pyrUp()
cv2.imshow('down',up_down)
cv2.waitKey(1000)
cv2.destroyAllWindows()

#拉普拉斯金字塔
down_l = cv2.pyrDown(img)
#print(down_l.shape)
down_up = cv2.pyrUp(down_l)
down_up = cv2.resize(down_up,(1279,720))
#print(down_up.shape)
l_l = img-down_up
cv2.imshow('l',l_l)
cv2.waitKey(0)
cv2.destroyAllWindows()