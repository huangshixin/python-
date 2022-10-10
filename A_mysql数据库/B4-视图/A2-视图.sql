视图是一种 【虚拟表】 ，本身是 【不具有数据】 的，占用很少的内存空间，它是 SQL 中的一个重要概念。
视图建立在已有表的基础上, 视图赖以建立的这些表称为【基表】。

1、视图只能够查询，而如果想对视图中的数据进行增删改，实际上是对原来的组合的表进行修改；
-------------【存储起来的select语句】--------
（1）删除视图本身，不影响结果，相当于删除select语句
（2）视图能够简化查询
 (3)虚拟表，本身不具有数据
（4）视图中使用select的表 都称之为基表


2、语法：
【精简的方法---创建视图】
CREATE VIEW 视图名称
AS 查询语句



EP：【针对单表创建视图】
CREATE VIEW empvu80
AS
SELECT employee_id, last_name, salary
FROM employees
WHERE department_id = 80;


【tips】 
与insert into as  select语句一致，如果查询的结果中赋予了【字段别名】，那么视图中的字段名将用这些别名代替；

CREATE VIEW empvu80(id,name,salary_s)#这一部分称为别名，需要与select中的字段进行【一一对应】
AS
SELECT employee_id, last_name, salary
FROM employees
WHERE department_id = 80;


2.2【视图---多作用于多表查询,以及搭配聚合函数】
1、建议不需要额外赋予别名，由于查询的结果在之前的表中不一定存在
create view vu_emps
AS
SELECT e.employee_id,e.department_id,d.department_name
FROM employees e  JOIN departments d
ON e.department_id = d.department_id;


2.3【基于视图创建视图】
1、把视图当作是一个表，对视图进行查询

CREATE VIEW emp_dept_ysalary
AS
SELECT emp_dept.ename,dname,year_salary
FROM emp_dept INNER JOIN emp_year_salary
ON emp_dept.ename = emp_year_salary.ename;

2.4 【查看视图】
show tables;

desc关键字;---查看结构

show table states like 'vi_emp';

show create view_name;


2.5【更新视图的数据】

#创建视图
create view vu_em
AS
select e.employee_id,e.last_name,e.salary
from employees e


SELECT * FROM vu_em;

select count(*) FROM vu_em;

【#对视图中的数据进行修改和查看】
update vu_em
set salary = 20000
WHERE employee_id=101;

【查看基表中的数据----发现已经改变】
select salary
from employees
where employee_id=101;


总结：
【一般情况下】
1、更新基表或者视图，那么两表的值都是会发生改变的
2、删除视图中的数据，基表中的数据也会发生改变

【不能更新的情况下】
1、更新的数据不是基表中存在的，【可能是通过聚合函数的基础上获得的】
2、它存在的目的就是为了查询



2.6【修改视图】

语法：【这个语法表示的是如果视图存在就替换，不存在就创建】
create or replace view  视图名
as
select 查询语句



EP:
create or REPLACE view vu_em
as
SELECT employee_id,last_name,salary,email
FROM employees;
################################################################################

语法 2: 修改视图  【这里和修改表的语法一致 不过关键字table变成了view】
Alter view 视图名
as
查询语句

EP:
ALTER view vu_em
as
SELECT employee_id,last_name,salary,email
FROM employees;


2.7【删除视图】
drop view 视图名；  不使用delete，因为这个是清空数据的

delete from table_name where condition（筛选条件）



