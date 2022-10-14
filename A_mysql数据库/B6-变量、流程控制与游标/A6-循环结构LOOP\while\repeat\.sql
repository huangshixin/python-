LOOP循环语句用来重复执行某些语句。LOOP内的语句一直重复执行直到循环被退出（使用LEAVE子
句），跳出循环过程。

【循环结构：四要数】
1、初始化条件
2、循环条件
3、迭代条件
4、结束条件


【举例】
当市场环境变好时，公司为了奖励大家，决定给大家涨工资。声明存储过程
“update_salary_loop()”，声明OUT参数num，输出循环次数。存储过程中实现循环给大家涨薪，薪资涨为
原来的1.1倍。直到全公司的平均薪资达到12000结束。并统计循环次数。


DELIMITER //
    CREATE PROCEDURE update_salary_loop(OUT num INT)#声明OUT参数num
    BEGIN
      DECLARE avg_salary DOUBLE;
      DECLARE loop_count INT DEFAULT 0;
      
      SELECT AVG(salary) INTO avg_salary FROM employees;
      label_loop:LOOP #记录loop循环体
      
          IF avg_salary >= 12000 THEN LEAVE label_loop; #结束循环 leave loop名字
          END IF;

          UPDATE employees SET salary = salary * 1.1;
          SET loop_count = loop_count + 1;
          SELECT AVG(salary) INTO avg_salary FROM employees;
      END LOOP label_loop;结束loop
      SET num = loop_count;
  END //
DELIMITER ;












【while循环】
1、先定义一个存储结构



【语法】
while condition  DO
      执行语句：
      可以是查询
      赋值
      更新
      ...    
END WHILE;



2 delimiter在最外边，之后是 存储结构  紧接着是 begin --end 最后是声明的变量和循环体

delimiter //
create procedure update_sal(OUT NUM INT)

BEGIN
    DECLARE NUM INT DEFAULT 1;
    WHILE NUM<=10 DO
        SET NUM:=NUM+1;
    END WHILE;
    
    #查询
    select num;
END //

delimiter;


【举例子2】
当市场环境不好时候，为了渡过难关，决定暂时降低大家的薪资。

声明存储过程“update_salary_while "声明OUT参数num，输出循环次数；
存储过程中实现循环给大家降薪，薪资为原来的90%，直到全公司的平均薪资达到5000结束，并统计循环次数


DELIMITER //
CREATE PROCEDURE update_salary_while(OUT num INT)#输出num
  BEGIN
      DECLARE COUNT INT DEFAULT 0;
      DECLARE SAL DOUBLE;
      #查询平均工资(第一次查询)
      select avg(salary) into SAL from employees;
      
      while SAL>5000 DO
          #如果平均工资大于5000，那么开始更新所有员工的工资
          UPDATE  employees set salary = salary*0.9 ; #update
          set count=count+1; #开始统计执行的次数
          #紧接着更新平均工资的值
          select avg(salary) into SAL from employees;
      END WHILE;#跳出循环
      
      #打印循环结果
      select COUNT;  #正常的查询语句 [×]---这个会
      set num = count; #把循环的结果赋值给num，系统会输出
      
  END//

DELIMITER;


【怎么调用呢？  这种带OUT的  】

call update_salary_while(@num);

######################################################################
CREATE PROCEDURE update_salary_while(OUT num INT)#输出num
  BEGIN
      DECLARE COUNT INT DEFAULT 0;
      DECLARE SAL DOUBLE;
      #查询平均工资(第一次查询)
      select avg(salary) into SAL from employees;
      
      while SAL>5000 DO
          #如果平均工资大于5000，那么开始更新所有员工的工资
          UPDATE  employees set salary = salary*0.9 ;
          set count:=count+1; #开始统计执行的次数
          #紧接着更新平均工资的值
          select avg(salary) into SAL from employees;
      END WHILE;#跳出循环
      
      #打印循环结果
      select COUNT;  #正常的查询语句 [×]---这个会
--       set num = count; #把循环的结果赋值给num，系统会输出
--       
  END
> Affected rows: 0
> 时间: 0.01s







【循环结构repeat】

【语法】 [先执行一次，然后再去判断循环条件]
repeat 
    执行结构体()
    set num=num+1;
    until num>10  #[这里是循环条件]，不要加封号
end repeat;



【区别判断】
loop：
while：
repeat









