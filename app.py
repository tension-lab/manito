# -*- coding: utf-8 -*-
import os
import random

from flask import Flask, request, render_template

app = Flask(__name__)

member = ['@3unbeom',
          '@jade_y1004',
          '@v01dwalker',
          '@thisisaarroniboyy',
          '@run.dong8',
          '@_jiyoung_e',
          '@ju3unoia',
          '@rightofsilence',
          '@__hyun91',
          '@vely_yoni_official']

current = member


@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        if len(current) == 0:
            return '다 뽑힘 힝구ㅜ'
        name = random.choice(current)
        current.remove(name)
        return name
    else:
        return render_template('index.html')


@app.route("/reset")
def reset():
    global current
    current = member
    return f'리셋완료 {current}'


if __name__ == "__main__":
    # app.run(host='0.0.0.0', port=os.environ['PORT'])
    app.run(host='0.0.0.0', port='8080')
