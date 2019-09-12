#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 20:09:26 2019

@author: lx
"""
import numpy as np
import cv2
import detect_clow
import os
import random
#file = 'output/0b333112-4aa2-4263-8ec0-29d2847ef22fid-face-img.txt'
def eman_(l):
    
    l = [float(x) for x in l]
#    x = (l[0] + l [2])/2
#    y = (l[1] + l [3])/2
    return l[0],l[1],l[3]-l[1]

def detect_third(filename):
#    filename = 'upload/0c8fe897-5f64-4913-a079-f9506c944c92id-face-img.jpg'
    image = filename
    file = filename.replace('jpg','txt')

#        file = os.path.join(fold_input,file)
#        image = os.path.join(fold_input,image)
    data = []
    for line in open(file,"r"): #设置文件对象并读取每一行文件
       data.append(line)
    try:
        if image.find('back') == -1:
            region = {}
            index = [eval(data[0])[0],eval(data[1])[0],eval(data[2])[0]]
            zuobiao = [eval(data[0])[1:],eval(data[1])[1:],eval(data[2])[1:]]
            jiaozheng = dict(zip(index,zuobiao))
            p_name = np.array(eman_(jiaozheng['0']))
            p_race = np.array(eman_(jiaozheng['2']))
            p_address = np.array(eman_(jiaozheng['1']))
            p_sex =np.array(((p_name[0] + p_address[0])/2,p_race[1]))
            p_bitrth = np.array(((p_name[0] + p_address[0])/2,2*(p_race[1]-p_name[1])+p_name[1]))
            p_number = np.array(((p_name[0] + p_address[0])/2,2.7*(p_race[1]-p_name[1])+p_address[1]))
            img = cv2.imread(image)
        #    cv2.rectangle(img, (int(p_name[0]+60),int(p_name[1]-10)), (int(p_name[0])+200, int(p_name[1])+25), (0, 255, 0), 2)
            address_regoin = img[int(p_name[1]-10):int(p_name[1])+25,int(p_name[0]+60):int(p_name[0])+200]
        #    address_regoin = cv2.resize(address_regoin, (280, 32))
            region['p_name'] = address_regoin
#                cv2.imwrite(fold +'p_name.png',address_regoin)
#                region.append(address_regoin)
            p_address[2] = int(p_address[2])
            address_regoin = img[int(p_address[1]):int(p_address[1])+int(4.8*p_address[2]),int(p_address[0])+60:int(p_address[0])+320]
#                cv2.imwrite('region/'+str(random.randint(1,10000))+'.png',address_regoin)
            cow = detect_clow.return_cow(address_regoin)
#                if cow == 1:
#            #         cv2.rectangle(img, (int(p_address[0]+60),int(p_address[1])), (int(p_address[0])+320, int(p_address[1])+30), (0, 255, 0), 2)
#                     address_regoin = img[int(p_address[1]):int(p_address[1]+1.5 * p_address[2]),int(p_address[0])+60:int(p_address[0])+320]
#            #         address_regoin = cv2.resize(address_regoin, (280, 32))
#                     cv2.imwrite(fold +'p1address.png',address_regoin)
            if cow == 2:
        #        cv2.rectangle(img, (int(p_address[0]+60),int(p_address[1])), (int(p_address[0])+320, int(p_address[1])+30), (0, 255, 0), 2)
                address_regoin = img[int(p_address[1]):int(p_address[1]+1.5*p_address[2]),int(p_address[0])+60:int(p_address[0])+320]
        #        address_regoin = cv2.resize(address_regoin,(280, 32))
#                    cv2.imwrite(fold +'p1address.png',address_regoin)
                region['p1address'] = address_regoin
        #        cv2.rectangle(img, (int(p_address[0]+60),int(p_address[1])+30), (int(p_address[0])+320, int(p_address[1])+60), (0, 255, 0), 2)
                address_regoin = img[int(p_address[1]+1.5*p_address[2]):int(p_address[1]+3.2*p_address[2]),int(p_address[0])+60:int(p_address[0])+320]
        #        address_regoin = cv2.resize(address_regoin, (280, 32))
#                    cv2.imwrite(fold +'p2address.png',address_regoin)
                region['p2address'] = address_regoin
            else:
        #        cv2.rectangle(img, (int(p_address[0]+60),int(p_address[1])), (int(p_address[0])+320, int(p_address[1])+50), (0, 255, 0), 2)
                address_regoin = img[int(p_address[1]):int(p_address[1]+1.5*p_address[2]),int(p_address[0])+60:int(p_address[0])+320]
        #        address_regoin = cv2.resize(address_regoin,(280, 32))
#                    cv2.imwrite(fold +'p1address.png',address_regoin)
                region['p1address'] = address_regoin
        #        cv2.rectangle(img, (int(p_address[0]+60),int(p_address[1])+50), (int(p_address[0])+320, int(p_address[1])+75), (0, 255, 0), 2)
                address_regoin = img[int(p_address[1]+1.5*p_address[2]):int(p_address[1]+3.2*p_address[2]),int(p_address[0])+60:int(p_address[0])+320]
        #        address_regoin = cv2.resize(address_regoin, (280, 32))
#                    cv2.imwrite(fold +'p2address.png',address_regoin)
                region['p2address'] = address_regoin
        #        cv2.rectangle(img, (int(p_address[0]+60),int(p_address[1])+75), (int(p_address[0])+320, int(p_address[1])+90), (0, 255, 0), 2)
                address_regoin = img[int(p_address[1]+3.2*p_address[2]):int(p_address[1]+4.8*p_address[2]),int(p_address[0])+60:int(p_address[0])+320]
        #        address_regoin = cv2.resize(address_regoin, (280, 32))
#                    cv2.imwrite(fold +'p3address.png',address_regoin)
                region['p3address'] = address_regoin
        #    cv2.rectangle(img, (int(p_address[0]+60),int(p_address[1])), (int(p_address[0])+320, int(p_address[1])+90), (0, 255, 0), 2)
        #    cv2.rectangle(img, (int(p_bitrth[0]-5),int(p_bitrth[1])), (int(p_bitrth[0])+270, int(p_bitrth[1])+30), (0, 255, 0), 2)
#            address_regoin = img[int(p_bitrth[1]):int(p_bitrth[1]+1.5*p_address[2]),int(p_bitrth[0]):int(p_bitrth[0])+270]
            address_regoin1 = img[int(p_bitrth[1]):int(p_bitrth[1])+30,int(p_bitrth[0]+3*p_address[2]):int(p_bitrth[0]+14*p_address[2])]  ####12.5
#                address_regoin2 = img[int(p_bitrth[1]):int(p_bitrth[1])+30,int(p_bitrth[0]+8*p_address[2]):int(p_bitrth[0]+10*p_address[2])]
#                address_regoin3 = img[int(p_bitrth[1]):int(p_bitrth[1])+30,int(p_bitrth[0]+11*p_address[2]):int(p_bitrth[0]+12.5*p_address[2])]
#            emptyImage = np.zeros((int(25),int(10*p_address[2]),3), np.uint8)
#                emptyImage = np.concatenate([address_regoin1,address_regoin2,address_regoin3],axis=1)
        #    address_regoin = cv2.resize(address_regoin, (280, 32))
#                cv2.imwrite(fold +'p_birth.png',address_regoin1 )
            region['p_birth'] = address_regoin1
        #    cv2.rectangle(img, (int(p_number[0]-5),int(p_number[1])), (int(p_number[0])+500, int(p_number[1])+30), (0, 255, 0), 2)
            address_regoin = img[int(p_number[1]-0.5*p_address[2]):int(p_number[1]+2*p_address[2]),int(p_number[0]+8*p_address[2]):int(p_number[0])+500]
        #    address_regoin = cv2.resize(address_regoin, (280, 32))
#                cv2.imwrite(fold +'p_number.png',address_regoin)
            region['p_number'] = address_regoin
        #    cv2.rectangle(img, (int(p_sex[0]-5),int(p_sex[1])), (int(p_sex[0])+220, int(p_sex[1])+25), (0, 255, 0), 2)
            address_regoin1 = img[int(p_sex[1]):int(p_sex[1])+30,int(p_sex[0]+3*p_address[2]):int(p_sex[0]+5*p_address[2])]
            address_regoin2 = img[int(p_race[1]):int(p_race[1])+30,int(p_race[0]+2.7*p_address[2]):int(p_race[0]+5*p_address[2])]
            emptyImage = np.concatenate([address_regoin1,address_regoin2],axis=1)
        #    address_regoin = cv2.resize(address_regoin,(280, 32))
#                cv2.imwrite(fold +'p_sex.png',emptyImage)
            region['p_sex'] = emptyImage
            return region
        elif image.find('face') == -1:
            region = {}
            img = cv2.imread(image)
            index = [eval(data[0])[0],eval(data[1])[0],eval(data[2])[0]]
            zuobiao = [eval(data[0])[1:],eval(data[1])[1:],eval(data[2])[1:]]
            jiaozheng = dict(zip(index,zuobiao))
            p_jiguan = np.array(eman_(jiaozheng['3']))
            p_riqi = np.array(eman_(jiaozheng['4']))
#            p_gonganju = np.array(eman_(jiaozheng['5']))
#                print(index)
            address_regoin = img[int(p_jiguan[1]-5):int(p_jiguan[1]+1.5*p_jiguan[2]),int(p_jiguan[0]+ 5*p_jiguan[2]):int(p_jiguan[0])+370]
        #    address_regoin = cv2.resize(address_regoin, (280, 32))
#                cv2.imwrite(fold +'p_jiguan.png',address_regoin)
            region['p_jiguan'] = address_regoin
            address_regoin = img[int(p_riqi[1]-5):int(p_riqi[1]+1.5*p_riqi[2]),int(p_riqi[0]+5*p_riqi[2]):int(p_riqi[0])+370]
        #    address_regoin = cv2.resize(address_regoin, (280, 32))
#                cv2.imwrite(fold +'p_riqi.png',address_regoin)
            region['p_riqi'] = address_regoin
            return region
        else:
            print('error')
    except:
         print('error')
        
#    cv2.imwrite('cut.jpg',address_regoin)
#    cv2.imshow('img', img)
#    cv2.waitKey(0)
#    cv2.destroyAllWindows()
