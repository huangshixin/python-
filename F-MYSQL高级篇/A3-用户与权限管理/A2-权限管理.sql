查看权限

show privileges;

查看权限
SHOW GRANTS;
# 或
SHOW GRANTS FOR CURRENT_USER;
# 或
SHOW GRANTS FOR CURRENT_USER();




授权原则
1、只能授予满足需要的最小权限、
2、限制用户登录主机、
3、满足一定复杂度的密码
4、定期清理不需要的用户，回收权限或删除用户；


【案例】
给与权限  grant select|update|select  on 数据库.* |数据库.表名 to '用户名'@'%';

grant select,update on dbtest1.* to 'zs'@'localhost';

[上面这个语句需要在root用户下实现，因为超管权限]，权限的赋予是一个并集；



【赋予全部权限】
grant  all privileges on '.*' to 'li4'@'localhost';

--->  root和li4的权限的区别，li4权限很大，但是它不能给别人赋予权限的能力；---除非加上


【回收权限】

revoke

revoke 权限1，权限2 .。。 oN 数据库名称.表名称 from 用户名@用户地址；

revoke all privileges ON '.*' FROM 'LI4'@'%';

REVOKE SELECT,INSERT,UPDATE ,DELETE ON mysql.* from joe@localhost;

【注意】
须用户重新登录后才能生效



【总结】

1、不建议使用root超级用户来访问数据库，完全把控制权限

host ： 表示连接类型
    % 表示所有远程通过 TCP方式的连接
    IP 地址 如 (192.168.1.2、127.0.0.1) 通过制定ip地址进行的TCP方式的连接
    机器名 通过制定网络中的机器名进行的TCP方式的连接
    ::1 IPv6的本地ip地址，等同于IPv4的 127.0.0.1
    localhost 本地方式通过命令行方式的连接 ，比如mysql -u xxx -p xxx 方式的连接。
user ： 表示用户名，同一用户通过不同方式链接的权限是不一样的。
password ： 密码
      所有密码串通过 password(明文字符串) 生成的密文字符串。MySQL 8.0 在用户管理方面增加了
      角色管理，默认的密码加密方式也做了调整，由之前的 SHA1 改为了 SHA2 ，不可逆 。同时
      加上 MySQL 5.7 的禁用用户和用户过期的功能，MySQL 在用户管理方面的功能和安全性都较之
      前版本大大的增强了。
      mysql 5.7 及之后版本的密码保存到 authentication_string 字段中不再使用password 字
      段。




3.2 db表
使用DESCRIBE查看db表的基本结构：
1. 用户列 db表用户列有3个字段，分别是Host、User、Db。这3个字段分别表示主机名、用户名和数据库
名。表示从某个主机连接某个用户对某个数据库的操作权限，这3个字段的组合构成了db表的主键。
2. 权限列
Create_routine_priv和Alter_routine_priv这两个字段决定用户是否具有创建和修改存储过程的权限。
3.3 tables_priv表和columns_priv表
tables_priv表用来 对表设置操作权限 ，columns_priv表用来对表的 某一列设置权限 。tables_priv表和
columns_priv表的结构分别如图：
tables_priv表有8个字段，分别是Host、Db、User、Table_name、Grantor、Timestamp、Table_priv和
Column_priv，各个字段说明如下：
Host 、 Db 、 User 和 Table_name 四个字段分别表示主机名、数据库名、用户名和表名。
Grantor表示修改该记录的用户。
Timestamp表示修改该记录的时间。
Table_priv 表示对象的操作权限。包括Select、Insert、Update、Delete、Create、Drop、Grant、
References、Index和Alter。
Column_priv字段表示对表中的列的操作权限，包括Select、Insert、Update和References。
3.4 procs_priv表
procs_priv表可以对 存储过程和存储函数设置操作权限 ，表结构如图：
DESCRIBE mysql.db;
desc mysql.tables_priv;
desc mysql.columns_priv;
desc mysql.procs_priv;



