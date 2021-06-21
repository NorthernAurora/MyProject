import cv2 #读取格式是BGR
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('moongold.jpg')#读取一张图片
cv2.imshow('image',img)#创建图像窗口
cv2.waitKey(1000)#等待时间(单位毫秒)，输入0意味键入任意键结束
cv2.destroyAllWindows()


#边界填充
top_size,bottom_size,left_size,right_size = (60,60,60,60)#指定填充范围
#填充方法
replicate = cv2.copyMakeBorder(img,top_size,bottom_size,left_size,right_size,borderType=cv2.BORDER_REPLICATE)#复制边缘像素进行填充
reflect = cv2.copyMakeBorder(img,top_size,bottom_size,left_size,right_size,cv2.BORDER_REFLECT)#反射法：对图中像素在两侧进行复制
reflect101 = cv2.copyMakeBorder(img,top_size,bottom_size,left_size,right_size,cv2.BORDER_REFLECT_101)#反射法：以最边缘像素为轴做镜面反射
wrap = cv2.copyMakeBorder(img,top_size,bottom_size,left_size,right_size,cv2.BORDER_WRAP)#外包装法
constant = cv2.copyMakeBorder(img,top_size,bottom_size,left_size,right_size,cv2.BORDER_CONSTANT,value=0)#常量填充法
plt.subplot(231),plt.imshow(img,'gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')

plt.show()