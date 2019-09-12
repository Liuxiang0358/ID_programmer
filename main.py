# -*- coding: utf-8 -*-

import alight
import second
import detect_id
import  crnn_dic
from werkzeug.utils import secure_filename
from flask import Flask, render_template, jsonify, request, make_response, send_from_directory, abort
import time
import os
import uuid
import base64
import remove
import check_total
app = Flask(__name__)
UPLOAD_FOLDER = 'upload'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
basedir = os.path.abspath(os.path.dirname(__file__))
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'JPG', 'PNG'])


def allowed_file(filename):
  return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
  
@app.route('/upload')
def upload_test():
  return render_template('up.html')
# 上传文件



@app.route('/up_photo', methods=['POST'], strict_slashes=False)
def api_upload():
  file_dir = os.path.join(basedir, app.config['UPLOAD_FOLDER'])
  if not os.path.exists(file_dir):
    os.makedirs(file_dir)
  f = request.files['photo']
  if f and allowed_file(f.filename):
    fname = secure_filename(f.filename)
    print(fname)
#    ext = fname.rsplit('.', 1)[1]
#    new_filename = str(uuid.uuid1()) + 'back' + '.' + ext
#    remove.remove()
    file_name = os.path.join(file_dir, f.filename)
    f.save(file_name)
    time_Take = time.time()
    align_img = alight.detect_first(file_name)
    print('first',time.time()-time_Take)
    time_Take1 = time.time()
    second.detect_second(file_name,align_img)
    print('second',time.time()-time_Take)
    time_Take = time.time()
    region  =  detect_id.detect_third(file_name)
    print('third',time.time()-time_Take)
    time_Take = time.time()
    res = crnn_dic.Crnn(region)
    print(res)
    print('checkion',time.time()-time_Take)
    res = check_total.check(res)
#    res['time'] = str(time.time()-time_Take1)
#    remove.remove()
    return jsonify(res)
  else:
    return jsonify({"error": 1001, "msg": "上传失败"})
  
#application = create_app()  
  
if __name__ == '__main__':
   app.run( debug=True) 
