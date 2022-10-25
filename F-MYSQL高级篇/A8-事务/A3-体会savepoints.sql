#体会savepoint

create table user3

begin;
update user3 set balance =balance -100 where name = '张三';

update user3 set balance =balance -100 where name = '张三';

savepoint s1;


事务的【隔离级别】:

MYSQL是一个客户端/服务器架构的控件；




数据并发问题：

1、脏写 dirty write

对于两个事务session A，session B，如果事务A修改了另一个未提交的B修改过的数据，意味着发生了脏写；



