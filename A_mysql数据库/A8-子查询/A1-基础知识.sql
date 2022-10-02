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
      
      【案例分析】子查询写入到having中　ｈａｖｉｎｇ　ｍｉｎ（ｓａｌａｒｙ）　＞　（ｓｅｌｅｃｔ　．．．）
      【案例分析】
      
      
      


############################################################################################################
                    
       #多行子查询
                    （1）子查询的语句返回多行数据
                    （2）in：等于列表中的任意一个
                    （3）any：满足其中一个就行，比如 
                    （4）all：要求全都都匹配
                    （5）some：作用与any一样
      (1)案例
      select last_name ,employee_id,salary
      from employees
      where salary in (
        select min(salary)
        from employees
      ) 
                    （2）案例：
                    any/all
                    返回其它job_id中比job——id为'IT_PROG'部门任一工资低的员工的员工号、姓名、job_id以及salary
                    
                    select employee_id,last_name,job_id,salary
                    from employees 
                    where job_id<>'IT_PROG'  #这里是筛选 不等于 'IT_PROG'
                    and  salary < any(
                          select salary
                          from employees
                          where job_id='IT_PROG'
                          )#查询job_id为it——prog的人的工资 ，然后查询 salary< any（）的值
                    
                    （3）案例;在2的基础上查询所有
                    
                    select employee_id,last_name,job_id,salary
                    from employees 
                    where job_id<>'IT_PROG'  #这里是筛选 不等于 'IT_PROG'
                    and  salary < all(
                          select salary
                          from employees
                          where job_id='IT_PROG'
                          )#查询job_id为it——prog的人的工资 ，然后查询 salary< any（）的值
                    这里查出的工资不是一个值，是一个列表，所以你要使用这个的时候，需要考虑的是all
                    
                    
                    
                    （4）查询平均工资最低的部门id【mysql聚合函数不能嵌套，orecle可以】
                    select department_id 
                    from employees
                    group by department_id
                    having AVG(salary) =(
                    select min(e.salary)
                     from  (select AVG(salary) avg_sal
                    from employees
                    group by department_id))   e#把这个查询结果当作一个表  from（）
                    
                    
                    继续改造
                    
                    select department_id
                    from employees
                    group by department_id
                    having AVG(salary) <=ALL(#查询平均工资最低的情况 <=ALL，就可以小于其中最小值
                          select AVG(salary) 
                          from employees
                          group by department_id ）  按照部门的id进行排序，它的平均工资
                          
                    
                                             
        5、空值问题
                    如何处理空值id【当内查询中有空值的时候，使用子查询判断语句将会出现空】
                                             
                    
                    
                    
                    
                    






