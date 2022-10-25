1、事务的完成过程

（1）开启事务
（2）一系列的DML操作
（3）commit使得事务进入提交状态、终止状态（rollback）




显示事务：

1、使用关键字start transaction 或者 begin

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




【哪些情况会隐式提交数据】














