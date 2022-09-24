#选择工资不在5000 到 12000的员工的姓名和工资
SELECT employees.last_name '姓名', employees.salary '工资' FROM employees WHERE salary NOT BETWEEN 5000 AND 12000 ;

#选择在20到50号部门工作的员工姓名和部门号

SELECT last_name,department_id FROM employees WHERE job_id IN (20,30,40,50) ;

#选择公司中没有管理者的员工姓名以及job_id
SELECT last_name,job_id FROM employees WHERE manager_id IS NULL ;

#选择公司中有奖金的员工姓名、工资和奖金级别

SELECT last_name,salary,commission_pct FROM employees WHERE commission_pct IS NOT NULL;

#选择员工姓名的第三个字母是a的员工姓名

SELECT last_name FROM employees WHERE last_name  like '__a%';
-- SELECT last_name FROM employees WHERE last_name LIKE '%A%';
#选择姓名中有字母a和k的员工姓名
SELECT last_name FROM employees WHERE last_name like "%a%k%"  OR  last_name like "%k%a%";

#显示出表employees 表中first_name 以e结尾的员工信息(all)
SELECT * FROM employees WHERE first_name  REGEXP 'e$';

#显示出e~部门编号在80~100之间的 name 、工种
SELECT first_name, job_id FROM employees WHERE department_id BETWEEN 80 AND 100;

#显示出 manager_id 是100，101，110 的姓名、工资、管理者id
select last_name ,salary,manager_id FROM employees WHERE manager_id in (100,101,110);

DESC employees;

SELECT employee_id FROM employees;
