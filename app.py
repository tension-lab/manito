# -*- coding: utf-8 -*-
import os
import random
import time

from flask import Flask, request, make_response

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

current_list = list(member)
server_reset_time = str(time.time())


@app.route("/", methods=['POST', 'GET'])
def index():
    client_reset_time = request.cookies.get('reset_time')
    if server_reset_time == client_reset_time:
        return request.cookies.get('name')

    if len(current_list) == 0:
        return '다 뽑힘 힝구ㅜ'

    name = random.choice(current_list)
    current_list.remove(name)

    res = make_response(name)
    res.set_cookie('name', name)
    res.set_cookie('reset_time', server_reset_time)
    return res


@app.route("/reset")
def reset():
    global current_list, server_reset_time
    current_list = list(member)
    server_reset_time = str(time.time())
    return f'리셋완료 {current_list}'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ['PORT'])
