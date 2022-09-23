1、补充一个概念 DUAL伪表

2、select 1+1 from DUAL;  为了满足最基本的 select ... from结构；

3、select * from table_name;  *表示查询所有的数据

4、列的别名；
  (1) 设置别名的两种方式 1 直接加上 “空格” ----【建议在别名的基础上 加上一个双引号】
  select cloumn_name1  别名1 , column_name2 from  table_name;
  （2）设置别名的第二种方式 使用  AS
  select colunmn_name  as 别名 from table_name ; 
  
  【注意 别名之间是不能有空格的】
  
  
 5、【去除冗余项】 ----使用 distinct关键字

  SELECT DISTINCT employee_id as 'id' FROM employees;

6、空值参与运算；
  
  null 与其它进行运算的时候，都默认为null ，同时需要注意的是，null 不等同于 0；
  
  
 7、着重号 ''

  select * from 'order';  当你出现 字段名 和 表名 出现 与 mysql 关键字相同的时候 ，你需要添加 [着重号]
  
  
 8、查询常数

select 'changshu' , column from table_name; 如果你使用的常数不存在这个表中，那么现在在查询的时候，就会直接给它进行 按列匹配；

9、查询表结构  [关键字 desc]

DESCRIBE 

DESC departments;
  

