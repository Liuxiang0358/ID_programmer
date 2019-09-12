#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 10:00:36 2019

@author: lx
"""
dict_ = {'壮': '6',
 '藏': '17',
 '裕固': '12,8',
 '彝': '18',
 '瑶': '14',
 '锡伯': '13,7',
 '乌孜别克': '4,7,7,7',
 '维吾尔': '11,7,5',
 '佤': '6',
 '土家': '3,10',
 '土': '3',
 '塔塔尔': '12,12,5',
 '塔吉克': '12,6,7',
 '水': '4',
 '畲': '12',
 '撒拉': '15,8',
 '羌': '7',
 '普米': '12,6',
 '怒': '9',
 '纳西': '7,6',
 '仫佬': '5,8',
 '苗': '8',
 '蒙古': '13,5',
 '门巴': '3,4',
 '毛南': '4,9',
 '满': '13',
 '珞巴': '10,4',
 '僳僳': '14,14',
 '黎': '15',
 '拉祜': '8,9',
 '柯尔克孜': '9,5,7,7',
 '景颇': '12,11',
 '京': '8',
 '基诺': '11,10',
 '回': '6',
 '赫哲': '14,10',
 '哈萨克': '9,11,7',
 '哈尼': '9,5',
 '仡佬': '5,8',
 '高山': '10,3',
 '鄂温克': '11,12,7',
 '俄罗斯': '9,8,12',
 '鄂伦春': '11,6,9',
 '独龙': '9,5',
 '东乡': '5,3',
 '侗': '8',
 '德昂': '15,8',
 '傣': '12',
 '达斡尔': '6,14,5',
 '朝鲜': '12,14',
 '布依': '5,8',
 '保安': '9,6',
 '布朗': '5,10',
 '白': '5',
 '阿昌': '7,8',
 '汉': '5'}
import check.check_number as number 
import check.language_deal as address
import re
import difflib
#import numpy as np
def ischinese(char):
    ch = ''
    for c in char:
        if u'\u4e00' <= c <= u'\u9fff':
            ch = ch + c
    return ch
    
def string_similar(s1, s2):
    return difflib.SequenceMatcher(None, s1, s2).quick_ratio()
def get_stroke(c):
    # 如果返回 0, 则也是在unicode中不存在kTotalStrokes字段
    strokes_path = 'addrs_libs/strokes.txt'
    strokes = []
    with open(strokes_path, 'r') as fr:
        for line in fr:
            strokes.append(int(line.strip()))

    unicode_ = ord(c)

    if 13312 <= unicode_ <= 64045:
        return strokes[unicode_-13312]
    elif 131072 <= unicode_ <= 194998:
        return strokes[unicode_-80338]
    else:
        print("c should be a CJK char, or not have stroke in unihan data.")
        # can also return 0

def check_race(race):
    race = '薇'
    line = ''
    for l in race:
        line = '' + str(get_stroke(l))  + ','
    line = line[:-1]
    values  = list(dict_.values())
    distance = []
    for v in values:
        distance.append(string_similar(line, v))
    m = max(zip(distance,dict_.keys()))
    return m[1]
#    values[distance.index(max(distance))]
    
def check(dice):
#    result = {'address':'','sex':'','birth':'','number':'','name':'','jiguan':'南冲市公安局','riqi':'2018.03.20-2028.03.20'}
    sex = {'0':'女','1':'男'}
    dice = dice
#    dice = {}
#    print(dice['number'],999+9)
#    dice['sex'] = '女朝.'
    if (dice['number'])!= '':
#        try :
        dice['sex'] = ischinese(dice['sex'])
        if dice['number'][-1] == 'x':
            dice['number'] = dice['number'][:-1] + 'X'
        try:
            if (number.number(dice['number'])):
                dice['性别'] =  sex[str(int(dice['number'][16]) % 2)]#+'民族' +dice['sex'][1]
                if len(dice['sex'])  >= 2:
#                     if dice['sex'][1:] in dict_.keys():
                     for race_single in dict_.keys():
                         if dice['sex'][1:] in race_single:
                             dice['民族'] = race_single
                     if not ( dice['sex'][1:]  in   dict_.keys()) :
                         dice['民族'] =  check_race(dice['sex'][1:])
                else:
                     dice['民族'] = '汉'
                    
                dice['birth'] = dice['number'][6:10] + '年' + dice['number'][10:12] + '月' + dice['number'][12:14] + '日' 
#                dice['address'] = address.address(dice['address'])
#            dic['sex'] = ''dic['sex'] + dic['sex']
#        except:
#            dice['address'] = address.address(dice['address'])
        except: 
            if len(dice['sex'])  >= 2:
#                     if dice['sex'][1:] in dict_.keys():
                     for race_single in dict_.keys():
                         if dice['sex'][1:] in race_single:
                             dice['民族'] = race_single
                     if not  dice['sex'][1:]  in   dict_.keys() :
                         dice['民族'] =  check_race(dice['sex'][1:])
            else:
                     dice['民族'] = '汉'
            dice['性别'] = dice['sex'][0]
        if dice['address'][-1] in ['_','慕']:
            dice['address'] =  dice['address'][:-1]
        if dice['address'][-2] in ['号','组']:
            dice['address'] =  dice['address'][:-1]
        dice['address'] = address.address(dice['address'])
        dice['出生日期'] = dice['birth'] 
        dice['地址'] = address.address(dice['address'])
        dice['身份证号码'] = dice['number']
        dice['姓名'] = dice['name']
        del dice['number']
        del dice['address']
        del dice['name']
        del dice['birth']
        del dice['sex']
        del dice['jiguan']
        del dice['riqi']
        return dice
    else:
        if '公安' in dice['jiguan']:
            dice['jiguan'] = dice['jiguan'].replace(re.search('公安.',dice['jiguan']).group(),'')
        if '分局' in dice['jiguan'] :
            dice['jiguan'] = dice['jiguan'].replace(re.search('分.',dice['jiguan']).group(),'')
        dice['jiguan'] = address.address(dice['jiguan'])
#        dic['jiguan'].split('市')
        a = dice['jiguan'].split('市')
        for i in a:
            if i == '':
                a.remove(i)
        if len(a) > 1:
            dice['jiguan'] = dice['jiguan'].split('市')[0] + '市公安局' + dice['jiguan'].split('市')[1] + '分局'
        else:
            dice['jiguan'] =  dice['jiguan'] = dice['jiguan'] + '公安局'
#        print(dic['jiguan'])
        dice['机关'] = dice['jiguan']
        dice['日期'] = dice['riqi']
        del dice['sex']
        del dice['jiguan']
        del dice['riqi']
        del dice['address']
        del dice['name']
        del dice['number']
        del dice['birth']
#            dice.clear()
           
        return dice

