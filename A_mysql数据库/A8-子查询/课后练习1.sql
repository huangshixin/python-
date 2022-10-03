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
select department_id,department_name,AVG(salaey)
from employees 
group by department_id
where salary =
(select min(salary) from (select AVG(salary) from employees) avg_al )#将这个表查出来当作新的表


方式2：
1、先按照部门进行平均工资查询，按照部门进行排序
2、使用having进行赛选 平均工资大于所有部门平均工资的【部门id】
3、查询部门id中的每种信息
select *
from departments
where department_id =(
                  select department_id
                  from employees
                  group by department_id
                  Having AVG(salary) <=ALL(
                                    select AVG(salary)
                                    from employees
                                    group by department)
                   );



9、查询平均工资最低的部门信息和 该部门的平均工资（相关子查询）

【在8的基础上修改】
select  department_id,AVG(salary)
from departments
where department_id
=(
select department_id
from employees
Having AVG(salary)<ALL(
(select AVG(salary)
from employees
group by department)
);


10 查询平均工资最高的job信息

select e1.job_id,e1.job_name
from eployees e1,job j
where e1.salary=(
From max(avg_val)
(select AVG(salary) avg_val from employees group by job_id) t_job)
and j.job_id=e1.job_id


select *
from jobs
where job_id =(
          select job_id
          from employees
          group by job_id
          Having AVG(salary) >=ALL(#avg(salary) 表示的是按照job排序后的avg的平均值
                            select AVG(salary) avg_val
                            from employees
                            group by job_id
                            )
            );

方式三：优化

select *
from jobs
where job_id =(
          select job_id
          from employees
          group by job_id
          Having AVG(salary)
                    =
                            (select AVG(salary) avg_val#查到平均值，并且逆序排序，然后查找出第一条数据，就是最大的
                            from employees
                            group by job_id
                            order by avg_val desc
                            limit 0,1
                            )
                      );


11查询平均工资高于公司平均工资的部门有哪些？

select department_name,department_id
from employees
group by department_id
where avg(salary) >(
select avg(salary) from employees) #不需要排列,因为只有一列
12 查询出公司中所有manager的详细信息
【这个表中存在 employee_id  manager_id,job_id,department_id；其中查出的manager_id也是一个员工id】
select e1.employee_id,e1.last_name
from employees e1 join (select manager_id from employees ) e2
on e1.employee_id = e2.manager_id


[子查询]
。。。
  + employee_id IN (select manager_id from employees )

【使用exist关键字】
where exist (
        select * 
        from employee e2
        where e1.employee_id = e2.manager_id
)

13  各个部门中，最高工资中最低的那个部门的最低工资是多少？

#找到最大工资
select max(salary)
from employees
group by department_id
#接着找最大中的最低工资
select table.salary
from (select max(salary) avg_val
      from employees
      group by department_id
      order by avg_val
      limit 0,1) table
#接着找部门
select department_id
from employees
group by department_id
where salary=(select table.salary
from (select max(salary) avg_val
      from employees
      group by department_id
      order by avg_val
      limit 0,1) table)


14  查询平均工资最高的部门的manager的详细信息：last_name,department_id,email,salary

---

15  查询部门的部门号，其中不包括job_id是“ST_CLERK"的部门号

select department_id
from departments
where department_id in (
select department_id
from employees
where job_id<>'ST_CLERK')

16 选择所有没有管理者的员工的last_name【not exists】


select last_name
from employees emp
where not exist (
            select * 
            from employees mgr
            where emp.employee_id = mgr.manager_id) #把符合条件的排除就是 不符合条件的




select 





