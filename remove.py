# -*- coding: utf-8 -*-

import os
def del_file(path):
      for i in os.listdir(path):
         path_file = os.path.join(path,i)  ## 取文件绝对路径
         if os.path.isfile(path_file):
           os.remove(path_file)
         else:
             del_file(path_file)
def remove():
     del_file('upload')
     del_file('id_card_align')
     del_file('result')
