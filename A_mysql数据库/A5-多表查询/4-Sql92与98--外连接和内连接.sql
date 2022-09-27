-- 1、内连接： 合并具有同一列的两个或者两个以上的表的行，结果集中【不包含】（一个表）和（另一个表）不匹配的行

-- 2、外连接：合并具有同一列的两个或者两个以上的表的行，结果集中【包含】（一个表）和（另一个表）不匹配的行外，包含左表或者右表外的值
--

--  外连接继续细分 :左外连接、右外连接、满外连接

-- 【内外连接的区分：是否返回包含表中不匹配的字段，内连接是不包含，外连接是包含】
-- 
-- 左外连接：两表的连接过程中返回包含条件的行外，还返回表中不满足条件的行（指的是左表）
-- 
-- 右外连接：两表的连接过程中返回包含条件的行外，还返回表中不满足条件的行（指的是右表）
-- 
-- 满外连接：两表的连接过程中返回包含条件的行外，还返回表中不满足条件的行（指的是左、右表）
-- 


#考题  查询‘所有的’员工的last_name 和department_name   【所有的：表示需要外连接，不然出现有些字段找不到】
#sql92的语法实现外连接  使用  +   ----【但是MySql不支持sql92】

#Sql99语法实现内连接    INNER JOIN ... ON
SELECT last_name,department_name
FROM employees INNER JOIN departments
ON employees.department_id=departments.department_id 
JOIN locations 
ON locations.location_id=departments.location_id;


#sql99实现左外连接  LEFT OUTER JOIN ... ON  (outer可以省略）
SELECT last_name,department_name
FROM employees LEFT OUTER JOIN departments
ON employees.department_id=departments.department_id;
-- JOIN locations 
-- ON locations.location_id=departments.location_id;
-- 

#sql99实现左外连接  RIGHT JOIN ... ON  (RIGHT可以省略）  [右外连接，指的是把右表的东西查出来，右表大于左表，那么左表【垫东西】]
SELECT last_name,department_name
FROM employees RIGHT JOIN departments
ON employees.department_id=departments.department_id 
JOIN locations 
ON locations.location_id=departments.location_id;


#满外连接  mysql不支持 full JOIN的格式  可以使用union  和 UNION all
-- 使用union  和 UNIONall的区别
-- UNION取两表的“并集” ---并且  去重
-- union all 取两表的并集---不去重
-- 【如果明确知道不存在重复场景，使用union all】
SELECT last_name,department_name
FROM employees Union ALL JOIN departments
ON employees.department_id=departments.department_id;

#7种join实现
#内连接
SELECT e.employee_id,d.department_id
FROM employees e join departments d
ON e.department_id=d.department_id;

#左外连接
SELECT e.employee_id,d.department_id
FROM employees e left join departments d
ON e.department_id=d.department_id;

#右外连接
SELECT e.employee_id,d.department_id
FROM employees e RIGHT JOIN departments d
ON e.department_id=d.department_id;

#查找两个图中“公共”的部分 ----可以在【左外连接】or【右外连接】的基础上去掉不匹配的部分;
#【因为左右连接的时候，有一边长，一边短的情况，----那么可以使用技巧，长的那个为null】
SELECT e.employee_id,d.department_id #左中图
FROM employees e LEFT JOIN departments d
ON e.department_id=d.department_id
WHERE d.department_id IS NULL;

SELECT e.employee_id,d.department_id #右中图
FROM employees e RIGHT JOIN departments d
ON e.department_id=d.department_id;
WHERE e.department_id is null;

#满外连接 【拿左连接的表，再拿有外连接表】
#左中图 并上 右中图  是中间空心的
SELECT e.employee_id,d.department_id
FROM employees e LEFT JOIN departments d
ON e.department_id=d.department_id
WHERE d.department_id IS NULL
UNION ALL
SELECT e.employee_id,d.department_id
FROM employees e RIGHT JOIN departments d
ON e.department_id=d.department_id;
WHERE e.department_id is null;



SELECT e.employee_id,d.department_id#右外连接
FROM employees e RIGHT JOIN departments d
ON e.department_id=d.department_id
UNION ALL
SELECT e.employee_id,d.department_id
FROM employees e LEFT JOIN departments d
ON e.department_id=d.department_id
WHERE d.department_id IS NULL;
