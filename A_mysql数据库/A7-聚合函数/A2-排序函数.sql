1. rank() over
作用：查出指定条件后的进行排名，条件相同排名相同，排名间断不连续。
说明：例如学生排名，使用这个函数，成绩相同的两名是并列，下一位同学空出所占的名次。即：1 1 3 4 5 5 7

2. dense_rank() over
作用：查出指定条件后的进行排名，条件相同排名相同，排名间断不连续。
说明：和rank() over 的作用相同，区别在于dense_rank() over 排名是密集连续的。例如学生排名，使用这个函数，成绩相同的两名是并列，下一位同学接着下一个名次。即：1 1 2 3 4 5 5 6

3. row_number() over
作用：查出指定条件后的进行排名，条件相同排名也不相同，排名间断不连续。
说明：这个函数不需要考虑是否并列，即使根据条件查询出来的数值相同也会进行连续排序。即：1 2 3 4 5 6

使用小提示
dense_rank() over 后面跟排序的依据的列，下面是用了一个排序好的列(order by score desc)。
注意：如果select中有一列是用rank()这类函数，其他的列都会按着他这列规定好的顺序排。



1、想要使用密集排序就是使用 dense_rank() over(order by  字段)


select score,dense_rank() over(order by score desc) as 'rank'
from Scores;
