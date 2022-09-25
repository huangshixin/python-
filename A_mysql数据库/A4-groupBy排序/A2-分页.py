1、分页  --limit 

#偏移量 0，显示条目数
SELECT employee_id,last_name,salary ads
FROM employees
LIMIT 0,20;

#显示第二页 在原先的基础上加上偏移量 
SELECT employee_id,last_name,salary ads
FROM employees
LIMIT 20,20;


2、显示第Number页的pagesize条
#公式 limit (Number-1)*pagesize,pagesize=====推导出来，显示第i页，（i-1）*pagesize，pagesize;   i>=1;




3、where    order by   limit

limit 10， 条目数等价于 limit 0,10
但是， 你要是从1开始，那就不行了

SELECT * FROM employees #查找第32，33数据 ，那么偏移量减去1，显示2条；
LIMIT 31,2  



4、Mysql 8.0新特性  limit  'pageSize' offset ‘偏移量’；【显示第32，33条数据】
SELECT * FROM employees 
LIMIT 2 OFFSET 31;
