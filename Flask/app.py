#!/usr/bin/env python3
from flask import Flask, url_for, redirect, request, session, make_response, render_template
from datetime import timedelta
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')


@app.route('/')
def index():
    username = request.cookies.get('username')
    return 'Hello {}'.format(username)

@app.route('/user/<username>')
def user_index(username):
    resp = make_response(render_template('user_index.html', username=username))
    resp.set_cookie('username', username)
    # 在函数中指明变量名称 username, 就能获取到通过路由传入的变量值 username
    return resp
'''
@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post {}'.format(post_id)


@app.route('/user/<username>')
def user_index(username):
    print('User-Agent:', request.headers.get('User-Agent'))  # 打印请求头的数据
    print('time:', request.args.get('time')) # 获取请求 URL 中 ? 后面的 time 参数
    print('q:', request.args.get('q')) # 获取请求 URL 中 ? 后面的 q 参数
    print('Q:', request.args.getlist('Q')) # 当参数的值不止一个时使用 geilist 方法
    return 'Hello {}'.format(username)


@app.route('/<username>')
def hello(username):
    if username == 'shixiaolou':   # 如果访问 shixiaolou 则显示页面
        return 'hello {}'.format(username)
    else:
        return redirect(url_for('index')) # 否则重定向到首页


@app.route('/register', methods=['GET', 'POST'])
def register():
    print('method:', request.method)
    print('name:', request.form.get('name'))
    print('password:', request.form.get('password'))
    print('hobbies:', request.form.getlist('hobbies'))
    print('age:', request.form.get('age', default=18))
    return 'registered successfully!'
'''
# 设置session
@app.route('/set_session')
def set_session():
    session.permanent = True   # 设置session的持久化
    app.permanent_session_lifetime = timedelta(minutes=5)  # 设置session的存活时间为5分钟
    session['username'] = 'shixiaolou'
    return '成功设置session'

# 获取 session
@app.route('/get_session')
def get_session():
    value = session.get('username')
    return '获取的session值为{}'.format(value)

# 移除 session
@app.route('/del_session')
def del_session():
    value = session.pop('username')
    return '成功移除session, 其值为{}'.format(value)

if __name__ == '__main__':
    app.run
