#!/usr/bin/env python
# encoding: utf-8
'''
@author: liuhongnan
@contact: liunanmu@163.com
@Blog address:http://www.cnblogs.com/liuhongnan/
@File    : 登陆最高级.py
@Time    : 2019/8/23 3:43 PM
'''
'''
可以支持多个用户登录
用户3次认证失败后，退出程序，再次启动程序尝试登录时，还是锁定状态
'''
userandpassword={'user1':'123','user2':'456','user3':'789'}
count=0
while count<3:
    username=input('username:')
    with open('baduser','r') as f:
        if username in f.readline():
            print('被锁定的用户')
            break
    password=input('password:')
    if username in userandpassword and password==userandpassword[username]:
        print('登陆成功')
        break
    else:
        print('登陆是失败 请重试')
        if count==2 and username in userandpassword:
            with open('baduser','w') as f:
                f.seek(2)
                f.write(username)
        count+=1

