/*
等值连接  & 非等值连接

自连接 vs 非自连接

内连接  vs  外连接
*/


1、等值连接 =

2、非等值连接 （不含等于号）
SELECT emp.last_name ,emp.salary,job.grade_level 
FROM employees emp, job_grades job
WHERE emp.salary BETWEEN job.lowest_sal AND job.highest_sal;









3、自连接（表 ，自己连接自己）
    #员工id和姓名，及其管理者的id和姓名
  
SELECT emp.last_name,emp.employee_id,map.manager_id,map.last_name
FROM employees emp,employees map
WHERE emp.manager_id=map.employee_id;#map表的id正好等于 员工表的管理者id
