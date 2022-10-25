1、事务的完成过程

（1）开启事务
（2）一系列的DML操作
（3）commit使得事务进入提交状态、终止状态（rollback）




显示事务：

1、使用关键字start transaction 或者 begin  ，结尾使用commit

start transactin后面可以跟着 read only /read write(默认)/with consistent snapshot

[可以设置事务的保存点  savepoint]---无论是commit还是rollback 都到某一个点，然后再考虑是否执行其它操作



隐式事务：

【关键字】autocommit
#set autocommit = false

show variables like 'autocommit';#默认是on

update account set balance=balance-10 where id =1;#此时是一个独立的事务

update account set balance=balance+10 where id =2;


【如何关闭自动提交】
【方式1】
set autocommit = false

update account set balance=balance-10 where id =1;#此时是一个独立的事务

update account set balance=balance+10 where id =2;

commit;

【方式2】
我们再autocommit为true的情况下，使用start transaction或者begin开启；
那么就不执行




【4、案例分析】

举例1：
set autocommit=True;这是默认的

mysql> use dbtest1;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
mysql> create table user3(NAME varchar(15) primary key);
Query OK, 0 rows affected (0.06 sec)

mysql> select * from user3;
Empty set (0.00 sec)

【这里是一个事务】
mysql> begin;
Query OK, 0 rows affected (0.00 sec)

mysql> insert into user3 values('张三');
Query OK, 1 row affected (0.00 sec)

mysql> commit;
Query OK, 0 rows affected (0.00 sec)

mysql> select * from user3;
+--------+
| NAME   |
+--------+
| 张三   |
+--------+
1 row in set (0.00 sec)



【这里是一个事务】
begin;
insert into user3 values('李四');#此时不会提交数据,要执行commit后；
insert into user3 values('李四');#受主键影响不会添加成功
rollback;


#先执行--以下两句，得到的结果
mysql> begin;
Query OK, 0 rows affected (0.00 sec)

mysql> insert into user3 values('李四');
Query OK, 1 row affected (0.00 sec)

mysql> select * from user3;
+--------+
| NAME   |
+--------+
| 张三   |
| 李四   |
+--------+
2 rows in set (0.00 sec)


#再执行这个插入语句后，使用rollback，回滚到最近的那个commit
mysql> insert into user3 values('李四');
ERROR 1062 (23000): Duplicate entry '李四' for key 'user3.PRIMARY'
mysql> rollback;
Query OK, 0 rows affected (0.00 sec)

mysql> select * from user3;
+--------+
| NAME   |
+--------+
| 张三   |
+--------+
1 row in set (0.00 sec)


【情况2】
1、清空表数据
delet from table_name;
or
truncate table user3;  一个是truncate table  table_name;#DDL操作会自动提交数据


begin;
insert into user3 values('张三');
commit;
                         
insert into user3 values('lisi')#默认的dml情况会默认提交数据
insert into user3 values('lisi');                        
rollback;#这里执行的rollback，不会影响到李四
                         

mysql> select * from user3;
+--------+
| NAME   |
+--------+
| 张三   |
| 李四   |
+--------+



【在情况2的基础上，使用变量】                         
  
select @@completion_type;

set @@completion_type =1;
  
begin;
insert into user3 values('张三');
commit;    

select * from user3;;

insert into user3 values('李四');
insert into user3 values('李四');

rollback;



【效果】

mysql> begin;
Query OK, 0 rows affected (0.00 sec)

mysql> insert into user3 values('张三');
Query OK, 1 row affected (0.01 sec)

mysql> commit;
Query OK, 0 rows affected (0.00 sec)

mysql> select * from user3;;
+--------+
| NAME   |
+--------+
| 张三   |
+--------+
1 row in set (0.00 sec)

ERROR: 
No query specified

mysql> insert into user3 values('李四');
Query OK, 1 row affected (0.00 sec)

mysql> insert into user3 values('李四');
ERROR 1062 (23000): Duplicate entry '李四' for key 'user3.PRIMARY'
mysql> rollback;
Query OK, 0 rows affected (0.01 sec)

mysql> select * from user3;;
+--------+
| NAME   |
+--------+
| 张三   |
+--------+
1 row in set (0.00 sec)

ERROR: 
No query specified



为什么completion_type=1会影响；

它为0是默认情况，当我们执行commit的时候会提交事务，在执行下一个事务的时候用start transaction或者begin来开启

它为1的时候，当事务提价了，相当于执行了commit and chain,也就是链式事务，即当我们提交了事务知乎会开启一个相同隔离级别的事务；

它为2时候；

