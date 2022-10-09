1、从MYSQL8.0开始不支持使用全连接,全连接的实现方式---需要使用外连接+ 右连接

Mysql(版本8.0.25)不支持full join，执行报错【1064 - You have an error in your SQL syntax; 
check the manual that corresponds to your MySQL server version for the right syntax to use near 'full  join 】

Mysql(版本8.0.25)中表student_table(id,name,birth,sex)，插入如下记录：
('1004' , '张三' , '2000-08-06' , '男');
('1005' , NULL , '2001-12-01' , '女');
('1006' , '张三' , '2000-08-06' , '女');
('1007' , ‘王五’ , '2001-12-01' , '男');
('1008' , '李四' , NULL, '女');
('1009' , '李四' , NULL, '男');
('1010' , '李四' , '2001-12-01', '女');
执行
select count(t2.birth) as c1
from (
select * from student_table where sex = '男' ) t1 
full  join 
(select * from student_table where sex = '女') t2 
on t1.birth = t2.birth and t1.name = t2.name ; 
的结果行数是（）？   【直接报错】
