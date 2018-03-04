#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 04/03/2018 22:52
# @Author  : DaBai
# @Site    : 
# @File    : Cars.py
# @Software: PyCharm

#最简单的IF语句 1
# cars = ['audi','bwm','toyota']
# for car in cars:
#     if car == 'audi':
#         print(car.upper())
#     else:
#         print(car.title())

# cars  = 'subaru'
# print("Is car =='subaru'? I predict True ")
# print(cars == 'subaru')

num = input('请输入您的年龄：')
if int(num) <= 18:
    print('您的年龄不够，不能参加此活动')
elif int(num) > 18 and int(num) <= 60:
    print('欢迎您的光临')
else:
    print('欢迎您的光临，您属于年老用户，有优惠')