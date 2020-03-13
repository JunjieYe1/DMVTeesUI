#!/usr/bin/env python
#-*- coding: utf8 -*-

import pymysql
import json

# 定义查询SQL语句
sql = "select * from Orders"

def connectdb():
    print('Creating Connection...')
    db = pymysql.connect(host="test.csxyg8gxd1zd.us-east-2.rds.amazonaws.com",user="admin",passwd="LYC438sby",db="IT493",charset="utf8")
    print('Connect successfully ...')
    return db ;

# Python 连接MySQL
conn=connectdb()
cur=conn.cursor()
cur.execute(sql)                        # 执行SQL查询
data = cur.fetchall()                   # 查询结果给data。如果执行：print data 显示结果：（（第一行内容），（第二行内容），（第三行内容），（第四行内容））
fields = cur.description               # 获取查询结果中列的字段名，如果查询SQL中使用别名，此处显示别名。      
cur.close()
conn.close()

# Main
column_list = []                        # 定义字段名的列表
for i in fields:
    column_list.append(i[0])  # 提取字段名，追加到列表中
#print column_list　　　　　　　   # 列表显示结果：['id', 'NAME', 'LOCAL', 'mobile', 'CreateTime']

with open('Orders.json','w+') as f:# 打开输出结果文件
    for row in data:                                    # 一次循环，row代表一行，row以元组的形式显示。
        result = {}                                     # 定义Python 字典
        result[column_list[0]] = row[0]                 # 将row中的每个元素，追加到字典中。　
        result[column_list[1]] = str(row[1])            # Python字段格式 和json字段格式转换
        result[column_list[2]] = str(row[2])
        result[column_list[3]] = row[3]
        result[column_list[4]] = str(row[4])
        result[column_list[5]] = row[5]
        result[column_list[6]] = row[6]
        result[column_list[7]] = row[7]
        result[column_list[8]] = row[8]
        result[column_list[9]] = row[9]
        print(result)
        jsondata=json.dumps(result,ensure_ascii=False) # Python的dict --转换成----> json的object
        f.write(jsondata + '\n')# 写入文件
f.close()         