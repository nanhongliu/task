#!/usr/bin/env python
# encoding: utf-8
'''
@author: liuhongnan
@contact: liunanmu@163.com
@Blog address:http://www.cnblogs.com/liuhongnan/
@File    : 登陆.py
@Time    : 2019/8/23 2:58 PM
'''
'''
实现用户输入用户名和密码,当用户名为 seven 且 密码为 123 时,显示登陆成功,否则登陆失败!
'''
username=input('username:')
password=input('password:')
if username=='seven' and password=='123':
    print('登陆成功')
else:
    print('登陆失败')