import json
from flask import Flask, Response, render_template, jsonify, url_for
import base64
import glob
import cv2
import socket
import subprocess
from concurrent.futures import ThreadPoolExecutor
import logging
import time

import flask

#  * Serving Flask app 'app.py' (lazy loading)
#  * Environment: development
#  * Debug mode: on
#  * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
#  * Restarting with stat

app= Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ajax', methods=['GET','POST'])
def ajax():
    print('ajax here')
    files = glob.glob("C:\\Users\\user\\Pictures\\test_picture\\*")
    cnt=0
    jsondat={}
    for file in files:
        print(file)
        #ファイルオープン方式（画像が大きいと重い）
        #with open(file, "rb") as image_file:
        #    data = base64.b64encode(image_file.read())

        #opencv方式(リサイズとか画像処理もできる)
        img=cv2.imread(file)
        height, width, channels = img.shape[:3]
        img=cv2.resize(img, [int(width*0.15), int(height*0.15)])
        _, encoded = cv2.imencode(".jpg", img)
        data = base64.b64encode(encoded)
        #jsondat[file]=data.decode('utf-8')#キーがファイル名になる
        d={'filename':file, 'image':data.decode('utf-8')}
        jsondat[cnt]=d
        cnt+=1
        #print(jsondat[file])
        
    
    return jsonify(jsondat)

@app.route('/quit', methods=['GET','POST'])
def quit():
    return 0



if __name__ =='__main__':
    #コマンドラインから実行するときに,以下が行われる
    print('from cmd')
    app.run(host='localhost', debug=True)

    