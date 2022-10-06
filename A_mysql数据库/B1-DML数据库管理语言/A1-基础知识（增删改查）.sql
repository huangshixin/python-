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






