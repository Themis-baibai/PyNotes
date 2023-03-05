#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/9 11:34
# @Author  : name
# @File    : city_function.py


"""def get_formatted_name(city,country):
    '''获得一定格式的城市国家输出'''
    result=city.title()+','+country.title()
    return result"""

def get_formatted_name(city,country,population=''):
    '''获得一定格式的城市国家输出'''
    if population:
        result = city.title() + ',' + country.title() + '-population ' + population
    else:
        result = city.title() + ',' + country.title()
    return result

