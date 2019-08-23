#!/usr/bin/env python
# encoding: utf-8
'''
@author: liuhongnan
@contact: liunanmu@163.com
@Blog address:http://www.cnblogs.com/liuhongnan/
@File    : 计算.py
@Time    : 2019/8/23 3:18 PM
'''
'''
a. 使用while循环实现输出2-3+4-5+6...+100 的和
'''
seq=0
for i in range(2,101):
    if i%2==0:
        seq=seq+i
    else:
        seq=seq-i
print(seq)