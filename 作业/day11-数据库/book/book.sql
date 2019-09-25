-- ----------------------------
-- 创建book_db库
-- ----------------------------
DROP DATABASE IF EXISTS `book_db`;
CREATE DATABASE IF NOT EXISTS book_db default charset utf8 COLLATE utf8_general_ci;

-- 进入book_db 
USE book_db;
SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;


-- ----------------------------
-- 0.创建book表 插入数据
-- ----------------------------
DROP TABLE IF EXISTS `book`;
CREATE TABLE `book`(
`name` char(20) not null,	# 书名
`author` char(20) not null,	# 作者
`Press` char(20) not null,	# 出版社
`price` float(5,1) not null, # 价格
`pub_date` date not null	#出版日期
);

insert into `book` values
('倚天屠龙记','egon','北京工业地雷出版社',70,'2019-7-1'),
('九阳神功','alex','人民音乐不好听出版社',5,'2018-7-4'),
('九阴真经','yuan',	'北京工业地雷出版社',62,'2017-7-12'),
('九阴白骨爪','jinxin','人民音乐不好听出版社',40,'2019-8-7'),
('独孤九剑','alex','北京工业地雷出版社',12,'2017-9-1'),
('降龙十巴掌','egon','知识产权没有用出版社',20,'2019-7-5'),
('葵花宝典','yuan',	'知识产权没有用出版社',33,'2019-8-2')
;
commit;

--1.查询egon写的所有书和价格
SELECT name 书名, price 价格 from book where author = 'egon';

--2.找出最贵的图书的价格
select max(price) from book;

--3.求所有图书的均价
select avg(price) 平均价格 from book;

--4.将所有图书按照出版日期排序
select * from book order by pub_date;

--5.查询alex写的所有书的平均价格
select author 作者, avg(price) 平均价格 from book where author='alex';

--6.查询人民音乐不好听出版社出版的所有图书
select * from book where press='人民音乐不好听出版社';

--7.查询人民音乐出版社出版的alex写的所有图书和价格
SELECT name 书名, price 价格 from book 
where author = 'alex' and press='人民音乐不好听出版社';

--8.找出出版图书均价最高的作者
select author 作者, avg(price) 价格 from book
group by author
order by avg(price) desc limit 1;

--9.找出最新出版的图书的作者和出版社
select name,author,press,pub_date from book 
order by pub_date desc limit 1;

--10.显示各出版社出版的所有图书
SELECT Press,GROUP_CONCAT( NAME ) FROM book GROUP BY press;

--11.查找价格最高的图书，并将它的价格修改为50元
update  book set price=50 order by price desc limit 1;

--12.删除价格最低的那本书对应的数据
delete from book order by price limit 1;

--13.将所有alex写的书作业修改成alexsb
update book set author='alexsb' where author='alex';

--14.select year(publish_date) from book
--自己研究上面sql语句中的year函数的功能，完成需求：
--将所有2017年出版的图书从数据库中删除
delete from book where year(pub_date)= '2017';

-- 15.有文件如下，请根据链接自学pymysql模块，使用python写代码将文件中的数据写入数据库

