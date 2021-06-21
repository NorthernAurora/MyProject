import cv2
import numpy as np

def main():
    cap = cv2.VideoCapture(0)
    while(cap.isOpened()):
        ret,img = cap.read()
        skinMask = HSVBin(img)
        contours = getContours(skinMask)
        cv2.drawContours(img,contours,-1,(0,255,0),2)
        cv2.imshow('capture',img)
        k = cv2.waitKey(10)
        if k == 27:
            break

def getContours(img):
    kernel = np.ones((5,5),np.uint8)
    closed = cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)
    closed = cv2.morphologyEx(closed,cv2.MORPH_CLOSE,kernel)
    contours,h = cv2.findContours(closed,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)


    vaildContours = []
    for cont in contours:
        if cv2.contourArea(cont)>9000:
            vaildContours.append(cv2.convexHull(cont))
    return  vaildContours

def HSVBin(img):
    hsv = cv2.cvtColor(img,cv2.COLOR_RGB2HSV)

    lower_skin = np.array([100,50,0])
    upper_skin = np.array([125,255,255])

    mask = cv2.inRange(hsv,lower_skin,upper_skin)
    return mask

if __name__ =='__main__':
    main()