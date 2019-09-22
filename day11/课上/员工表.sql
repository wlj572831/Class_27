#建表
create table department(
id int,
name varchar(20) 
) ENGINE = InnoDB AUTO_INCREMENT = 5 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

create table employee(
id int primary key auto_increment,
name varchar(20),
sex enum('male','female') not null default 'male',
age int,
dep_id int
)ENGINE = InnoDB AUTO_INCREMENT = 5 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

#插入数据
insert into department values
(200,'技术'),
(201,'人力资源'),
(202,'销售'),
(203,'运营');

insert into employee(name,sex,age,dep_id) values
('egon','male',18,200),
('alex','female',48,201),
('wupeiqi','male',38,201),
('yuanhao','female',28,202),
('liwenzhou','male',18,200),
('jingliyang','female',18,204)
;

# 1.找到技术部的所有人
select emp.*  from employee emp 
left join department dep on dep.id = emp.dep_id
where dep.name = '技术'

# 2. 以内连接的方式查询employee和department表
select emp.*,dep.name  from employee emp 
inner join department dep on dep.id = emp.dep_id
where emp.age>25

# 3. 以内连接方式查询 employee 和 department表 并以age 升序显示
select *  from employee emp 
inner join department dep on dep.id = emp.dep_id
order by emp.age