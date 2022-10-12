1.会话用户变量   vs    2.局部变量

系统变量的指定是使用@@，用户变量使用的是@


1.1 会话用户变量 【这是自定义的】
    
    会话用户变量：使用“@”开头，作用域为当前的会话 [全局和局部变量的修饰词是@@]
    局部用户变量：只在 BEGIN 和 END 语句块中有效，只在【存储结构】的局部结构中
    
    会话用户的定义：
    #方式1：“=”或“:=”
    SET @用户变量 = 值;
    SET @用户变量 := 值;【建议使用这个】
    
    
    #方式2：“:=” 或 INTO关键字
    SELECT @用户变量 := 表达式 [FROM 等子句];
    SELECT 表达式 INTO @用户变量 [FROM 等子句];
    
        1.定义变量
        举例：
        2.变量赋值
        方式1：一般用于赋简单的值
        方式2：一般用于赋表中的字段值
        3.使用变量（查看、比较、运算等）
        SET @a = 1;
        SELECT @a;
        SELECT @num := COUNT(*) FROM employees;
        SELECT @num;
        SELECT AVG(salary) INTO @avgsalary FROM employees;
        SELECT @avgsalary;
        SELECT @big; #查看某个未声明的变量时，将得到NULL

1.2.3 局部变量
        
        【定义：可以使用 DECLARE 语句定义一个局部变量】
        作用域：仅仅在定义它的 BEGIN ... END 中有效 【只能使用在存储结构中】
        位置：只能放在 BEGIN ... END 中，而且只能放在第一句
        1.2.3 局部变量

        BEGIN
        #声明局部变量
        DECLARE 变量名1 变量数据类型 [DEFAULT 变量默认值];
        DECLARE 变量名2,变量名3,... 变量数据类型 [DEFAULT 变量默认值];
        #为局部变量赋值
        SET 变量名1 = 值;
        SELECT 值 INTO 变量名2 [FROM 子句];
        #查看局部变量的值
        SELECT 变量1,变量2,变量3;
        END     

1、定义变量： DECLARE 变量名 类型 [default 值]; # 如果没有DEFAULT子句，初始值为NULL
        declare variable_name int default 100;

2、变量赋值：
    set 变量名=value;  实际上和会话用户的赋值是一致的，只是没有使用@
    CREATE PROCEDURE set_value()
    BEGIN
    DECLARE emp_name VARCHAR(25);
    DECLARE sal DOUBLE(10,2);
    SELECT last_name,salary INTO emp_name,sal
    FROM employees
    WHERE employee_id = 102;
    SELECT emp_name,sal;
    END //
    DELIMITER ;



案例：
1、使用用户变量

set @x1 =1;
set @x2 =3;
set @sum = @x1+@x2;

2、使用局部变量
delimiter//

create procedure add_value()【存储过程】
begin
    #局部变量
    declare m int default 1;【使用declare关键字定义局部变量  declare 变量 数据类型 default 值】
    declare n int default 1;
    declare sum int ;
    
    set sum = m+n;【设置最后的那个局部变量】
    select sum;

end //


举例3：创建存储过程“different_salary”查询某员工和他领导的薪资差距，并用IN参数emp_id接收员工
id，用OUT参数dif_salary输出薪资差距结果。
#声明
DELIMITER //
CREATE PROCEDURE different_salary(IN emp_id INT,OUT dif_salary DOUBLE)
BEGIN
#声明局部变量
DECLARE emp_sal,mgr_sal DOUBLE DEFAULT 0.0;
DECLARE mgr_id INT;
SELECT salary INTO emp_sal FROM employees WHERE employee_id = emp_id;
SELECT manager_id INTO mgr_id FROM employees WHERE employee_id = emp_id;
END //
DELIMITER ;
#调用
SET @emp_id = 102;
CALL different_salary(@emp_id,@diff_sal);
#查看
SELECT @diff_sal;




