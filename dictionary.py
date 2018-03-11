#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 04/03/2018 23:51
# @Author  : DaBai
# @Site    : 
# @File    : dictionary.py
# @Software: PyCharm

favorite_languages = {
    'jen':'python',
    'sear':'c',
    'edward':'ruby'
}

friends = ['phil','sear']

for name in favorite_languages:

    if name in friends:
        print('Hi \n'+name.title()+'! I see your favorate languages is '+favorite_languages[name].title())
