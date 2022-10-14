虽然我们也可以通过筛选条件 WHERE 和 HAVING，或者是限定返回记录的关键字 LIMIT 返回一条记录，
但是，却无法在结果集中像指针一样，向前定位一条记录、向后定位一条记录，或者是 随意定位到某一
条记录 ，并对记录的数据进行处理。



第一步，声明游标
在MySQL中，使用DECLARE关键字来声明游标，其语法的基本形式如下：
这个语法适用于 MySQL，SQL Server，DB2 和 MariaDB。如果是用 Oracle 或者 PostgreSQL，需要写成：
要使用 SELECT 语句来获取数据结果集，而此时还没有开始遍历数据，这里 select_statement 代表的是
SELECT 语句，返回一个用于创建游标的结果集。


DECLARE cursor_name [CURSOR for] select_statement;

在sqlserver 或者orecal中 cursor IS 

eg:
		DECLARE emp_cursor 【CURSOR FOR】关键字 
    SELECT salary from employees ORDER BY salary desc; ---查询语句


第二步，打开游标
打开游标的语法如下：

OPEN cursor_name

当我们定义好游标之后，如果想要使用游标，必须先打开游标。打开游标的时候 SELECT 语句的查询结
果集就会送到游标工作区，为后面游标的 逐条读取 结果集中的记录做准备。




第三步，使用游标（从游标中取得数据）
语法如下：

FETCH cursor_name INTO var_name [, var_name] ...

这句的作用是使用 cursor_name 这个游标来读取当前行，并且将数据保存到 var_name 这个变量中，游
标指针指到下一行。如果游标读取的数据行有多个列名，则在 INTO 关键字后面赋值给多个变量名即可。
注意：var_name必须在声明游标之前就定义好。
注意：游标的查询结果集中的字段数，必须跟 INTO 后面的变量数一致，否则，在存储过程执行的时
候，MySQL 会提示错误。




第四步，关闭游标


close cursor_name; 
有 OPEN 就会有 CLOSE，也就是打开和关闭游标。当我们使用完游标后需要关闭掉该游标。因为游标会
占用系统资源 ，如果不及时关闭，游标会一直保持到存储过程结束，影响系统运行的效率。而关闭游标
的操作，会释放游标占用的系统资源。







-- 创建存储过程“get_count_by_limit_total_salary()”，声明IN参数 limit_total_salary，DOUBLE类型；声明
-- OUT参数total_count，INT类型。函数的功能可以实现累加薪资最高的几个员工的薪资值，直到(until）薪资总和
-- 达到limit_total_salary参数的值，返回累加的人数给total_count。



DELIMITER //
CREATE PROCEDURE get_count_by_linit_total(IN limit_total_salary double,OUT total_count INT)

		BEGIN
		declare sal_count INT DEFAULT 0;#计算累加人数
		declare sal DOUBLE ;
		DECLARE emp_sum double DEFAULT 0.0;
		
		#声明游标
		DECLARE emp_cursor CURSOR FOR SELECT salary from employees ORDER BY salary desc;
		
		#打开游标
		OPEN emp_cursor;
		
		
		repeat
							#使用游标
					FETCH emp_cursor INTO sal;#游标是从上往下 不断的去取数的；取出一个数放在sal中
					SET emp_sum=emp_sum+sal;
					set sal_count=sal_count+1;
					until sal>=limit_total_salary
		end REPEAT;
			
		set total_count =sal_count;		#用于输出
		CLOSE emp_cursor;	
		end //
DELIMITER ;




