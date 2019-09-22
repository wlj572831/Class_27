#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author ：wangliujun

# 启动数据库
    # server端
    # net start mysql 启动服务端
    # net stop mysql 关闭服务端


# mysql
    # mysql -uroot -p123456 -h192.168.0.1
    # select user() 当前登录的用户
    # exit 退出客户端
    # set password = password('新密码') 修改密码
    # show variables like '%character%';
# 名词
    # DBMS 数据库管理系统
    # DBA 数据库管理员
    # DB  table（表） data(数据)

# mysql oracle sqlserver db2 postgresql sqllite 关系型数据库
# mongodb redis memcache 非关系型数据库


# 数据库的操作:
    # 创建库 create database 数据库名
        # 相当于创建了一个文件夹
    # 查看库 show databases
    # 使用库 use 数据库名 切换到指定库下
    # 删除库: drop databse 数据库名;
# 数据库的存储引擎
    # InnoDB
# 数据库表操作
    # 创建库
        # creat tabl 表名(字段1 类型(长度) 约束, 字段2 类型(长度) 约束)
        # create table score(id int(8), name char(20), num int(10) charset= utf-8)

    # 修改表
    # 查看表
        # desc score    更直观
        # show create table score 更全面(包括编码信息)
        # show engines; mysql 5.6以上存储引擎  默认(inndb)
            # 支持事物
            # 行级锁，表锁 数据修改频繁
            # 外键约束:
    # 删除表
        # drop table 表名
# 数据的操作:
    # 增
        # insert into 表名(字段名) values (值)
        # insert into score(id,name,num) values(1,'alex',0);
        # insert into score values (1,'alex',0),(2,'wusir',0);  #一次插入多行
    # 删
        # delete from 表名 where 条件
    # 改
        # update 表名 set 字段名 = '新的值' where 条件
    # 查:
        # select * from 表 查询所有数据

# 类型和约束
# 类型
    # 数字: 薪资 年龄
        # 整型: # 长度的约束都是无效的，它能够表示的的大小只和它存储的字节数相关
            # 年龄: tinyint 1bytes
            # smallint 2bytes
            # mediumint 3bytes
            # int  4bytes 2**32
        # 浮点型
            # float(m, n) 单精度
                # m 表示一共有多少位
                # n 小数部位占其中多少位
            # double(m, n) 双精度 能够表示的小数点之后的位数更精准
    # 字符串: 用户名和密码\手机号\身份证号
        # char :    用户名\密码\手机号
            # char(20) 定长存储  浪费空间
            # 'alex           ' 操作节省时间
        # varchar : 评论\动态\
            # varchar(255) 变长存储
                # 存储 'alex4'    # 节省空间
                # 操作更加浪费时间
    # 时间:  注册时间\登录时间\修改时间\出生日期
        # datetime  年月日时分秒
        # date  年月日
        # time  时分秒
        # timestamp 时间戳
        # year 年
        # create table t6(dt datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE 记录时间为更新时间
    # 单选和多选:
        # enum单选和 set多选，去重
        # create table t7(gender enum('男','女'),hobby set('抽烟','喝酒','烫头','洗脚'));