from xmlrpc.server import DocCGIXMLRPCRequestHandler
import cv2 #读取格式是BGR
import numpy as np
import matplotlib.pyplot as plt

img_cat = cv2.imread('cat.jpg')
img_dog = cv2.imread('dog.jpg')
#print(img_cat)
img_cat2 = img_cat+10
img_cat3 = img_cat + img_cat2#若大于255，则对255取余
img_cat4 = (cv2.add(img_cat,img_cat2))#若大于255则取255，不大于则正常相加

#检查两张图片的shape值是否一样，不一样将会影响一些操作
print(img_cat.shape)#(955, 924, 3)
print(img_dog.shape)#(635, 640, 3)

img_dog2 = cv2.resize(img_dog,(924,955))#对img_dog的shape进行调整，使得两张图的shape值相等
#img_dog = cv2.resize(img_dog,(0,0),fx=1,fy=2)#直接对图像的x，y进行倍数拉伸
#print(img_dog.shape)#检查是否相等

#图像融合 formula：R = (α * X + β * Y + B)  B为偏置，α和β为权重参数
img_cog = cv2.addWeighted(img_dog2,0.4,img_cat,0.6,0)
cv2.imshow('cog',img_cog)#检视融合后的图像
cv2.waitKey(10000)

