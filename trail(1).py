import cv2
import numpy as np


class Build_path(object):
    def __init__(self,colorRange=((110, 240, 180), (123, 255, 255))):
        self.colorRange = colorRange
        self.src = cv2.imread('path.jpg')
        self.mode='rgb'#or rgb
    def __call__(self) :
        bw_Mask = np.zeros_like(self.src)[:, :, 0]
        self.hsv = cv2.cvtColor(self.src, cv2.COLOR_BGR2HSV)
        lower, upper = self.colorRange
        mask = cv2.inRange(self.hsv, lower, upper)
        finalMask = cv2.bitwise_or(bw_Mask, mask)
        self.finalMask=finalMask
        if self.mode=='rgb':
            channels = cv2.split(self.src)
            result = []

            for i in channels:
                result.append(cv2.bitwise_and(i,finalMask))
            dest = cv2.merge(result)
            self.rgbMas=dest
    def img_show(self,img:np.ndarray):
        cv2.imshow('img',img)
        cv2.waitKey(0)
if __name__ == '__main__':
    build_path =Build_path()  # 初始化ColorFilter()对象
    build_path()
