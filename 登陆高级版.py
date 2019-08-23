#!/usr/bin/env python
# encoding: utf-8
'''
@author: liuhongnan
@contact: liunanmu@163.com
@Blog address:http://www.cnblogs.com/liuhongnan/
@File    : 登陆高级版.py
@Time    : 2019/8/23 3:12 PM
'''
'''
实现用户输入用户名和密码,当用户名为 seven 或 alex 且 密码为 123 时,显示登陆成功,否则登陆失败,失败时允许重复输入三次
'''
userdb=['seven','alex']
count=0
while count<3:
    username=input('username:')
    password=input('password:')
    if username in userdb and password=='123':
        print('登陆成功')
        break
    else:
        print('登陆失败 请重新输入')
        count+=1
