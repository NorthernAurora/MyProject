import cv2 #读取格式是BGR
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('moongold.jpg')#读取一张图片
cv2.imshow('image',img)#创建图像窗口
cv2.waitKey(1000)#等待时间(单位毫秒)，输入0意味键入任意键结束
cv2.destroyAllWindows()
print(img.shape)#显示shape
b,g,r=cv2.split(img)#截取通道
print(b)#显示通道
print(b.shape)#显示shape
img = cv2.merge((b,g,r))#组合通道
print(img.shape)

#B.G.R
cur_img = img.copy()
cur_img[:,:,0] = 0#将B设置为0
cur_img[:,:,1] = 0#将G设置为0
cv2.imshow('R',cur_img)#显示图片
#剩下同理


img2 = cv2.imread('moongold.jpg',cv2.IMREAD_GRAYSCALE)#读取灰度图
cv2.imshow('image',img2)#创建图像窗口
cv2.waitKey(1000)
print(img.shape)#显示shape
cv2.imwrite('graygoddess.jpg',img2)#保存图片到本地
moongold = img2[0:50,0:200]#截取图片
cv2.imshow('gold',moongold)
cv2.waitKey(1000)






