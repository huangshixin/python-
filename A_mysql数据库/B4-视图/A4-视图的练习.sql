-- 1、使用表employees创建视图employee_vu,其中包括 姓名、员工号、部门号
-- 

create view employee_vu
AS
SELECT last_name,employee_id,department_id
FROM employees;


-- 2、显示视图的结构
desc employee_vu; 


--  3、查询视图中的全部内容
select * FROM employee_vu; 


SELECT DISTINCT department_id FROM employee_vu;

-- 将视图中的数据限定在部门号是80的范围内【这里存在两种方式 ：1、使用create or replace view  2、使用alter view】

CREATE OR REPLACE VIEW employee_vu 
AS
SELECT last_name,employee_id,department_id
FROM employees
WHERE department_id=80;






#1. 创建视图emp_v1,要求查询电话号码以‘011’开头的员工姓名和工资、邮箱
desc employees;

CREATE VIEW emp_v1
AS
select last_name,salary,email
FROM employees
WHERE phone_number like "011%";


select count(*) FROM emp_v1;



#2. 要求将视图 emp_v1 修改为查询电话号码以‘011’开头的并且邮箱中包含 e 字符的员工姓名和邮箱、电话号码
create or REPLACE view emp_v1
AS
SELECT last_name,salary,email
FROM employees
WHERE phone_number like "011%" AND email like "%e%";

select * FROM emp_v1;





#3. 向 emp_v1 插入一条记录，是否可以？
insert into emp_v1
values('Russell',	14000.00	'JRUSSEL');
-- 【不能向视图中插入记录】


#4. 修改emp_v1中员工的工资，每人涨薪1000
#【update可以不使用where语句】
update emp_v1
set salary=salary+1000;


#5. 删除emp_v1中姓名为Olsen的员工
select * FROM emp_v1;

delete from emp_v1
where last_name = 'Russell';



#6. 创建视图emp_v2，要求查询部门的最高工资高于 12000 的部门id和其最高工资
select department_id,max(salary)
FROM employees
GROUP BY department_id
HAVING max(salary)>12000;

CREATE VIEW emp_v2
AS
select department_id,max(salary)
FROM employees
GROUP BY department_id
HAVING max(salary)>12000;

#7. 向 emp_v2 中插入一条记录，是否可以？
#【不可以】
#8. 删除刚才的emp_v2 和 emp_v1
drop view if exists  emp_v2 ,emp_v1;

