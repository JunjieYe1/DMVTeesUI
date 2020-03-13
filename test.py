#!/usr/bin/python3
# coding=utf-8# coding=utf-8# coding=utf-8# coding=utf-8# coding=utf-8# coding=utf-8# coding=utf-8# coding=utf-8
#import sys
import pymysql
import traceback  
import datetime ,time



def connectdb():
    print('Creating Connection...')
    db = pymysql.connect(host="test.csxyg8gxd1zd.us-east-2.rds.amazonaws.com",user="admin",passwd="LYC438sby",db="IT493",charset="utf8")
    print('Connect successfully ...')
    return db ;


def query(db,sql="select * from Orders"):
    cursor=db.cursor()

    try:
        cursor.execute(sql)
        results=cursor.fetchall()
        for line in results:
            print (str(line))
    except:
        traceback.print_exc()  
        print ("ERROR :unable fetch data")

def insertQ(db,sql = """INSERT INTO Orders(OrderID) VALUES (10)"""):
    cursor=db.cursor()

    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        print("Insert successfully")
    except:
        # 如果发生错误则回滚
        traceback.print_exc()  
        db.rollback()
        print("Insert faliure")



def OrderTable(db,lim):
    print("-----------------------------Order Table----------------------------------")

    if lim == 'all':
        sql="select * from Orders"
    elif lim == "Pending" or lim == "pending":
        sql="select * from Orders where OrderStatus = 'Pending'"

    else:
        print("wrong input")
        pass
    query(db,sql)
    


    

def main():
    db=connectdb()
    #query(db,sql="Describe Orders")

    OrderTable(db,lim="Pending")

    #insertQ(db)
    
    db.close()

if __name__=='__main__':
    main()
