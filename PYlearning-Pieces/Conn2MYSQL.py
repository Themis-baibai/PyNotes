#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/2 14:49
# @Author  : name
# @File    : web_spider.py

import requests
from bs4 import BeautifulSoup #网页数据解析和格式化处理工具
import pymysql



def spider_video():
    '''爬取知识区视频内容'''
    rank_url =r'https://www.bilibili.com/v/popular/rank/knowledge' #知识区排行榜网址
    rank_html = requests.get(rank_url)
    rank_html.encoding = 'utf8'
    rank_soup=BeautifulSoup(rank_html.text,'lxml') #创建soup对象
    vid_url=[] # 保存各个视频的url
    vid_oid=[] # 保存各个视频的oid


def spider_comments(vid_oid):



def insert_tables(datalist):
    '''插入数据到表'''
    # 连接数据库
    db = pymysql.connect(host='localhost', user='root', password='520929', database='bilibili')
    # 声明游标
    cur = db.cursor()
    try:
        for data in datalist :
            data = tuple(data)  #列表转元祖 一定要记得
            sql = 'INSERT INTO activities(name,adress) VALUE (%s,%s)' # 表名  字段名 插入的值
            # print(sql)   #打印从元祖中获取到的东西
            value = (data[0],data[1])  #传递元组的值  status 初始化0
            cur.execute(sql,value)  # 将数据进行提交
            db.commit()  # 数据库的提交
        print("数据插入成功!")
    except pymysql.Error as e:
        print("数据插入失败"+str(e))
        db.rollback()   #数据插入失败返回原先状态

    db.close()


