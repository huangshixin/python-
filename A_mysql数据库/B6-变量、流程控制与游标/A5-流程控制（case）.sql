#情况一：类似于switch
CASE 表达式
WHEN 值1 THEN 结果1或语句1(如果是语句，需要加分号)
WHEN 值2 THEN 结果2或语句2(如果是语句，需要加分号)
...
ELSE 结果n或语句n(如果是语句，需要加分号)
END [case]（如果是放在begin end中需要加上case，如果放在select后面不需要）


【举例子1】
CASE val
WHEN 1 THEN SELECT 'val is 1';
WHEN 2 THEN SELECT 'val is 2';
ELSE SELECT 'val is not 1 or 2';
END CASE;



#情况二：类似于多重if
CASE
WHEN 条件1 THEN 结果1或语句1(如果是语句，需要加分号)
WHEN 条件2 THEN 结果2或语句2(如果是语句，需要加分号)
...
ELSE 结果n或语句n(如果是语句，需要加分号)
END [case]（如果是放在begin end中需要加上case，如果放在select后面不需要）

【举例子2】
CASE
WHEN val IS NULL THEN SELECT 'val is null';
WHEN val < 0 THEN SELECT 'val is less than 0';
WHEN val > 0 THEN SELECT 'val is greater than 0';
ELSE SELECT 'val is 0';
END CASE;

【方法1和方法2的区别是什么？】
在一当中，相当于case接收的是值，然后when当作按照值，进行分支执行
在二当中，case不接收任何东西，然后在when中进行判断；



【做题】 【要求是case when】

#创建存储过程

#创建存储过程

DELIMITER //
CREATE PROCEDURE update_salary(IN emp_id INT) #这个是传入的，只需要定义
BEGIN

-- 			声明存储过程update_salary，定义in参数emp_id
-- 			,输入员工编号；
-- 			1、判断该员工薪资如果低于9k，就更新薪资为9k，大于等于9k且低于10000的，但是奖金比例为null的，就更新奖金比例为0，01；其它的涨薪100；
			#声明局部变量
			DECLARE emp_sal DOUBLE;
			DECLARE bonus double;
			
			#给局部变量赋值
			select  salary into emp_sal FROM employees where employee_id=emp_id;
			select commission_pct into  bonus from employees  where employee_id=emp_id;
			
-- 			#判断
-- 			if emp_sal<9000
-- 					THEN UPDATE employees set salary =9000 where employee_id=emp_id;
-- 			ELSEIF bonus=0.01 and emp_sal BETWEEN 9000 AND 10000
-- 						THEN UPDATE employees set commission_pct=0.01 WHERE employee_id=emp_id;
-- 			else
-- 					update employees set salary=salary+100 WHERE employee_id=emp_id;
-- 			END IF;
			CASE
				when emp_sal<9000 THEN UPDATE employees set salary =9000 where employee_id=emp_id;
				WHEN bonus=0.01 and emp_sal BETWEEN 9000 AND 10000 THEN UPDATE employees set commission_pct=0.01 WHERE employee_id=emp_id;
				else update employees set salary=salary+100 WHERE employee_id=emp_id;
				END CASE;
END //
DELIMITER ;

【删除存储结构】
drop PROCEDURE update_salary;
【查看存储结构】
【show PROCEDURE STATUS】 like '%update%';---使用模糊查询
【引用存储结构】
call 存储结构名

SELECT * from
 employees where employee_id=140;#原始工资2500
 
 
 SELECT * from
 employees where employee_id=109;#原始工资9000  通过存储结构后变成了9100
 
 
 【分析】
 CALL update_salary();【×】这里要求传入一个id

 CALL update_salary(109);【✔】


