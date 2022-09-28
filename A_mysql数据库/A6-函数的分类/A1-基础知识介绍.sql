#单行函数：
-- 	操作数据对象
-- 	接受参数返回一个结果
-- 	只对一行进行变换
-- 	每行返回一个结果
-- 	可以嵌套

ABS(X) 绝对值
SIGN(X) 返回x的符号 正的为1 负的为-1
PI()  圆周率
CEIL(X)、CEILING(X) 返回 大于或者等于某个值的【最小整数】  CEILING(32.32)=33   CEILING(-32.32)=-33 取不大于x的最大整数
FLOOR(X) 返回小于或者等于某个值的【最大整数】  ---地板（天花板，最大值）
LEAST(value1,value2,...) 返回list中最小值
GREATEST(value1,value2,...) 返回list中最大值
MOD(N,M) n除以m的取余
RAND() 返回0-1的随机值
round(x) 返回0-1的随机值其中x的值用作种子值，相同的x值会产生相同的随机数
round(x,y) ，输入x，保留小数点后面y个值    eg:SELECT ROUND(32.34323524,5) FROM DUAL;
TRUNCATE(X,D) 返回数字x截断为y位小数的结果 :SELECT TRUNCATE(32.332,2); 从小数后2位开始都不要
SQRT(X) 求平方根








