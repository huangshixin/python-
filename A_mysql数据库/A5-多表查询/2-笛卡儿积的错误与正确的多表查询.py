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

