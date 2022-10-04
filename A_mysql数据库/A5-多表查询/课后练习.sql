注意事项：超过三张表 不要使用join  否则相当于三层for循环


# 1.显示所有员工的姓名，部门号和部门名称。
#满连接
SELECT e.last_name ,d.department_id,d.department_name
FROM employees e LEFT JOIN departments d
ON e.department_id=d.department_id
UNION ALL
SELECT  e.last_name ,d.department_id,d.department_name
FROM employees e RIGHT JOIN departments d
ON e.department_id IS Null;
# 2.查询90号部门员工的job_id和90号部门的location_id
SELECT e.job_id,l.location_id
FROM employees e JOIN departments d
ON e.department_id=d.department_id join locations l
on d.location_id=l.location_id
WHERE e.department_id=90;

# 3.选择所有有奖金的员工的 last_name , department_name , location_id , city
SELECT e.last_name,d.department_name,l.location_id,l.city
FROM employees e , departments d,locations l
WHERE e.department_id=d.department_id AND l.location_id=d.location_id
AND e.commission_pct is NOT Null;

# 4.选择city在Toronto工作的员工的 last_name , job_id , department_id , department_name【内连接】
SELECT e.last_name,e.job_id,d.department_id,d.department_name
FROM employees e JOIN departments d ON e.department_id=d.department_id
JOIN locations l ON l.location_id=d.location_id AND l.city='Toronto';

# 5.查询员工所在的部门名称、部门地址、姓名、工作、工资，其中员工所在部门的部门名称为’Executive’【内连接是满足i傲剑的】
SELECT d.department_name,e.last_name,j.job_title,e.salary
FROM employees e JOIN departments d ON e.department_id=d.department_id AND d.department_name='Executive'
join jobs j ON e.job_id=j.job_id ;

desc jobs;

# 6.选择指定员工的姓名，员工号，以及他的管理者的姓名和员工号，结果类似于下面的格式
SELECT emp.last_name employees, emp.employee_id "Emp#", mgr.last_name manager,
mgr.employee_id "Mgr#"
FROM employees emp
LEFT OUTER JOIN employees mgr
ON emp.manager_id = mgr.employee_id;

# 7.查询哪些部门没有员工
SELECT d.department_name
FROM employees e right join departments d
ON e.department_id=d.department_id
WHERE e.department_id IS Null;

-- # 8. 查询哪个城市没有部门
SELECT l.location_id,l.city
FROM employees e JOIN departments d
ON e.department_id=d.department_id RIGHT JOIN locations l
ON l.location_id=d.location_id 
WHERE d.location_id is Null;
# 9. 查询部门名为 Sales 或 IT 的员工信息  
#【这个直接内连接即可】
SELECT employee_id,last_name,department_name
FROM employees e,departments d
WHERE e.department_id = d.`department_id`
AND d.`department_name` IN ('Sales','IT');


-- SELECT employee_id,last_name,department_name
-- FROM employees e,departments d
-- WHERE e.department_id = d.`department_id`
-- AND d.`department_name`='Sales' or d.department_name='IT';
-- 




#1.所有有门派的人员信息
SELECT *
FROM t_dept t1 JOIN t_emp t2
ON t1.id=t2.deptId;
#2.列出所有用户，并显示其机构信息
SELECT *
FROM t_emp a left JOIN t_dept b
ON a.deptId=b.id;
#3.列出所有门派
SELECT *
FROM t_emp a RIGHT JOIN t_dept b
ON a.deptId=b.id;
#4.所有不入门派的人员(a独有，a>b)  因此 b is null
SELECT *
FROM t_emp a left JOIN t_dept b
ON a.deptId=b.id
WHERE b.id is NULL;
#5.所有没人入的门派
SELECT *
FROM t_emp a RIGHT JOIN t_dept b
ON a.deptId=b.id
WHERE a.deptId IS Null;
#6.列出所有人员和机构的对照关系
SELECT *
FROM t_emp a left JOIN t_dept b
ON a.deptId=b.id
UNION ALL
SELECT *
FROM t_emp a RIGHT JOIN t_dept b
ON a.deptId=b.id
WHERE a.deptId IS Null;


SELECT *
FROM t_emp a RIGHT JOIN t_dept b
ON a.deptId=b.id
UNION ALL
SELECT *
FROM t_emp a RIGHT JOIN t_dept b
ON a.deptId=b.id
WHERE a.deptId IS Null;


#MySQL Full Join的实现 因为MySQL不支持FULL JOIN,下面是替代方法
#left join + union(可去除重复数据)+ right join
#7.列出所有没入派的人员和没人入的门派  [在遇到两张表都要求‘没有’这种字眼的时候，需要考虑把满外连接-共有的部分]
-- （A的独有+B的独有）
-- 
SELECT *
FROM t_emp a left JOIN t_dept b
ON a.deptId=b.id
WHERE b.id is NULL;
UNION all
SELECT *
FROM t_emp a RIGHT JOIN t_dept b
ON a.deptId=b.id
WHERE a.deptId IS Null;

