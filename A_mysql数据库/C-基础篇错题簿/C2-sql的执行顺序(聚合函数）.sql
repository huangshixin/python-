命令顺序为：select, from, where, group by, having, order by, limit


count(1) 和count(*)
count(1) 与 count(*) 比较 :
1> 如果数据表没有主键，那么 count(1) 比 count(*) 快
2> 如果有主键的话，那主键 (联合主键) 作为 count条件也比 count(*) 要快
3> 如果你的表只有一个字段的话那 count(*) 就是最快

聚合函数【除了count外】，都是跳过空值，处理非空值；
count(*)统计的是全部行，当count(列名)时候，统计的是该列的长度；

【案例】 -----只有D,F是一定相等的
表结构如下：
CREATE TABLE `score` (
   `id` int(11) NOT NULL AUTO_INCREMENT,
   `sno` int(11) NOT NULL,
   `cno` tinyint(4) NOT NULL,
   `score` tinyint(4) DEFAULT NULL,
   PRIMARY KEY (`id`)
 ) ;
以下查询语句结果一定相等的是（）
A.SELECT sum(score) / count(*) FROM score WHERE cno = 2;

B.SELECT sum(score) / count(id) FROM score WHERE cno = 2;

C.SELECT sum(score) / count(sno) FROM score WHERE cno = 2;

D.SELECT sum(score) / count(score) FROM score WHERE cno = 2;

E.SELECT sum(score) / count(1) FROM score WHERE cno = 2;

F.SELECT avg(score) FROM score WHERE cno = 2;

