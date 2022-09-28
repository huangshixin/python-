函数 用法
ASCII(S) 返回字符串S中的第一个字符的ASCII码值
CHAR_LENGTH(s) 返回字符串s的【字符数】。作用与CHARACTER_LENGTH(s)相同
LENGTH(s) 返回字符串s的字节数，和字符集有关

    SELECT ASCII('abc') as 'ASCII',
    CHAR_LENGTH("hellosadasdasdasd")  as 'zifu',
    LENGTH('hellosadasdasdasd') "我",
    LENGTH('我');

CONCAT(s1,s2,......,sn) 连接s1,s2,......,sn为一个字符串
CONCAT_WS(x,s1,s2,......,sn) 同CONCAT(s1,s2,...)函数，但是每个字符串之间要加上x【】

    SELECT CONCAT('aaa','bbb','dcd') as 'str';
    #实际应用 管理员表的员工id 是管理员自己的，而员工表的管理者id 匹配到了管理员id，管理员管了那些员工
    SELECT CONCAT(e.last_name,'-',mgr.last_name) as 'name'
    FROM employees e JOIN employees mgr
    ON e.manager_id=mgr.employee_id;
    
    SELECT CONCAT_WS('-',e.last_name,mgr.last_name) as 'name' #相当于在拼接str的时候每次使用‘-’进行分割，这个是必须要加入的
    FROM employees e JOIN employees mgr
    ON e.manager_id=mgr.employee_id;


INSERT(str, idx, len,replacestr) 将字符串str从第idx位置开始，len个字符长的子串替换为字符串replacestr
    SELECT INSERT('helloworld',2,3,'aaaaaa') as '--'; #字符串是从角标为1开始的，这句话的意思是从helloworld中的第2个角标开始，数3个数，把这些字符串用aaaaaa替代

REPLACE(str, a, b) 用字符串b替换字符串str中所有出现的字符串a

  【直接使用字符串替换】a,b必须是在str中


【字符串大小写转换】
UPPER(s) 或 UCASE(s) 将字符串s的所有字母转成【大写字母】
LOWER(s) 或LCASE(s) 将字符串s的所有字母转成【小写字母】


【返回左右第n个字符】
LEFT(str,n) 返回字符串str最【左边的n个字符】
RIGHT(str,n) 返回字符串str最【右边的n个字符】


【字符串填充】
LPAD(str, len, pad) 用字符串pad对str最左边进行填充，直到str的长度为len个字符
RPAD(str ,len, pad) 用字符串pad对str最右边进行填充，直到str的长度为len个字符


【删除空格符号】
LTRIM(s) 去掉字符串s左侧的空格
RTRIM(s) 去掉字符串s右侧的空格
TRIM(s) 去掉字符串s开始与结尾的空格

TRIM(s1 FROM s) 去掉字符串s    【开始与结尾的s1】
    SELECT TRIM('oo' FROM 'oddddddddddddddddoo') 'a'; #去掉头尾的oo，但是不满足条件，就不删除
TRIM(LEADING s1 FROM s) 去掉字符串s开始处的s1
TRIM(TRAILING s1 FROM s) 去掉字符串s结尾处的s1




【重复】
REPEAT(str, n) 返回str重复n次的结果

SPACE(n) 返回n个空格

STRCMP(s1,s2) 比较字符串s1,s2的ASCII码值的大小

SUBSTR(s,index,len) 返回从字符串s的index位置其len个字符，作用与SUBSTRING(s,n,len)、
MID(s,n,len)相同
LOCATE(substr,str) 返回字符串substr在字符串str中首次出现的位置，作用于POSITION(substr IN str)、INSTR(str,substr)相同。未找到，返回0
ELT(m,s1,s2,...,sn) 返回指定位置的字符串，如果m=1，则返回s1，如果m=2，则返回s2，如
果m=n，则返回sn

    select SUBSTR('hello',2,2) as 'sd',LOCATE('l','heooool') as 'first_exist'; #一个是字符串的截取，一个是定位 sql是从1开始的

【可以检查s，在多个字符串中第一次出现的位置】
FIELD(s,s1,s2,...,sn) 返回字符串s在字符串列表中第一次出现的位置
    
    
      SELECT FIELD('v',"vasdadasdas","v",'bg',"asdasdad") as 'name';#这里指的是完全匹配，而不是单独一个字符串属于某一个字符串的子串；

函数 用法
FIND_IN_SET(s1,s2) 返回字符串s1在字符串s2中出现的位置。其中，字符串s2是一个以逗号分
隔的字符串

【翻转】
REVERSE(s) 返回s反转后的字符串


NULLIF(value1,value2) 比较两个字符串，如果value1与value2相等，则返回NULL，否则返回
value1    
