#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 20:19:15 2019

@author: lx
"""

#基于FLANN的匹配器(FLANN based Matcher)定位图片
import numpy as np
import cv2
import os.path
import os
from PIL import Image
#file = os.listdir('images')
#for f in file:
#    if f.find('back') != -1:
sift = cv2.xfeatures2d.SIFT_create()
template_face = cv2.imread('templet/face.jpg',0)
kp_face, des_face = sift.detectAndCompute(template_face,None)
template_back = cv2.imread('templet/back.jpg',0)
kp_back, des_back = sift.detectAndCompute(template_back,None)
def detect_first(fold):
#        time_Take = time.time()
        file = fold
        MIN_MATCH_COUNT = 6 #设置最低特征点匹配数量为10
#        
#        file = 'upload/0b0de7a1-1cdf-4afd-bbfd-bfb4605d76b2id-face-img.jpg'
#    for file in os.listdir(fold):
        if file.find('face') != -1:
            template = template_face # queryImage# queryImage
            kp1, des1 = kp_face, des_face
        else:
            template = template_back
            kp1, des1 = kp_back, des_back 
        file_name = file
#        target = cv2.imread(file_name,0) # trainImage
        # Initiate SIFT detector创建sift检测器
        target_copy = cv2.imread(file_name)
        target = cv2.cvtColor(target_copy, cv2.COLOR_BGR2GRAY)
#        target_copy = cv2.cvtColor(target_copy, cv2.COLOR_BGR2RGB)
        h ,w =  template.shape
        h1 , w1  = target.shape # trainImage

        kp2, des2 = sift.detectAndCompute(target,None)
        #创建设置FLANN匹配
        
        FLANN_INDEX_KDTREE = 0
        index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 3)  ####  5
        search_params = dict(checks = 10)   #####50
        flann = cv2.FlannBasedMatcher(index_params, search_params)
        matches = flann.knnMatch(des1,des2,k=2)
        # store all the good matches as per Lowe's ratio test.
        good = []
        #舍弃大于0.7的匹配
        
        for m,n in matches:
            if m.distance < 0.7*n.distance:
                good.append(m)
        if len(good)>MIN_MATCH_COUNT:
            # 获取关键点的坐标
            src_pts = np.float32([ kp1[m.queryIdx].pt for m in good ]).reshape(-1,1,2)
            dst_pts = np.float32([ kp2[m.trainIdx].pt for m in good ]).reshape(-1,1,2)
            #计算变换矩阵和MASK
            M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
            matchesMask = mask.ravel().tolist()
            # 使用得到的变换矩阵对原图像的四个角进行变换，获得在目标图像上对应的坐标
            pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)
           # pts = np.float32([ [37,100],[37,795],[1145,793],[1145,103] ]).reshape(-1,1,2)
        #    pts = np.float32([ [0,0],[37,795],[1145,793],[1145,103] ]).reshape(-1,1,2)
            dst = cv2.perspectiveTransform(pts,M)
            cv2.polylines(target,[np.int32(dst)],True,0,2, cv2.LINE_AA)
        else:
            print( "Not enough matches are found - %d/%d" % (len(good),MIN_MATCH_COUNT))
            matchesMask = None
        
        pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)
        dst = cv2.perspectiveTransform(pts,M)
        src = dst
        dst1 = np.float32([[0, 0], [h1, 0], [h1, w1], [0, w1]])
        m = cv2.getPerspectiveTransform(src, dst1)
        result = cv2.warpPerspective(target_copy, m, (h1, w1))
        #result = result.T
        result.dtype='uint8'
        result = cv2.flip(result, 1)
        result = cv2.transpose( result)
        result = cv2.flip( result, 0 )
        
#        print(time.time() - time_Take)
        #        cv2.imshow('gray',result)
        result = cv2.resize(result, (553, 350))
    #   (filename,extension) = os.path.splitext(file_name)
#    file = '12346/132345.jpg'
#        filename = os.path.join(file.replace('.jpg','align.jpg'))
        cv2.imwrite(file,result)
        target =  cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
        return target
#        filename = os.path.join('id_card_align',file)
#        cv2.imwrite(filename,result)
#cv2.imshow('gray',img_Eason )
#cv2.waitKey(0)#无限期等待输入
#cv2.destroyAllWindows()

