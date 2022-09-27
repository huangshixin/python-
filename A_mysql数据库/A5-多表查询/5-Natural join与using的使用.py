#1、自然连接 NATURAL JOIN
SELECT e.employee_id,d.department_id
FROM employees e  NATURAL JOIN departments d
# 会自动查询多张表中的相同字段的值


#2、USING连接 USING （字段）
SELECT e.employee_id,d.department_id
FROM employees e  JOIN departments d#这个别名 到不了using
USING (department_id);
#查询给定的匹配字段



