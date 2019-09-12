#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 11:15:14 2019

@author: lx
"""
#x1 = 357.2267
#y1 = 383.7010
#x2 = 353.3857
#y2 = 447.1516
#import math
#b=math.atan2(x2-x1,y2-y1)
#print(b/math.pi*180)
import math
import numpy as np
import math
import cv2
file =  "output/result.txt"
#file = 'output/0b333112-4aa2-4263-8ec0-29d2847ef22fid-face-img.txt'
def eman_(l):
    
    l = [float(x) for x in l]
    x = (l[0] + l [2])/2
    y = (l[1] + l [3])/2
    return x,y
data = []
for line in open(file,"r"): #设置文件对象并读取每一行文件
   data.append(line)
index = [eval(data[0])[0],eval(data[1])[0],eval(data[2])[0]]
zuobiao = [eval(data[0])[1:],eval(data[1])[1:],eval(data[2])[1:]]
jiaozheng = dict(zip(index,zuobiao))
p1 = np.array(eman_(jiaozheng['0']))
p2 = np.array(eman_(jiaozheng['1']))
p4 = np.array(eman_(jiaozheng['2']))
p3=p2-p1
x = p1[0] + (p2[0] - p1[0])/3
k = p3[1]/p3[0]
y = p1[1] + k* (p2[0] - p1[0])/3
p0 = [x , y]
print(p0)
print(p4)
p = p4 - p0
k_s = p[1]/p[0]
angle = 180/math.pi*(math.atan(k_s))
print(angle)
img = cv2.imread('output/result.png')
rows,cols=img.shape[:2]
M = cv2.getRotationMatrix2D((cols/2,rows/2),angle, 1)
#注意此处 为坐标 0,0
dst = cv2.warpAffine(img, M, (cols, rows))
#默认黑色填充
cv2.imshow('img', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()