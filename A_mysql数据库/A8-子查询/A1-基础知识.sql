子查询：将一个查询语句放入一个查询语句中；


#比如查询工资大于‘abel’的人的姓名和工资

（1）自连接
select e.last_name,e.salary
from employees e ,employees d
where e.salary<d.salary
and e.last='Abel';查出名字叫abel的人，然后去另一张表中查比他大的值


（2）子查询
select e.last_name,e.salary
from employees e
where  e.salary>(select salary from employees where last_name='Abel');



规范：
1、外查询、和内查询 

内查询：（也叫子查询） 
      
      在主查询之前完成，（先计算）
外查询：待子查询的结果结束后，传递给外查询使用；

2、子查询需要使用 ()进行包裹




3、自查询的分类
  
  （1）单行查询
  （2）多行查询
  
  
  （3）相关子查询 



############################################################################################################

（1）单行子查询的案例分析
    
      单行比较符号  <= >= <>  != > <
      
      [案例分析]
      select last_name ,employee_id,salary
      from employees
      where salary > (
        select salary 
        from employees
        where employee_id=149
      )
      
      
      【案例分析2】返回job_id与141号员工相同，salary比143号员工多的员工姓名、job_id
      和工资
      select last_name,job_id ,salary
      from employees
      where job_id=(select job_id from employees where employee_id=141)
      and salary > (
        select salary 
        from employees
        where employee_id=149
      );
      
      【案例分析】返回公司工资最少的员工的last_name ，job_id 和salary
      select last_name ，job_id ,salary,
      from employees
      where salary=(select salary from employees where salary=min(salary)
      
      
      
      【案例分析】查询与141号或者174号员工的manager_id 和department_id相同的其他员工的manager_id，manager_id,employee_id
      select manager_id，manager_id,employee_id
      from employees
      where manager_id in (select manager_id from employees  where employee_id =141) 
      and department_id in (select department_id from employees  where employee_id=174)
      and employee_id<>141;
      
      【案例分析】
      【案例分析】
      
      
      


############################################################################################################






