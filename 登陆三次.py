#!/usr/bin/env python
# encoding: utf-8
'''
@author: liuhongnan
@contact: liunanmu@163.com
@Blog address:http://www.cnblogs.com/liuhongnan/
@File    : 登陆三次.py
@Time    : 2019/8/23 3:05 PM
'''
'''
实现用户输入用户名和密码,当用户名为 seven 且 密码为 123 时,显示登陆成功,否则登陆失败,失败时允许重复输入三次
'''
count=0
while count<3:
    username=input('username:')
    password=input('password:')
    if username=='seven' and password=='123':
        print('登陆成功')
        break
    else:
        print('登陆失败 请重新登陆')
        count+=1