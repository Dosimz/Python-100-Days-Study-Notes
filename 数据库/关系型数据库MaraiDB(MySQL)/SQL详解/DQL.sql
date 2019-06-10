-- 查询所有学生信息
select * from tb_student;

-- 查询所有课程名称及学分(投影和别名)
select couname, coucredit from tb_course;
select couname as 课程名称, coucredit as 学分 from tb_course;

-- 查询所有学生的姓名和性别(条件运算)
select stuname as 姓名, case stusex when 1 then '男' else '女' end as 性别 from tb_student;
select stuname as 姓名, if(stusex, '男', '女') as 性别 from tb_student;

-- 查询所有女学生的姓名和出生日期(筛选)
select stuname, stubirth from tb_student where stusex=0;

-- 查询所有80后学生的姓名、性别和出生日期(筛选)
select stuname, stusex, stubirth from tb_student where stubirth>='1980-1-1' and stubirth<='1989-12-31';
select stuname, stusex, stubirth from tb_student where stubirth between '1980-1-1' and '1989-12-31';

-- 查询姓"杨"的学生姓名和性别(模糊)
select stuname, stusex from tb_student where stuname like '杨%';

-- 查询姓"杨"名字两个字的学生姓名和性别(模糊)
select stuname, stusex from tb_student where stuname like '杨_';

-- 查询姓"杨"名字三个字的学生姓名和性别(模糊)
select stuname, stusex from tb_student where stuname like '杨__';

-- 查询名字中有"不"字或"嫣"字的学生的姓名(模糊)
select stuname, stusex from tb_student where stuname like '%不%' or stuname like '%嫣%';

-- 查询没有录入家庭住址的学生姓名(空值)
select stuname from tb_student where stuaddr is null;

-- 查询录入了家庭住址的学生姓名(空值)
select stuname from tb_student where stuaddr is not null;

-- 查询学生选课的所有日期(去重)
select distinct scdate from tb_score;

-- 查询学生的家庭住址(去重)
select distinct stuaddr from tb_student where stuaddr is not null;

-- 查询男学生的姓名和生日按年龄从大到小排列(排序)
-- asc (ascending) - 升序（从小到大）/ desc (descending) - 降序（从大到小）
select stuname as 姓名, year(now())-year(stubirth) as 年龄 from tb_student where stusex=1 order by 年龄 desc;

-- 聚合函数：max / min / count / sum / avg
-- 查询年龄最大的学生的出生日期(聚合函数)
select min(stubirth) from tb_student;

-- 查询年龄最小的学生的出生日期(聚合函数)
select max(stubirth) from tb_student;

-- 查询男女学生的人数(分组和聚合函数)
select stusex, count(*) from tb_student group by stusex;

-- 查询课程编号为1111的课程的平均成绩(筛选和聚合函数)
select avg(scmark) from tb_score where couid=1111;

-- 查询学号为1001的学生所有课程的平均分(筛选和聚合函数)
select avg(scmark) from tb_score where stuid=1001;

-- 查询每个学生的学号和平均成绩(分组和聚合函数)
select stuid as 学号, avg(scmark) as 平均分 from tb_score group by stuid;

-- 查询平均成绩大于等于90分的学生的学号和平均成绩
-- 分组以前的筛选使用where子句 / 分组以后的筛选使用having子句
select stuid as 学号, avg(scmark) as 平均分 from tb_score group by stuid having 平均分>=90;

-- 查询年龄最大的学生的姓名(子查询/嵌套的查询)
select stuname from tb_student where stubirth=(
	select min(stubirth) from tb_student
);

-- 查询年龄最大的学生姓名和年龄(子查询+运算)
select stuname as 姓名, year(now())-year(stubirth) as 年龄 from tb_student where stubirth=(
	select min(stubirth) from tb_student
);

-- 查询选了两门以上的课程的学生姓名(子查询/分组条件/集合运算)
select stuname from tb_student where stuid=(
	select stuid from tb_score group by stuid having count(stuid)>2
)

-- 查询学生姓名、课程名称以及成绩(连接查询)
select stuname, couname, scmark from tb_student t1, tb_course t2, tb_score t3 where t1.stuid=t3.stuid and t2.couid=t3.couid and scmark is not null;

-- 查询学生姓名、课程名称以及成绩按成绩从高到低查询第11-15条记录(内连接+分页)
select stuname, couname, scmark from tb_student t1 inner join tb_score t3 on t1.stuid=t3.stuid inner join tb_course t2 on t2.couid=t3.couid where scmark is not null order by scmark desc limit 5 offset 10;

select stuname, couname, scmark from tb_student t1 inner join tb_score t3 on t1.stuid=t3.stuid inner join tb_course t2 on t2.couid=t3.couid where scmark is not null order by scmark desc limit 10, 5;

-- 查询选课学生的姓名和平均成绩(子查询和连接查询)
select stuname, avgmark from tb_student t1, (select stuid, avg(scmark) as avgmark from tb_score group by stuid) t2 where t1.stuid=t2.stuid;

select stuname, avgmark from tb_student t1 inner join 
(select stuid, avg(scmark) as avgmark from tb_score group by stuid) t2 on t1.stuid=t2.stuid;

-- 内连接（inner join）- 只有满足连接条件的记录才会被查出来
-- 外连接（outer join）- 左外连接(left outer join) / 右外连接(right outer join) / 全外连接
-- 查询每个学生的姓名和选课数量(左外连接和子查询)
select stuname, ifnull(total, 0) from tb_student t1 left outer join (select stuid, count(stuid) as total from tb_score group by stuid) t2 on t1.stuid=t2.stuid;