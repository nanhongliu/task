#!/usr/bin/env python
# encoding: utf-8
'''
@author: liuhongnan
@contact: liunanmu@163.com
@Blog address:http://www.cnblogs.com/liuhongnan/
@File    : 计算进阶版.py
@Time    : 2019/8/23 3:29 PM
'''
'''
使用 while 循环实现输出 1,2,3,4,5, 7,8,9, 11,12
'''
count=0
while count<=12:
    count+=1
    if count==6 or count==10:
        continue
    else:
        print(count)


'''
使用 while 循环实现输出 1-100 内的所有奇数
'''
count=0
while count<100:
    count+=1
    if count%2==0:
        continue
    else:
        print(count)

'''
使用 while 循环实现输出 1-100 内的所有偶数
'''
count=0
while count<100:
    count+=1
    if count%2==0:
        print(count)