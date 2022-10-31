【实际开发都是在命令行中执行】


[语法]
create role '角色名'@'用户地址'  #用户地址设定角色名的访问权限

【案例】
create role 'manager'@'%';
create role 'boss'@'%';

查看角色需要去mysql库中的user去看；
select user,host from mysql.user;

[赋予权限]
grant select ,update on dbtest1.* to 'manager';

grant all privileges on *.* to 'wang5';



[查看权限]

在root用户下查看用户权限

show grants for '用户'@'用户地址';

+------------------------------------------------------------+
| Grants for admin@%                                         |
+------------------------------------------------------------+
| GRANT USAGE ON *.* TO `admin`@`%`                          |
| GRANT SELECT, UPDATE, DELETE ON `dbtest1`.* TO `admin`@`%` |
+------------------------------------------------------------+
【revoke】

revoke  select on dbtest1.* from 'manager';


[删除权限]
drop role 'admin';



##############################################################################################

以上部分是关于角色的定义和改变；

[默认情况设定了角色，但是没有激活]
因此需要手动激活
角色激活的两种方式：
1、SET DEFAULT ROLE ALL TO '用户名'@'用户地址'; #用户地址 %  ，localhhost
或者ip

2、先查看权限
show variables like 'activate_all_roles_on_login';

set global activate_all_roles_on_login=ON;#这个变量属于全局的

【查看当前的角色】
mysql> select current_role();
+----------------+
| current_role() |
+----------------+
| NONE           |
+----------------+
[角色激活]
set default role 'manger'@'%' all to 'wang5'@'%';





