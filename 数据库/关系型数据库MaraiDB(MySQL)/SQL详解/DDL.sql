-- 如果存在名为 school 的数据库就删除它
DROP DATABASE IF EXISTS school;

-- 创建名为 school 的数据库并设置默认的字符集和排序方式
CREATE DATABASE 'school' CHARACTER SET utf8;

-- 切换到 school 数据库上下文环境
USE school

-- 创建学院表
CREATE TABLE tb_college
(
    collid INT NOT NULL auto_increment comment '编号',
    collname VARCHAR(22) NOT NULL comment '名称',
    collmaster VARCHAR(20) NOT NULL comment '院长',
    collweb VARCHAR(511)  default '' comment '网站',
    PRIMARY KEY (collid)
);

-- 创建学生表
CREATE TABLE tb_student
(
    stuid INT NOT NULL comment '学号',
    stuname VARCHAR(20) NOT NULL comment '姓名',
    stusex BIT DEFAULT 1 comment '性别',
    stubirth DATE NOT NULL comment '出生日期',
    stuaddr VARCHAR(255) DEFAULT '' comment ' 籍贯',
    collid INT NOT NULL comment '所属学院',
    PRIMARY KEY (stuid),
    FOREIGN KEY (collid) REFERENCES tb_college (collid),
);

-- alter table tb_student add constraint fk_student_collid ......

-- 创建教师表
CREATE TABLE tb_teacher
(
    teaid INT NOT NULL comment '工号',
    teaname VARCHAR(20) NOT NULL comment '姓名',
    teatitle VARCHAR(10) DEFAULT '助教' comment '职称',
    collid INT NOT NULL comment '所属学院'
    PRIMARY KEY (teaid),
    FOREIGN KEY (collid) REFERENCES tb_college (collid)
);

-- 创建课程表
CREATE TABLE tb_course
(
    couid INT NOT NULL comment '编号',
    couname VARCHAR(50) NOT NULL comment '学分',
    teaid INT NOT NULL comment '授课老师',
    PRIMARY KEY (couid),
    FOREIGN KEY (teaid) REFERENCES tb_teacher (teaid)
);

-- 创建选课记录表
CREATE TABLE tb_score
(
    scid INT auto_increment comment '选课记录号',
    stuid INT NOT NULL comment '选课学生',
    couid INT NOT NULL comment '所选课程',
    scdate DATETIME comment '选课时间日期',
    scmark DECIMAL(4,1) comment '考试成绩',
    PRIMARY KEY (scid),
    FOREIGN KEY (stuid) REFERENCES tb_student (stuid),
    FOREIGN KEY (couid) REFERENCES tb_course (couid)
);

-- 添加唯一性约束(一个学生选某个课程只能选一次)
ALTER TABLE tb_score add CONSTRAINT uni_score_stuid_couid UNIQUE (stuid,couid);