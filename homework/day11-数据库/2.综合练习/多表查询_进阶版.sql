-- 1、查询没有学全所有课的同学的学号、姓名；
SELECT
	sc.student_id,
	stu.sname 
FROM
	score sc
	LEFT JOIN student stu ON stu.sid = sc.student_id 
GROUP BY
	sc.student_id 
HAVING
	COUNT( student_id ) != ( SELECT count( cid ) FROM course );

-- 2、查询和“002”号的同学学习的课程完全相同的其他同学学号和姓名；
SELECT
	student_id,
	stu.sname 
FROM
	score sc
	LEFT JOIN student stu ON stu.sid = sc.student_id 
GROUP BY
	student_id 
HAVING
	GROUP_CONCAT( sc.course_id ) = ( SELECT GROUP_CONCAT( sc.course_id ) FROM score sc WHERE student_id = '002' ) 
	AND student_id != '002';
	
-- 3、删除学习“叶平”老师课的SC表记录；
DELETE FROM score 
WHERE course_id IN ( 
	    SELECT co.cid FROM course co 
			LEFT JOIN teacher tea ON tea.tid = co.teacher_id 
			WHERE tea.tname = '叶平' 
		);

-- 4、向SC表中插入一些记录，这些记录要求符合以下条件：
	--①没有上过编号“002”课程的同学学号；②-插入“002”号课程的平均成绩； 
	
	SELECT * FROM student WHERE sid not in(	 	-- 1.查询没有上过002课程的同学学号
			SELECT student_id FROM score  
			WHERE course_id = 002
			);
	SELECT AVG(num) FROM score WHERE course_id = '002'; -- 2.查询002 平均成绩
	INSERT INTO score(student_id,course_id,num)	-- 3.插入数据
	VALUES (2,002,65),(13,002,65),(14,002,65);
	
-- 5、按平均成绩从低到高显示所有学生的“语文”、“数学”、“英语”三门的课程成绩，
	--按如下形式显示：学生ID,语文,数学,英语,有效课程数,有效平均分；
SELECT
	sc.student_id,
	SUM( CASE WHEN course_id = ( SELECT cid FROM course WHERE cname = '生物' ) THEN num END ) '生物',
	SUM( CASE WHEN course_id = ( SELECT cid FROM course WHERE cname = '物理' ) THEN num END ) '物理',
	SUM( CASE WHEN course_id = ( SELECT cid FROM course WHERE cname = '体育' ) THEN num END ) '体育',
	count_num,
	avg_num 
FROM	score sc
LEFT JOIN ( SELECT student_id, avg( num ) avg_num, COUNT( num ) count_num FROM score GROUP BY student_id) temp ON sc.student_id = temp.student_id 
GROUP BY	sc.student_id ORDER BY	avg_num;
	
-- 6、查询各科成绩最高和最低的分：以如下形式显示：课程ID，最高分，最低分；
SELECT course_id, max( num ) max_num, min( num ) min_num
FROM score GROUP BY course_id

-- 7、按各科平均成绩从低到高和及格率的百分数从高到低顺序；
SELECT course_id, avg(num) 	-- 按各科平均成绩从低到高
FROM score sc GROUP BY course_id ORDER BY avg(num);

SELECT course_id,	-- 及格率的百分数从高到低顺序
CONCAT(ROUND(COUNT(CASE WHEN num < 60 THEN num END)/COUNT(sid)*100,2),'%') '及格率'
FROM score
GROUP BY course_id  
ORDER BY COUNT(CASE WHEN num < 60 THEN num END)/COUNT(num) DESC ;

-- 8、查询各科成绩前三名的记录:(不考虑成绩并列情况) 
SELECT course_id,
	(SELECT num FROM score sc WHERE sc.course_id = A.course_id ORDER BY sc.course_id, sc.num DESC LIMIT 1 ) '第一名',
	(SELECT num FROM score sc WHERE sc.course_id = A.course_id ORDER BY sc.course_id, sc.num DESC LIMIT 1,1 ) '第二名',
	( SELECT num FROM score sc WHERE sc.course_id = A.course_id ORDER BY sc.course_id, sc.num DESC LIMIT 2,1 ) '第三名'
FROM
	score A
GROUP BY  course_id;

-- 9、查询每门课程被选修的学生数；
SELECT course_id,count(DISTINCT student_id) count_num
FROM score
GROUP BY course_id;

-- 10、查询同名同姓学生名单，并统计同名人数；
SELECT sname, count(sid) 
FROM student
GROUP BY sname;

-- 11、查询每门课程的平均成绩，结果按平均成绩升序排列，平均成绩相同时，按课程号降序排列；
SELECT  course_id, avg(num) avg_num from score 
group by course_id  order by avg_num ASC,course_id DESC;

-- 12、查询平均成绩大于85的所有学生的学号、姓名和平均成绩；
SELECT student_id,sname,AVG(num) avg_num
from score
LEFT JOIN student stu on stu.sid=student_id
GROUP BY student_id 
HAVING avg_num > 85;

-- 13、查询课程名称为“数学”，且分数低于60的学生姓名和分数；
SELECT stu.sname, sc.num FROM score sc 
LEFT JOIN student stu ON stu.sid = sc.student_id
LEFT JOIN course co ON co.cid = sc.course_id
WHERE co.cname = '物理' AND sc.num <60;

-- 14、查询课程编号为003且课程成绩在80分以上的学生的学号和姓名； 
SELECT stu.sname, sc.num FROM score sc 
LEFT JOIN student stu ON stu.sid = sc.student_id
WHERE course_id='003' AND sc.num > 80;

-- 15、求选了课程的学生人数
SELECT
	SUM( sid IN ( SELECT student_id FROM score sc GROUP BY sc.student_id ) ) 
FROM
	student;

-- 16、查询选修“杨艳”老师所授课程的学生中，成绩最高的学生姓名及其成绩；
SELECT student.sid ,student.sname ,num  FROM score 
LEFT JOIN course ON score.course_id=course.cid
LEFT JOIN student ON score.student_id=student.sid
LEFT JOIN teacher ON course.teacher_id=teacher.tid
WHERE teacher.tname = "李平老师" ORDER BY num DESC LIMIT 1;

-- 17、查询各个课程及相应的选修人数；
SELECT course_id, co.cname, COUNT( student_id ) 
FROM score sc
LEFT JOIN course co ON co.cid = sc.course_id 
GROUP BY course_id;

-- 18、查询不同课程但成绩相同的学生的学号、课程号、学生成绩；
SELECT A.student_id,A.course_id,B.num,B.student_id,B.course_id,B.num
FROM score A,score B
WHERE A.course_id <> B.course_id AND A.num = B.num 
ORDER BY A.student_id;

-- 19、查询每门课程成绩最好的前两名；
SELECT  co.cname,
(SELECT sc.num FROM score sc WHERE sc.course_id = co.cid ORDER BY sc.num DESC LIMIT 1) '第一名',
(SELECT sc.num FROM score sc WHERE sc.course_id = co.cid ORDER BY sc.num DESC LIMIT 1,1) '第二名'
FROM  course co ;

-- 20、检索至少选修两门课程的学生学号；
SELECT student_id, count(sid) cou_cour FROM score
group by student_id
having cou_cour >= 2;

-- 21、查询全部学生都选修的课程的课程号和课程名；
SELECT course_id, co.cname 
FROM score
LEFT JOIN course co ON co.cid = score.course_id 
GROUP BY course_id 
HAVING COUNT( student_id ) = ( SELECT COUNT( sid ) FROM student );


-- 22、查询没学过“叶平”老师讲授的任一门课程的学生姓名；
SELECT sid, sname 
FROM student 
WHERE sid NOT IN
	(SELECT student_id FROM score sc 
	INNER JOIN course co ON co.cid = sc.course_id
	INNER JOIN teacher tea ON tea.tid = co.teacher_id
	WHERE tea.tname = '李平老师' 
	GROUP BY student_id 
	);

-- 23、查询两门以上不及格课程的同学的学号及其平均成绩；
SELECT student_id,COUNT(num) no_pass,
	(SELECT AVG(A.num) FROM score A WHERE A.student_id = sc.student_id  
	 GROUP BY A.student_id ) '平均分'
FROM score sc
WHERE num <60
GROUP BY student_id HAVING no_pass > 1 ;

-- 24、检索“004”课程分数小于60，按分数降序排列的同学学号；
SELECT stu.sid, sname, num FROM score sc
LEFT JOIN student stu ON stu.sid = sc.student_id
WHERE course_id = '004' AND num < 60
ORDER BY num DESC;

-- 25、删除“002”同学的“001”课程的成绩；
SELECT * FROM score
-- DELETE FROM score
WHERE student_id = '002' AND course_id = '001';

