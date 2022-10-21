1、sql语句中,即使聚合函数起了一个别名，这个别名也不能用在where里面；

正确的顺序是：where......group by ......having......order by ;
如果是对group by聚合后的结果做筛选，需要用having，where是在聚合前做筛选；

2、可以，按照一下方式进行改变

SELECT mark FROM (

SELECT mark,COUNT(mark) AS num

FROM grade

GROUP BY mark

) AS STATISTIC

WHERE num>1


