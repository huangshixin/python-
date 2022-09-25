1、排序-------【默认asc】
  
  使用 order by 对查询的数据进行排序操作
  
  【语法】  order by  ‘key’ desc； 按照key --降序排序
  【语法】 order by ‘key’ asc； 按照key  升序排序
  
SELECT employee_id,last_name,salary
FROM employees
ORDER BY salary DESC;



2、按照列的别名进行排序 ----【在order by中可以使用别名排序】
【ads】别名
  
SELECT employee_id,last_name,salary ads
FROM employees
ORDER BY ads DESC;



3、order 必须放在 where之后  【如果有where】



4、order by中的排序内容，不需要是查询的字段；
