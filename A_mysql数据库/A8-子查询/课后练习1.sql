1、查询和Zlotkey相同部门的员工的姓名和工资
select last_name ,salary
from employees
where department_id  in (select department_id from employees where last_name='Zlotkey')
[为什么用in，因为不确定姓名是不是不重复]

2、查询工资比公司平均工资高的员工的员工号，姓名和工资

select employee_id,last_name ,salary
from employees
where salary >(select AVG(salary) from employees )#这里是全员的工资，所以查出的薪资是单字段

3、选择工资大于所有(需要all关键字)job_id='SA_MAN'的员工的工资的员工的last_name,job_id,salary

select last_name,job_id,salary
from employees
where salary > all(
select salary 
from employees
where job_id = 'SA_MAN'
)

4、查询和姓名中包含字母u的员工在相同部门的员工的员工号和姓名【相关子查询】

select e1.employee_id ,e1.last_name
from employees  e1，
where  department in (e2.department_id e2 from employees 
where last_name like '%u%' )

5、查询在部门的location_id为1700的部门工作的员工和员工号
select employee_id
from employees
where department_id in
(select department_id
from departments
where location_id=1700);[从里往外写]，先查询部门id，

6\查询管理者是King的员工姓名和工资
【先查 管理者是Kingd的员工id，然后查询所在部门，然后查出所在部门下的员工信息】
[先查名字叫king的人的员工id，然后查询管理者id为员工id的人的信息]
select last_name,salary，manager_id
from employees
where manager_id in
(select employee_id 
from employees
where last_name = 'King')#查出来数据是100，156



7、查询工资最低水平的员工信息[聚合函数是min max mean]
select last_name,employee_id
from employees
where salary = (
select MIN(salary)
from employees)


8、查询平均工资最低的部门信息

#聚合函数不能嵌套，但是可以当作是一个新的表

【逻辑是什么？

1、需要先查出平均工资的所
2、】
select department_id,department_name,min(salaey)
from employees e1,(select AVG(salary) from employees) e2
where 

9、查询平均工资最低的部门信息和 该部门的平均工资（相关子查询）
where department_id = (select










