nysql 支持四种隔离级别

mysql> show variables like 'transaction_isolation'; #查看
+-----------------------+-----------------+
| Variable_name         | Value           |
+-----------------------+-----------------+
| transaction_isolation | REPEATABLE-READ |
+-----------------------+-----------------+
1 row in set (0.04 sec)


如何设置隔离级别：
【语法】
SET [GLOBAL|SESSION] TRANSACTION ISOLATION LEVEL 隔离级别;
其中隔离级别格式为：
READ UNCOMMITED
READ COMMITED
REPEATABLE REAP
SERIALIZABLE

mysql> show variables like 'transaction_isolation';
+-----------------------+-----------------+
| Variable_name         | Value           |
+-----------------------+-----------------+
| transaction_isolation | REPEATABLE-READ |
+-----------------------+-----------------+
1 row in set (0.04 sec)

mysql> SET SESSION TRANSACTION ISOLATION  LEVEL READ UNCOMMITTED;
Query OK, 0 rows affected (0.00 sec)

mysql> show variables like 'transaction_isolation';
+-----------------------+------------------+
| Variable_name         | Value            |
+-----------------------+------------------+
| transaction_isolation | READ-UNCOMMITTED |
+-----------------------+------------------+
1 row in set (0.00 sec)

mysql> SET SESSION TRANSACTION ISOLATION  LEVEL REPEATABLE READ;
Query OK, 0 rows affected (0.00 sec)



mysql> SELECT @@TRANSACTION_ISOLATION;
+-------------------------+
| @@TRANSACTION_ISOLATION |
+-------------------------+
| REPEATABLE-READ         |
+-------------------------+
1 row in set (0.00 sec)




【读未提交隔离性下的演示】
create TABLE account(
id INT PRIMARY KEY AUTO_INCREMENT,
NAME VARCHAR(15),
balance DECIMAL(10,2));


insert into account(NAME,balance)  values ('张三',1000), ('李四',1000);



【会话1：】
mysql> select * from account;
+----+--------+---------+
| id | NAME   | balance |
+----+--------+---------+
|  1 | 张三   |  100.00 |
|  2 | 李四   |    0.00 |
+----+--------+---------+
2 rows in set (0.00 sec)

mysql> #开启事务
mysql> begin;
Query OK, 0 rows affected (0.00 sec)

mysql> update account set balance=balance+100 where id=1;
Query OK, 1 row affected (0.00 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> #该事务还未提交;




会话2：

mysql> select @@transaction_isolation;
+-------------------------+
| @@transaction_isolation |
+-------------------------+
| READ-UNCOMMITTED        |
+-------------------------+
1 row in set (0.00 sec)

mysql> select * from account;
+----+--------+---------+
| id | NAME   | balance |
+----+--------+---------+
|  1 | 张三   |  100.00 |
|  2 | 李四   |    0.00 |
+----+--------+---------+
2 rows in set (0.00 sec)

mysql> select * from account;
+----+--------+---------+
| id | NAME   | balance |
+----+--------+---------+
|  1 | 张三   |  200.00 |
|  2 | 李四   |    0.00 |
+----+--------+---------+
2 rows in set (0.00 sec)

mysql> #事务还没提交 ，但是读到了脏数据；





【读已提交和可重复读隔离性下的演示】





【幻读的演示和解决方案】




























































