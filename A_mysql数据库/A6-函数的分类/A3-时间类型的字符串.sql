[1]
CURDATE() ，CURRENT_DATE() 返回当前日期，只包含年、月、日 ,now()  【常用 curdate、now】
CURTIME() ， CURRENT_TIME() 返回当前时间，只包含时、分、秒

    SELECT CURDATE() 'time1',CURRENT_DATE() as 'time2',CURTIME() 'time3', CURRENT_TIME() as 'time4';


[2]
NOW() / SYSDATE() / CURRENT_TIMESTAMP() / LOCALTIME() /LOCALTIMESTAMP()返回当前系统日期和时间
UTC_DATE()返回UTC（世界标准时间）日期
UTC_TIME()返回UTC（世界标准时间）时间
    SELECT NOW(),SYSDATE(),CURRENT_TIMESTAMP(),LOCALTIME(),LOCALTIMESTAMP(); #展示分时秒
    
    
[3]日期与时间戳的转换
UNIX_TIMESTAMP() unix时间戳  Unix 时间戳（英文为 Unix epoch, Unix time, POSIX time 或 Unix timestamp）. UNIX时间 戳的 0 按照 ISO 8601 规范为 ：1970-01-01T00:00:00Z. 一个小时表示为UNIX时间戳格式为：3600秒；
UNIX_TIMESTAMP(date) 将时间date以UNIX时间戳的形式返回
FROM_UNIXTIME(timestamp) 将UNIX时间戳的时间转换为普通格式的时间
        
        SELECT UNIX_TIMESTAMP(now());
        SELECT UNIX_TIMESTAMP(CURDATE());//显示分时秒
        SELECT UNIX_TIMESTAMP(CURTIME());
        SELECT UNIX_TIMESTAMP('2011-11-11 11:11:11')



[4]如何获取月份、星期、星期数、天数等函数


SELECT YEAR(NOW()),MONTH(NOW()),DAY(NOW()); 年月日
SELECT HOUR(CURRENT_TIME()),MINUTE(NOW()),SECOND(CURRENT_TIME());时分秒

MONTHNAME(date) 返回月份：January，...
DAYNAME(date) 返回星期几：MONDAY，TUESDAY.....SUNDAY
WEEKDAY(date) 返回周几，注意，周1是0，周2是1，。。。周日是6
QUARTER(date) 返回日期对应的季度，范围为1～4
WEEK(date) ， WEEKOFYEAR(date) 返回一年中的第几周
DAYOFYEAR(date) 返回日期是一年中的第几天
DAYOFMONTH(date) 返回日期位于所在月份的第几天
DAYOFWEEK(date)返回周几，注意：周日是1，周一是2，。。。周六是7




EXTRACT(type FROM date) 返回指定日期中特定的部分，type指定返回的值

[type的类型]
MICROSECOND(expr)
SECOND
MINUTE
HOUR
DAY
WEEK
MONTH
QUARTER
YEAR
SECOND_MICROSECOND
MINUTE_MICROSECOND
HOUR_MICROSECOND
HOUR_SECOND
HOUR_MINUTE
DAY_MICROSECOND
DAY_MINUTE
DAY_HOUR
DAY_SECOND
YEAR_MONTH



【5】时间和秒钟转换的函数
TIME_TO_SEC(time)将 time 转化为秒并返回结果值。转化的公式为： 小时*3600+分钟*60+秒
SEC_TO_TIME(seconds) 将 seconds 描述转化为包含小时、分钟和秒的时间



【6】计算日期和时间的函数
DATE_ADD(datetime, INTERVAL expr type)，
ADDDATE(date,INTERVAL expr type)
返回与给定日期时间相差INTERVAL时
间段的日期时间


DATE_SUB(date,INTERVAL expr type)，
SUBDATE(date,INTERVAL expr type)
返回与date相差INTERVAL时间间隔的
日期

type：

hour
minute
second
year
month
day
year_month
day_hour
day_minute
day_second
hour_minute
hour_second
minute_second


ADDTIME(time1,time2)返回time1加上time2的时间。当time2为一个数字时，代表的是秒 ，可以为负数

SUBTIME(time1,time2)返回time1减去time2后的时间。当time2为一个数字时，代表的是 秒 ，可以为负数

DATEDIFF(date1,date2) 返回date1 - date2的日期间隔天数

TIMEDIFF(time1, time2) 返回time1 - time2的时间间隔

FROM_DAYS(N) 返回从0000年1月1日起，N天以后的日期

TO_DAYS(date) 返回日期date距离0000年1月1日的天数

LAST_DAY(date) 返回date所在月份的最后一天的日期

MAKEDATE(year,n) 针对给定年份与所在年份中的天数返回一个日期

MAKETIME(hour,minute,second) 将给定的小时、分钟和秒组合成时间并返回

PERIOD_ADD(time,n) 返回time加上n后的时间



【4.7】日期的格式化与解析
DATE_FORMAT(date,fmt) 按照字符串fmt格式化日期date值
TIME_FORMAT(time,fmt) 按照字符串fmt格式化时间time值
GET_FORMAT(date_type,format_type) 返回日期字符串的显示格式
STR_TO_DATE(str, fmt) 按照字符串fmt对str进行解析，解析为一个日期


【fmt】的格式
%Y 4位数字表示年份    %y 表示两位数字表示年份
%M 月名表示月份（January,....） %m两位数字表示月份（01,02,03。。。）
%b 缩写的月名（Jan.，Feb.，....） %c 数字表示月份（1,2,3,...）
%D英文后缀表示月中的天数（1st,2nd,3rd,...）
%d 两位数字表示月中的天数(01,02...)
%e数字形式表示月中的天数（1,2,3,4,5.....）
%H两位数字表示小数，24小时制（01,02..）
%h和%I两位数字表示小时，12小时制（01,02..）
%k 数字形式的小时，24小时制(1,2,3) %l数字形式表示小时，12小时制（1,2,3,4....）
%i 两位数字表示分钟（00,01,02）
%S和%s两位数字表示秒(00,01,02...)
%W 一周中的星期名称（Sunday...） %a一周中的星期缩写（Sun.，Mon.,Tues.，..）
%w以数字表示周中的天数(0=Sunday,1=Monday....)
%j 以3位数字表示年中的天数(001,002...) %U以数字表示年中的第几周，（1,2,3。。）其中Sunday为周中第一天
%u以数字表示年中的第几周，（1,2,3。。）其中Monday为周中第一天
%T 24小时制 %r 12小时制
%p AM或PM %% 表示%

fmt = '%M%D%Y'这个格式

1、select STR_TO_DATE('09/01/2009','%m/%d/%Y');
2、 STR_TO_DATE('20140422154706','%Y%m%d%H%i%s')
3、select date_format(CURRENT_TIME(),'%d%m%Y'); 这个fmt的格式会影响最后的输出；
SELECT STR_TO_DATE('09/01/2009','%m/%d/%Y')
FROM DUAL;
SELECT STR_TO_DATE('20140422154706','%Y%m%d%H%i%s')
FROM DUAL;
SELECT STR_TO_DATE('2014-04-22 15:47:06','%Y-%m-%d %H:%i:%s') fmt形式
FROM DUAL;













