1、常见的几个聚合函数
    1、AVG/SUM  
    2 MAX/MIN 求最大值 和 求最小值
    3 COUNT  求个数
    4、方差和标准差、中位数

select avg(salary),sum(salary),AVG(salary)*107 from employees;

select count(last_name) from employees;

select sum(commission_pct)/count(IFNULL(comission_pct,0))
from employees;

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
2、group by的使用 【作用就是分组】

      select deppartment_id,last_name
      from employees
      group by depatment_id  [需要有重复的字段]，否则无效

      假定只按照某一个组进行排序，求平均工资
      select job_id, AVG(salary)
      from employees
      group by job_id;

      查询各个 department_id ,job_id 的平均工资；  【加上job id 和 department id是增加可读性】
      select department_id, job_id,AVG(salary)
      from employees
      group by job_id,department_id;
      
      【结论，select中的【非主函数的字段】一定要出现在group by中，但是 group by中的字段，不一定需要出现在select】

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%




3、HAVING 

结论：  如果我们的过滤条件中【聚合函数】，则使用having，不能使用where

    1、Having 必须放在group by的后面
    2、使用having的时候需要分组；
    3、having需要和group by一起使用
select > from>where > order by >group by >Having



4、SQL底层执行原理
