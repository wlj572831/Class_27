--1、查询男生、女生的人数；
select gender , count(sid) from student group by gender;

--2、查询姓“张”的学生名单；
select * from student where sname like '张%';

--3、课程平均分从高到低显示
select sc.course_id,co.cname, sc.num 
from score sc
left join course co on co.cid = sc.course_id
group by sc.course_id order by sc.num desc;

--4、查询有课程成绩小于60分的同学的学号、姓名；
select stu.sid  学号,stu.sname 姓名,min(sc.num) 最小成绩 from student stu
left join score sc on sc.student_id = stu.sid
group by stu.sid  having min(sc.num) < 60;

--5、查询至少有一门课与学号为1的同学所学课程相同的同学的学号和姓名
SELECT a.student_id, stu.sname FROM score as a 
LEFT JOIN student stu ON stu.sid = a.student_id
WHERE a.course_id in (SELECT b.course_id FROM score AS b WHERE b.student_id = 1)
GROUP BY a.student_id;
-- having a.student_id <> 1 --如果要去掉学号1本身

--6、查询出只选修了一门课程的全部学生的学号和姓名；
select student_id,stu.sname from score sc
left join student stu on stu.sid = sc.student_id
group by student_id having count(*) =1;

--7、查询各科成绩最高和最低的分：以如下形式显示：课程ID，最高分，最低分；
select course_id ,max(num) highest, min(num) lowest from score
group by course_id;

--8、查询课程编号“2”的成绩比课程编号“1”课程低的所有同学的学号、姓名；
-- 写法1 
SELECT a.student_id, stu.sname,a.num AS score1, b.num AS score2 
FROM score a
LEFT JOIN score b ON a.student_id = b.student_id
LEFT JOIN student stu ON stu.sid = a.student_id
WHERE a.course_id = 1 AND b.course_id = 2 
GROUP BY a.student_id HAVING score1 > score2;

-- 写法2 
SELECT tmp.student_id, stu.sname,sum(score1) sco1, sum(score2) sco2 
FROM 
(
SELECT student_id,
CASE WHEN course_id = 1 THEN num END score1,
CASE WHEN course_id = 2 THEN num END score2
FROM score
) tmp 
LEFT JOIN student stu ON stu.sid = tmp.student_id
GROUP BY student_id HAVING sco1 > sco2;

--9、查询“生物”课程比“物理”课程成绩高的所有学生的学号；
SELECT tmp.student_id,sum(score1) sco1, sum(score2) sco2 
FROM 
(
SELECT student_id,
CASE WHEN course_id = (SELECT cid FROM course WHERE cname ='生物' ) THEN num END score1,
CASE WHEN course_id = (SELECT cid FROM course WHERE cname ='物理' ) THEN num END score2
FROM score
) tmp 
GROUP BY student_id 
HAVING sco1 > sco2;

--10、查询平均成绩大于60分的同学的学号和平均成绩;
SELECT  student_id,avg(num) avg_sore from score
group by student_id;

--11、查询所有同学的学号、姓名、选课数、总成绩；
select student_id, count(student_id) total_num, sum(num) total_sco  from score 
group by student_id;

--12、查询姓“李”的老师的个数；
select count(tid) from teacher where tname like '李%';

--13、查询没学过“张磊老师”课的同学的学号、姓名；
SELECT sid,sname FROM student
WHERE sid not in (
	SELECT student_id
	FROM course co
	LEFT JOIN score sc ON co.cid = sc.course_id
	LEFT JOIN teacher tea ON tea.tid = co.teacher_id
	WHERE tea.tname = '张磊老师' 
	GROUP BY student_id 
	)


--14、查询学过“1”并且也学过编号“2”课程的同学的学号、姓名；
SELECT sc.student_id,stu.sname  FROM score sc
LEFT JOIN student stu ON stu.sid = sc.student_id
WHERE sc.course_id IN(1,2)
GROUP BY sc.student_id
HAVING COUNT(student_id) = 2

--15、查询学过“李平老师”所教的所有课的同学的学号、姓名；
SELECT student_id, stu.sname 
FROM course co
LEFT JOIN score sc ON co.cid = sc.course_id
LEFT JOIN teacher tea ON tea.tid = co.teacher_id
LEFT JOIN student stu ON stu.sid = student_id 
WHERE tea.tname = '李平老师' 
GROUP BY student_id 
HAVING COUNT( student_id ) = (
	SELECT COUNT( co.cid ) FROM course co
	LEFT JOIN teacher tea ON tea.tid = co.teacher_id 
	WHERE tea.tname = '李平老师' 
	)
