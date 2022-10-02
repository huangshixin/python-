1、查询员工中工资大于本公司平均工资的员工的last-name salary 、department_id

select last_name,salary,department_id
from employees
where salary > (select avg(salary) from employees );不相关子查询，【主查询和子查询的表，没有关联语句】



2、查询员工中工资大于本部门平均工资的员工的last-name salary 、department_id
select e1.last_name,e1.salary,e1.department_id
from employees e1
where salary > (select avg(salary) from employees e2 where
e1.department_id = e2.department_id
);相关子查询，【主查询和子查询的表，关联语句】


写法 2：在from中声明子查询
select e1.last_name ,e1.salary ,e1.department_id
from (select departmen_id,last_name,AVG(salary) avg_val
from employees
group by department_id) e1 ,employees e2
where e1.department_id = e2.department_id and e2.salary > e2.avg_val;





3、可以在where中、from、order by中使用子查询

select\where\order by\ from  中都可以使用子查询



4、exist  和 not exist 关键字
exist每次去子查询中找，如果返回True就不找了，否则继续找【目的是查找记录】

not exist 就是当找到一条是False，直接返回；【查询department表中不存在于employees中的记录】


select e1.department_id
from employees e1
where not exist 
(
select * 
  from employee e2
  where e1.department_id=e2.department_id

)#相当于拿到e1去e2中去寻找，是否存在e2表中，如果没有就返回


