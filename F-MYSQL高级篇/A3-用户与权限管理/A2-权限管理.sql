查看权限

show privileges;

查看权限
show grants


授权原则
1、只能授予满足需要的最小权限、2限制用户登录主机、
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



【总结】

1、不建议使用root超级用户来访问数据库，完全把控制权限








