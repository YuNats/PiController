import json
from flask import Flask, Response, render_template, jsonify, url_for
import base64

from concurrent.futures import ThreadPoolExecutor
import logging
import time
import RPi.GPIO as GPIO

import flask

#  * Serving Flask app 'app.py' (lazy loading)
#  * Environment: development
#  * Debug mode: on
#  * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
#  * Restarting with stat

app= Flask(__name__)
out_pins=[4,17,27,22,5,6,13,19,26]
@app.route('/')
def index():
    # GPIO番号指定の準備
    GPIO.setmode(GPIO.BCM)

    # LEDピンを出力に設定
    for pin in out_pins:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)

    return render_template('index.html')

@app.route('/ajax/<int:pin>', methods=['GET','POST'])
def ajax(pin):
    target_pin=pin
    if(target_pin in out_pins):
        GPIO.output(pin, GPIO.HIGH)
        return jsonify('0')
    else:
        return jsonify('-1')

        
    


@app.route('/quit', methods=['GET','POST'])
def quit():
    return 0



if __name__ =='__main__':
    #コマンドラインから実行するときに,以下が行われる
    print('from cmd')
    app.run(host='localhost', debug=True)
    GPIO.clear()
    