【leave】

语法：  LEAVE 标记名

在mysql中 if loop while repeat 的最后都需要 end + 【上述任意一个]

【】

【举例1】：创建存储过程 “leave_begin()”，声明INT类型的IN参数num。给BEGIN...END加标记名，并在
BEGIN...END中使用IF语句判断num参数的值。
如果num<=0，则使用LEAVE语句退出BEGIN...END；
如果num=1，则查询“employees”表的平均薪资；
如果num=2，则查询“employees”表的最低薪资；
如果num>2，则查询“employees”表的最高薪资。

delimiter //
CREATE PROCEDURE leave_begin(IN num INT)
		signal_name:BEGIN #加标记名
		IF num<=0 THEN LEAVE signal_name;
		ELSEIF num=1 
		THEN SELECT AVG(salary) FROM employees;
		ELSEIF num=2 
		THEN SELECT min(salary) FROM employees;
		ELSEIF num>2 
		THEN SELECT max(salary) FROM employees;
		end IF;
			
			#查询
			select num;
END//
delimiter;


【案例2】
当市场环境不好时，公司为了渡过难关，决定暂时降低大家的薪资。声明存储过程“leave_while()”，声明
OUT参数num，输出循环次数，存储过程中使用WHILE循环给大家降低薪资为原来薪资的90%，直到全公
司的平均薪资小于等于10000，并统计循环次数。

DELIMITER //
CREATE PROCEDURE leave_begin(OUT num INT)
		BEGIN
		DECLARE SAL DOUBLE;
		DECLARE COUNTS INT DEFAULT 0;
		SELECT AVG(salary) INTO SAL FROM employees;
		
		
		WHILE SAL>=10000 DO
				UPDATE employees SET salary=salary*0.9;
				SET COUNTS=COUNTS+1;
				SELECT AVG(salary) INTO SAL FROM employees;
		END WHILE;
		
		set num = COUNTS;
		END//		
DELIMITER ;



【iterate】
3.7 跳转语句之ITERATE语句
ITERATE语句：只能用在循环语句（LOOP、REPEAT和WHILE语句）内，表示重新开始循环，将执行顺序
转到语句段开头处。如果你有面向过程的编程语言的使用经验，你可以把 ITERATE 理解为 continue，意
思为“再次循环”。


举例： 定义局部变量num，初始值为0。循环结构中执行num + 1操作。
如果num < 10，则继续执行循环；
如果num > 15，则退出循环结构；
        DECLARE while_count INT DEFAULT 0; #记录循环次数
        SELECT AVG(salary) INTO avg_sal FROM employees; #① 初始化条件
        while_label:WHILE TRUE DO #② 循环条件
        #③ 循环体
        IF avg_sal <= 10000 THEN
        LEAVE while_label;
        END IF;
        UPDATE employees SET salary = salary * 0.9;
        SET while_count = while_count + 1;
        #④ 迭代条件
        SELECT AVG(salary) INTO avg_sal FROM employees;
        END WHILE;
        #赋值
        SET num = while_count;
        END //
        DELIMITER ;
        ITERATE label
        DELIMITER //
        CREATE PROCEDURE test_iterate()
        BEGIN
        DECLARE num INT DEFAULT 0;
        my_loop:LOOP
        SET num = num + 1;
        IF num < 10
        THEN ITERATE 




