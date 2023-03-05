#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/8 14:32
# @Author  : name
# @File    : file_reading.py

file_obj=open('learning_python.txt','r')
# the first printing
contents=file_obj.read()
print('first\n'+contents)
# the second printing
print('second')
for line in file_obj:
    print(line.strip())
# the third printing
lines = file_obj.readlines()
file_obj.close()

print('third')
for i in lines:
    print(i.strip())
print(type(contents))
print(type(lines))
