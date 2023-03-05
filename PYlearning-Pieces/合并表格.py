#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/11/19 12:19
# @Author  : Anki
# @File    : 合并表格.py


import pandas as pd
import os
import io
import openpyxl
#import xlwt

# 全局变量，文件读取路径
read_path = "C:/Users/10371/Desktop/female各年龄"
# 全局变量，处理结果文件输出路径
output_path = "C:/Users/10371/Desktop/female各年龄"

# 读取文件名称和内容
def deal_files():
    # 获取read_path下的所有文件名称（顺序读取的）
    files = os.listdir(read_path)
    df = pd.read_excel(r"C:/Users/10371/Desktop/female各年龄/0014.xls",sheet_name='Data',header=3) #都合并到第一张表
    for file_name in files:
        if file_name != "0014.xls":
            # 读取单个文件内容
            dfdata = pd.read_excel(read_path+"/"+file_name,sheet_name='Data',header=3)
            df = pd.concat([df,dfdata],axis=0)

        # 输出结果到指定路径下
    df.to_csv(output_path + "/" + "female各年龄段合并.csv" , index=False)
    print("文件处理完毕")


# 主函数
if __name__=="__main__":
    # 开始处理文件，并输出处理文件结果
    deal_files()


