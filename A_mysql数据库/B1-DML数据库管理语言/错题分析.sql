在老表中查出数据，通过select后面接入一个新表，将数据传入新表后面
SELECT column_name(s)   【INTO new_table_name】 [IN externaldatabase] FROM old_tablename
      
 
 
 
【错题1】更新表中的数据的时候
update table
set 表中字段(使用逗号分割)
where 这里面才使用and
   
有一张Course表包含如下数据：
user_id   2
course_status  学习 Python
course_date  2021-09-30
 	
	 

现要把Course表中user_id为2的course_status更新为'学习SQL'，course_date更新为'2021-10-01'。下列MySQL语句中，正确的是： 
   
UPDATE Course SET course_status = '学习SQL', course_date = '2021-10-01' WHERE user_id = 2;      
      
      
