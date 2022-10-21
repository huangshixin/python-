【用户管理】
1、普通用户 和 root用户

【1.1登录mysql服务器】
mysql -h hostname|hostIP -P port -y username -p DataBaeName -e 'SQL';

【mysql -h localhost -P 3306 -y dbtest1 -p password】

-h：主机id
-P 端口号


【1.2.数据库创建完会有几个数据建库】
以mysql为例，查看其user表信息
1.1select host,user from user;

创建用户
1.2create user 'zhang3' identified by 'abc123'; #默认%任何端连接---可以用于远程连接；


查看权限
show grants;

1.3 修改表[DML需要flush privileges]
update table_name 
set user = 'wang5'
where user = 'li4' and host ='%';


之后必须flush privileges;


1.4 删除用户；

drop user 'wang5';



1.5设置当前用户的密码 【8.0不再只是password()】

（1）root用户修改
alter user user() identified by 'abcabc';

（2）其它用户修改


（3)其它用户修改别人的密码



















