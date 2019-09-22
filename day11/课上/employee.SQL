create table employee(
id int not null unique auto_increment,
emp_name varchar(20) not null,
sex enum('male','female') not null default 'male', #大部分是男的
age int(3) unsigned not null default 28,
hire_date date not null,
post varchar(50),
post_comment varchar(100),
salary double(15,2),
office int, #一个部门一个屋子
depart_id int
)ENGINE = InnoDB AUTO_INCREMENT = 5 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;


insert into employee(emp_name,sex,age,hire_date,post,salary,office,depart_id) values
('egon','male',18,'20170301','老男孩驻沙河办事处外交大使',7300.33,401,1), #以下是教学部
('alex','male',78,'20150302','teacher',1000000.31,401,1),
('wupeiqi','male',81,'20130305','teacher',8300,401,1),
('yuanhao','male',73,'20140701','teacher',3500,401,1),
('liwenzhou','male',28,'20121101','teacher',2100,401,1),
('jingliyang','female',18,'20110211','teacher',9000,401,1),
('jinxin','male',18,'19000301','teacher',30000,401,1),
('成龙','male',48,'20101111','teacher',10000,401,1),

('歪歪','female',48,'20150311','sale',3000.13,402,2),#以下是销售部门
('丫丫','female',38,'20101101','sale',2000.35,402,2),
('丁丁','female',18,'20110312','sale',1000.37,402,2),
('星星','female',18,'20160513','sale',3000.29,402,2),
('格格','female',28,'20170127','sale',4000.33,402,2),

('张野','male',28,'20160311','operation',10000.13,403,3), #以下是运营部门
('程咬金','male',18,'19970312','operation',20000,403,3),
('程咬银','female',18,'20130311','operation',19000,403,3),
('程咬铜','male',18,'20150411','operation',18000,403,3),
('程咬铁','female',18,'20140512','operation',17000,403,3)
;

 insert into employee(emp_name,sex,age,hire_date,post,salary,office,depart_id) values
 ('茨木童子','male',800,20190101, 'boss',5000.11,505,4),
 ('大天狗', 'female',1000,20180101,'妖怪',100000,505,4)；
 
 # 拼接
 
# 1.concat 字符拼接
select concat('名字:',emp_name),concat('薪资:',salary) from employee;

# 2. 去重查询
select DISTINCT (post) from employee;

# 3. 四则运算
select emp_name, salary * 12 annual_year from employee;

# where 语句

#1. 查看岗位是teacher的员工姓名、年龄
select emp_name, age from employee where post='teacher';

#2. 查看岗位是teacher且年龄大于30岁的员工姓名、年龄
select emp_name,age from employee where post='teacher' and age>30;

#3. 查看岗位是teacher且薪资在9000-10000范围内的员工姓名、年龄、薪资
select emp_name,age,salary from employee where post='teacher' and salary between 9000 and 10000; 

#4. 查看岗位描述不为NULL的员工信息
select * from employee where post_comment is not null;
#5. 查看岗位是teacher且薪资是10000或9000或30000的员工姓名、年龄、薪资
select emp_name,age,salary from employee where post='teacher' and salary in(9000,30000,10000);

#6. 查看岗位是teacher且薪资不是10000或9000或30000的员工姓名、年龄、薪资
select emp_name,age,salary from employee where post='teacher' and salary not in(9000,30000,10000);

#7. 查看岗位是teacher且名字是jin开头的员工姓名、年薪
select emp_name name,salary*12 salary from employee where post='teacher' and emp_name like 'jin%';


# 分组查询 
#1. 查询岗位名以及岗位包含的所有员工名字
select post,group_concat(emp_name) from employee group by post;

#2. 查询岗位名以及各岗位内包含的员工个数
select post, count(id) from employee group by post;

#3. 查询公司内男员工和女员工的个数
select sex,count(id) from employee group by sex;

#4. 查询岗位名以及各岗位的平均薪资
select post,avg(salary) from employee group by post;

#5. 查询岗位名以及各岗位的最高薪资
select post,max(salary) from employee group by post;

#6. 查询岗位名以及各岗位的最低薪资
select post,min(salary) from employee group by post;

#7. 查询男员工与男员工的平均薪资，女员工与女员工的平均薪资
select sex,avg(salary) from employee group by sex;

# having 过滤
#1. 查询各岗位内包含的员工个数小于2的岗位名、岗位内包含员工名字、个数
select count(id), post ,group_concat(emp_name)
from employee 
group by post
having count(id) <2 ;

#3. 查询各岗位平均薪资大于10000的岗位名、平均工资
select avg(salary),post from employee group by post having avg(salary) >10000;

#4. 查询各岗位平均薪资大于10000且小于20000的岗位名、平均工资
select avg(salary),post from employee group by post having avg(salary) >10000 and avg(salary)<20000;
