1、如何实现多表查询？

【注意】什么时候可以不使用  表.字段名,查询的字段只存在自己的表中

（1）笛卡尔积
SELECT last_name,department_name
FROM employees,departments;
    【出现笛卡尔错误的原因，缺少了多表的连接条件】

笛卡尔积：  mxn；



（2）多表查询到正确方式：需要有连接条件

SELECT last_name,department_name
FROM employees,departments
WHERE employees.employee_id=departments.department_id; 【连接条件】



（3）当这个字段，在不同的表都出现的时候，应该使用 【表.ziduan】
    
  
  如果查询语句中出现多个表中都存在的字段，则必须指明此字段


    
（4）给表起一个别名 ，在select和where中 给字段 或者表名 起别名

        SELECT emp.last_name,dep.department_name
        FROM employees emp,departments dep

（5）练习 查询三张表中员工中的信息；
SELECT emp.employee_id,emp.last_name,dep.department_name,loc.city
FROM employees emp,departments dep,locations loc
WHERE emp.department_id=dep.department_id AND dep.location_id=loc.location_id;
