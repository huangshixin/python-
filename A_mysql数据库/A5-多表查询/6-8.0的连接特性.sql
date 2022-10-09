1、从MYSQL8.0开始不支持使用全连接,全连接的实现方式---需要使用外连接+ 右连接

Mysql(版本8.0.25)不支持full join，执行报错【1064 - You have an error in your SQL syntax; 
check the manual that corresponds to your MySQL server version for the right syntax to use near 'full  join 】
