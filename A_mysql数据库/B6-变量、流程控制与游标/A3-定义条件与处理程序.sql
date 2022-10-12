案例分析： 创建一个存储结构 UpdateDataNoCondition
DELIMITER //
CREATE PROCEDURE UpdateDataNoCondition()
  BEGIN
      SET @x = 1;先设置变量1，然后执行更新语句 但是在创建表的初期，定义的email不能为null；于是存储结构第一条将报错；
      UPDATE employees SET email = NULL WHERE last_name = 'Abel';
      SET @x = 2;
      UPDATE employees SET email = 'aabbel' WHERE last_name = 'Abel';
      SET @x = 3;
  END //
DELIMITER ;


#调用存储结构
CALL 关键字
call 存储结构名字();
CALL UpdateDataNoCondition();

select @x;




[语法：]

DECLARE 错误名称 CONDITION FOR 错误码（或错误条件） //这个需要放在存储结构中

【案例分析】
定义“Field_Not_Be_NULL”错误名与MySQL中违反非空约束的错误类型是“ERROR 1048 (23000)”对
应。


#使用mysql错误码
DECLARE Field_Not_Be_NULL CONDITION FOR 1048 ;#1048表示错误码
#使用sqlstate
DECLARE Field_Not_Be_NULL CONDITION FOR SQLSTATE '23000';




【处理程序】

【语法】
declare 处理方式【continue\exit\undo】 HANDLER FOR 错误类型【SQLSTATE '字符串错误码' /    mysql_error_code】 【处理语句】

【案例分析：】
#方法1：捕获sqlstate_value
DECLARE CONTINUE HANDLER FOR SQLSTATE '42S02' SET @info = 'NO_SUCH_TABLE';

#方法2：捕获mysql_error_value
DECLARE CONTINUE HANDLER FOR 1146 SET @info = 'NO_SUCH_TABLE';

#方法3：先定义条件，再调用
DECLARE no_such_table CONDITION FOR 1146;
DECLARE CONTINUE HANDLER FOR NO_SUCH_TABLE SET @info = 'NO_SUCH_TABLE';

#方法4：使用SQLWARNING
DECLARE EXIT HANDLER FOR SQLWARNING SET @info = 'ERROR';

#方法5：使用NOT FOUND
DECLARE EXIT HANDLER FOR NOT FOUND SET @info = 'NO_SUCH_TABLE';

#方法6：使用SQLEXCEPTION
DECLARE EXIT HANDLER FOR SQLEXCEPTION SET @info = 'ERROR';



【对上述存储过程的处理】
【处理的方式】
DELIMITER //
CREATE PROCEDURE UpdateDataNoCondition()
  BEGIN
  
      DECLARE CONTINUE HANDLER FOR '1048' SET @prc_value = -1;
      SET @x = 1;先设置变量1，然后执行更新语句 但是在创建表的初期，定义的email不能为null；于是存储结构第一条将报错；
      UPDATE employees SET email = NULL WHERE last_name = 'Abel';
      SET @x = 2;
      UPDATE employees SET email = 'aabbel' WHERE last_name = 'Abel';
      SET @x = 3;
  END //
DELIMITER ;

CALL UpdateDataNoCondition(); #调用

select @x,@prc_value;#查看


【案例2】

创建一个名称为“InsertDataWithCondition”的存储过程，代码如下。
在存储过程中，定义处理程序，捕获sqlstate_value值，当遇到sqlstate_value值为23000时，执行EXIT操
作，并且将@proc_value的值设置为-1。
调用存储过程：
UPDATE employees SET email = NULL WHERE last_name = 'Abel';
SET @x = 2;
UPDATE employees SET email = 'aabbel' WHERE last_name = 'Abel';
SET @x = 3;
END //
DELIMITER ;
mysql> CALL UpdateDataWithCondition();
Query OK, 0 rows affected (0.01 sec)
mysql> SELECT @x,@proc_value;
+------+-------------+
| @x | @proc_value |
+------+-------------+
| 3 | -1 |
+------+-------------+
1 row in set (0.00 sec)
#准备工作
CREATE TABLE departments
AS
SELECT * FROM atguigudb.`departments`;
ALTER TABLE departments
ADD CONSTRAINT uk_dept_name UNIQUE(department_id);
DELIMITER //
CREATE PROCEDURE InsertDataWithCondition()
BEGIN
DECLARE duplicate_entry CONDITION FOR SQLSTATE '23000' ;
DECLARE EXIT HANDLER FOR duplicate_entry SET @proc_value = -1;
SET @x = 1;
INSERT INTO departments(department_name) VALUES('测试');
SET @x = 2;
INSERT INTO departments(department_name) VALUES('测试');
SET @x = 3;
END //
DELIMITER ;
