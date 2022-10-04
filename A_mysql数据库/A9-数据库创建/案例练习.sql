1、创建数据库test01_office ，指明字符集为utf8.并在此数据库下执行下述操作

create database if not exists test01_office  character set 'utf8'




2、创建表dept01
id （int(7))
name  varchar(25)

use test01_office;
create table if not exists dept01(id int(7),name varchar(25))  ;




3、将表departments中的数据插入信标dept02中 【使用as关键字】

create TABLE dept02
AS
select * from atguigudb.departments #atguigudb表示的是数据库




4、创建表emp01

id int(7)   first_name varchar(25)  last_name varchar(25)

create table if not exists emp01(
id int(7) ,first_name varchar(25) , last_name varchar(25),dept_id int(7));



5、将last_name 的长度增加到50 [修改表名---使用rename，修改表字段属性，使用rename---这些是DDL操作]
Alter table emp01
modify last_name varchar(50);


6、根据表employees创建emp02 【不要表中数据】
create table if not exists emp02
AS
select * from employees where 1=2;

7、删除表emp01
【尽量不使用truncate】
drop table emp01;


8、将表emp02重命名为emp01
【rename】

#Alter table emp02 [改表中字段]
rename table emp02 TO emp01;


9、在表dept02和emp01中添加新列test_column,并检查所作的操作


Alter table dept02 ADD colummn test_column varchar(15)
Alter table emp01 ADD colummn test_column varchar(15) first;


10、直接啥暗处表emp01中的列dept_id

alter table emp01
drop column dept_id;






【练习2】
1、创建数据库 test02_market

create database  test02_market;

2、创建数据表customers

use test02_market；
create table if not exists customers

3、将c_contact 字段移动到c_birth字段后面

alter table customers
add  c_contact after c_birth
  
4、将c_name 字段数据类型改为varchar(70)  使用change关键字
alter table customers
CHANGE  c_name varchar(70)
















