1、排序-------【默认asc】
  
  使用 order by 对查询的数据进行排序操作
  
  【语法】  order by  ‘key’ desc； 按照key --降序排序
  【语法】 order by ‘key’ asc； 按照key  升序排序
  
SELECT employee_id,last_name,salary
FROM employees
ORDER BY salary DESC;



2、按照列的别名进行排序 ----【在order by中可以使用别名排序】

  
SELECT employee_id,last_name,salary*12 'key'
FROM employees
ORDER BY key DESC;
