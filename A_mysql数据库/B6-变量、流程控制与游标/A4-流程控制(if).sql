【语法】
1、if 表达式 then  查询语句
  else 语句
  end if;


-- 		#	情况1
-- 		DECLARE STU_NAME VARCHAR(15);
-- 		IF STU_NAME IS NULL
-- 					THEN SELECT "STU_NAME IS NULL";
-- 		END IF;
		#情况2 二选一
		DECLARE email VARCHAR（25）default 'aaa';#给一个默认值
		IF email IS NULL
				THEN SELECT 'email IS null';
		ELSE
				SELECT 'email is not null';
		END IF;
 
 
 
 
【案例】 if  else
 
DELIMITER //
CREATE PROCEDURE test2()
BEGIN

			DECLARE age int default 20;
			IF age>40
						THEN select 'age over 20';
			ELSE
					SELECT 'age low DEFAULT value';
			END IF;
END //
DELIMITER ;


CALL test2();
  
  
  
 
 
 
  
  
【案例】if  elseif   else 【记住 这里的elseif是连在一起的】

#创建存储过程

DELIMITER //
CREATE PROCEDURE test2()
BEGIN

			DECLARE age int default 20;
			IF age>40
						THEN select 'age over 20';
			elseif age=20 #这里体现的
							THEN select 'age is equals 20';
			ELSE
					SELECT 'age low DEFAULT value';
			END IF;
END //
DELIMITER ;



CALL test2();

##################################################################################

具体案例：

声明存储过程"update_salary_by_email,定义in参数emp_id,输入员工编号。
判断该员工薪资如果低于8k并且入职时间超过5年，就涨薪500元，否则不变；

delimiter//
create procedure update_salary_by_email(in emp_id int) //in参数 （就是在存储结构后面定义 in  参数名）
begin
    #声明局部变量
    declare emp_sal double;
    declare hire_date double;#多久了 不是日期
    #赋值 [select 表中字段 into 局部变量 from 表 wher 条件]
    select salary into emp_sal from employees where employee_id = emp_id;
    select DATEDIFF(CURDAE(),hire_date)/365 into hire_date from employees where  employee_id = emp_id;
  
    #开始做判断
    if hire_date>5 and emp_sal>8000
          then update employees set salary=salary+500 where employee_id=emp_id;
    end if;
end //
delimiter ;



