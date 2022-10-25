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



2、脏读

事务A准备读取某一个数据，但是事务b对数据进行操作了，这个数据被A读到了，但是b对它进行了回滚；
所以变成了脏读；


3、不可重复读；

事务A读取的时候，每次读取的数据都不一致；---（除去多了东西）


4、幻读---针对了插入数据；

对于两个事务a和b， a从一个表中读取了一个字段，然后事务b在该表中【插入了新数据】






sql中的四种隔离级别：

1、读未提交read unconmited  解决脏读

2、读已提交：解决脏读，解决不可重复读

3、repeatable read 解决幻读、解决脏读，解决不可重复读

4、serializable  只解决 加锁读；




