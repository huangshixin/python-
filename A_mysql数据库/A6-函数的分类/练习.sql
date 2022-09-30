1、显示系统时间 （日期＋时间）
select now() sysdata() current_timestamp() localtime() from dual;

2、查询员工号、姓名、工资、以及工资提高百分之20%后的结果（new salary）
select employees_id,last_name,salary,salary*1.2 new salary
from employees;

3、将员工的姓名按照首字母排序，并写出姓名的长度（length）
select last_name,LENGTH(last_name) 'length'
from employees
order by last_name (按照首字母进行排序 直接desc or asc)

4、查询员工id，last_name，salary，并作为一个列输出，别名为out_put[意思是将几个字符串按照列a]
select concat(employee_od ,last_name,salary ) 'out_put' 
from employees;

CONCAT(s1,s2,......,sn) 连接s1,s2,......,sn为一个字符串
CONCAT_WS('_',NAME1,NAME2，...)
5、查询公司各员工工作的年数、工作的天数，并按工作的年数的降序排列
select DATEDIFF(CURDATE(),hire_date)/365  'year',DATEDIFF(CURDATE(),hire_date) 'day'
from employees
order by year desc;
To_DAYS(CURDATE())-TO_DAYS(Hire_date) 计算出多少天

6、查询员工姓名，hire_data,department_id,满足以下条件；雇佣时间在1997年之后，department_id为80or90or110，commission_pct不为null
select last_name,hire_data,department
from employees
where heir_date >='1997-01-01' and #存在的隐式转换
Department_id in (80,90,110) and 
commission_pct is not NULL

改造

select last_name,hire_data,department
from employees
where heir_date >=date_format(hire_date,"%y-%m-%d)>='1997-01-01' and #存在的隐式转换
Department_id in (80,90,110) and 
commission_pct is not NULL

7、查询公司中入职超过10000天的员工姓名、入职时间；
select last_name ,hire_data
from employees
where DATEDIFF(CURDATE(),hire_date)>=10000;

8、查询结果，展示以下效果
<last_name> earns <salary> monthly but wants <salary*3>

select concat(last_name,'earns',truncate(salary,0),'monthly but wants',truncate(salary*3.0,0)) 'Dream salary'
from employees;

小数点处理 truncate(salary,0)



9、使用case when
select  j.job  case job when AD_PERS THEN A
                      WHEN ST_MAN THEN B
                      WHEN IT_PROG THEN C
                      WHEN SA_RED THEN D
                      WHEN ST_CLERK THEN E
                      END 'grade'
from employees e join job j
on e.id=j.id;
                      
