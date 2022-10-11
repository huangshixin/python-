1.会话用户变量   vs    2.局部变量

1.1 会话用户变量 【这是自定义的】
    
    会话用户变量：使用“@”开头，作用域为当前的会话 [全局和局部变量的修饰词是@@]
    局部用户变量：只在存储结构的局部结构中
    
    会话用户的定义：
    #方式1：“=”或“:=”
    SET @用户变量 = 值;
    SET @用户变量 := 值;
    
    #方式2：“:=” 或 INTO关键字
    SELECT @用户变量 := 表达式 [FROM 等子句];
    SELECT 表达式 INTO @用户变量 [FROM 等子句];

        1.2.3 局部变量
        
        【定义：可以使用 DECLARE 语句定义一个局部变量】
        作用域：仅仅在定义它的 BEGIN ... END 中有效
        位置：只能放在 BEGIN ... END 中，而且只能放在第一句
        
        
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






