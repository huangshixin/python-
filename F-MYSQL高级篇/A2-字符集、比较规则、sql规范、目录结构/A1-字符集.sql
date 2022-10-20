show variables like '%character%'; #查看数据库默认使用的字符集

1、字符集的修改与底层原理的说明

mysql5.7 在character_set_client \character_set_database\character_set_server ;默认的分别是 utf8mb4\latin\latin

mysql8.0 character_set_client \character_set_database\character_set_server分别是utf8，utf8,utf8


latin字符集是不支持【中文的】，因此需要改字符集---linux下 etc/mysql/my.cnf
[影响最终的创建表，以及比较规则]


2、【实例测试】

create database if not exists dbtest1;

use dbtest1;


create table if not exists emp1(id int,lname varchar(15));

insert into emp1
values(1,'TOM'),(2,'Mr.huang');


show create database dbtest1;//查看字符集
show create table emp1;


3、修改表、或者、数据库的字符集的几种方式；

【改数据库】
1、alter database dbtest1 character set 'utf8';
【改表】
alter table 表名 [convert to] character set 'utf8';



4、【各个级别的字符集】
1、服务器级别 character_set_server决定了 character_set_database


2、数据库级别


3、表级别


4、列级别


5、字符集比较规则【了解】
1、utf8 与 utf8mb4
utf8表示一个字符可以等于1-3个字节
utf8mb4表示一个字符可以等于1-4个字节

后缀表示
_ai  不区分重音
_as区分重音
_ci不区分大小写
_cs区分大小写
_bin 以二进制比较



6、查看字符集比较规则
show collation like '具体字符集';

7、修改具体数据库的字符集
alter database dbtest1 default character set 'utf8' collate 'utf_ge..'





