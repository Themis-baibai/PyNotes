#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/8 15:00
# @Author  : name
# @File    : file_opening.py

'''
with open('programming.txt','w') as file_obj: #新建文件并写入
    file_obj.write("I love programming !\n"+"What about you ?\n")

with open('programming.txt','a') as add_obj:  #为新建的文件添加内容
    add_obj.write("Me too!\n"
                  "I also love creating apps that can run in a browser.^_^")
'''

while True:
    name = input("Please input your name:")
    if name=='end':
        break
    reason = input("Why do love programming?")
    print("Thank you! ^-^")
    with open('guest.txt', 'a') as file_obj:
        file_obj.write(name + '\n')
    with open('reasons.txt','a') as reason_file:
        reason_file.write(name+"s\' reason for loving programming is that: "+reason+'\n')

