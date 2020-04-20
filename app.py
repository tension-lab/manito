# -*- coding: utf-8 -*-
import os
import random
import time

from flask import Flask, request, make_response, render_template

app = Flask(__name__)

members = ['@3unbeom',
           '@jade_y1004',
           '@v01dwalker',
           '@thisisaarroniboyy',
           '@run.dong8',
           '@_jiyoung_e',
           '@ju3unoia',
           '@rightofsilence',
           '@__hyun91',
           '@vely_yoni_official']

user_list = list()
target_list = list(members)
server_reset_time = str(time.time())


@app.route("/", methods=['POST', 'GET'])
def index():
    client_reset_time = request.cookies.get('reset_time')
    if server_reset_time == client_reset_time:
        return request.cookies.get('name')

    if len(target_list) == 0:
        return '다 뽑힘 힝구ㅜㅜ'

    if request.method == 'POST':
        my_name = request.form['myName']
        choice_list = list(target_list)
        if my_name in choice_list:
            choice_list.remove(my_name)

        if len(choice_list) == 0:
            return '다 뽑힘 힝구ㅜㅜ'

        name = random.choice(choice_list)
        target_list.remove(name)
        user_list.append(my_name)

        res = make_response(name)
        res.set_cookie('name', name)
        res.set_cookie('reset_time', server_reset_time)
        return res

    return render_template('index.html', users=user_list, members=members)


@app.route("/reset")
def reset():
    global user_list, target_list, server_reset_time
    user_list = list()
    target_list = list(members)
    server_reset_time = str(time.time())
    return f'리셋완료 {target_list}'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ['PORT'])
