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
















