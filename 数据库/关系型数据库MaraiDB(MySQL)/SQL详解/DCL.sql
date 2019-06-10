-- 创建名为hellokitty的用户
create user 'hellokitty'@'%' identified by '123123';

-- 将对school数据库所有对象的所有操作权限授予hellokitty
grant all privileges on school.* to 'hellokitty'@'%';

-- 召回hellokitty对school数据库所有对象的insert/delete/update权限
revoke insert, delete, update on school.* from 'hellokitty'@'%';