#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author ：王刘俊

import pymysql

# 数据库连接信息
conn = pymysql.connect(
    host='127.0.0.1', user='root', password="123456",
    database='book_db', port=3306
)
cursor = conn.cursor()

try:
    with open('book', encoding='utf-8') as f:
        for line in f:
            book_tu = tuple(line.strip().split('|'))
            sql = "insert into book values %s" % str(book_tu)
            cursor.execute(sql)

    conn.commit()  # 提交事务
except:
    conn.rollback()
conn.close()
