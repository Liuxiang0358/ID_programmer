# -*- coding: utf-8 -*-

import cv2 as cv
 
# 读入原图片
img = cv.imread('back1.jpg')
# 打印出图片尺寸
print(img.shape)
# 将图片高和宽分别赋值给x，y
x, y = img.shape[0:2]
 
# 显示原图
# 缩放到原来的二分之一，输出尺寸格式为（宽，高）
#img_test1 = cv.resize(img, (int(y / 2), int(x / 2)))

 
# 最近邻插值法缩放
# 缩放到原来的四分之一
img_test2 = cv.resize(img, (0, 0), fx=0.25, fy=0.25, interpolation=cv.INTER_NEAREST)
cv.imwrite('back.jpg', img_test2)

