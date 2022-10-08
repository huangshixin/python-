1、添加数据
use atguigudb

create table if not exists  emp1{
id int
name varchar(15)
hire_date date
salary double(10,2)
};


DESC emp1;

方式1： 一条一条数据的添加
      （1）不署名添加
      insert into emp1
      values (1,'TOM','2020-12-21',3400);  一定要按照声明的顺序添加；【这种方式不太好】
      （2）署名添加
      insert into emp1(id,hire_date,salary,'name')#按照提供的名字顺序进行添加
      values(2,'2020-10-2',4000,'TOS')
      （3） 署名添加多条【模板】
      insert into emp1(id,hire_date,salary,'name')
       values(2,'2020-10-2',4000,'TOS'),
       values(2,'2020-10-2',4000,'TOSE'),
       values(2,'2020-10-2',4000,'TOS');
       
方式2：将查询结果插入到表中[这种方式比较好]

       SELECT * FROM emp1;
       
       #使用查询语句 ，将查询的数据添加到表中【字段的类型需要一致】
       insert into emp1(id,name,salary,heir_date)
       select employee_id,last_name,salary,heir_date
       from employees
       where department_id in (70,60);
       
       
       #新的方法： 在查询的时候，直接into到一张表中；into seniordrivers----牛客题
       select * into seniordrivers from drivers where drivedistanced >=5000;
       
       
      INSERT INTO 语句用于向表格中插入新的行。
      INSERT INTO table_name VALUES (值1, 值2,....)
      指定所要插入数据的列：
      INSERT INTO table_name (列1, 列2,...) VALUES (值1, 值2,....)
      SELECT INTO 语句从一个表中选取数据，然后把数据插入另一个表中。常用于创建表的备份复件或者用于对记录进行存档。
      把所有的列插入新表 
      SELECT *
      INTO new_table_name [IN externaldatabase] 
      FROM old_tablename
      只把希望的列插入新表 
      SELECT column_name(s)
      INTO new_table_name [IN externaldatabase] 
      FROM old_tablename


【规范】
            insert into table_name(table_columns1,table_columns2,...)
            values(...),
            values(...);


            insetr into table_name(table_columns1,table_columns2,...)
            select columns1,columns2,...
            from table_name
            where ...





[修改数据]

            UPDATE ... SET ...WHERE[where不能丢]


            #批量的数据修改
            update emp1
            set hire_date = CURDATE()
            WHERE id = 5;

            #同时修改一条数据的多个字段
            update emp1
            set heir_date = CURDATE(),SALARY = 6000
            WHERE id =5;


【修改不成功原因】
1、可能是由于外键约束









【删除数据】delete from 。。。 where

delete from emp1
where id=1;


delete from departments
where department_id =50;





MYSQL  8.0：计算列

假定a,b,c 有三列，a，b都有值，c是通过a+b得到的，，所以c是计算列【加速查询效率】


案例分析


use atguigudb

create table teste1(
a INT,
b INT,
c INT generated always AS (a+b) VIRTUAL);




【综合案例】
1、创建数据库test01_lib
create databses if not exists test01_lib character set 'utf8';

2、创建表 books，表结构如下
create table if not exists books(
id int,
name varchar(15),
authors varchar(10),
price float(10,2),
pubdate year,
note varchar(10),
num int
)

3、添加数据

      (1)不指定字段
      insert into books
      values('tal of AAA','Dickes',23,'1995',noval);
      (2)插入多条
      insert into books(name ,authors,price,pubdate,note)
      values('tal of AAA','Dickes',23,'1995',noval),
      value(...),
      ...
      value(...);


4、将小说类型novel的书的价格都增加5
update books
set price=price+5
where note='novel'


5、将名称为EmmaT的书的价格改为40，并将说明改为drama
【建议在增删改之前，先做一个查询操作】
update books
set price=40,note='drama'
where name='EmmaT' and


6、删除库存为0的记录

delete from books
where num=0;

7、统计署名中包含a字母的书
select name
from books
where name like '%a%';


8、统计书名中包含a字母的书的数量和库存总量
select count(name),sum(num)
from books
where name like '%a%';

9、找出‘novel’类型的书，按照价格降序排列

select name,price
from books
where note='novel'
group by price desc

10、查询图书信息，按照库存量降序排列，如果库存量相同的按照note升序排列



11、当查询的 某个字段为空的时候，比如查询员工表中除了email不等于 123@abc.com
 select * from employess where email<>'123@abc.com' or email is  NULL ---相当于把不等于 和 为空的都查出来了； 为什么是or呢？ 因为and，就之查出为null；



