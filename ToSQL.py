#!/usr/bin/env python
#-*- coding: utf8 -*-

import pymysql
import json
sqlstatement = ''
datalist = []  # python 列表
with open('Orders.json','r') as f:
    for line in f:      # 读取json文件中的行（也就是json的object）　　　
        datalist.append(json.loads(line)) # 将json的object转成 Python的dict，追加到Python 列表中, 结果都是unicode格式：[{},{},{},{},{}]
for json in datalist:
    keylist = "("
    valuelist = "("
    firstPair = True
    for key, value in json.items():
        if not firstPair:
            keylist += ", "
            valuelist += ", "
        firstPair = False
        keylist += key
        if value is str:
            valuelist += "'" + value + "'"
        else:
            valuelist += str(value)
    keylist += ")"
    valuelist += ")"

    sqlstatement += "INSERT INTO " + "Orders" + " " + keylist + " VALUES " + valuelist + "\n"

print(sqlstatement)