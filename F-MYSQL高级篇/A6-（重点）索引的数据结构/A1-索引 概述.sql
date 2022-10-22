1、为啥使用索引
    
    加快查询速度，提高系统的处理能力；---减少了磁盘的I/O的次数
    索引的本质：
        你可以简单的理解为‘排好序的快速查找数据结构’；
    
2、索引的优缺点：

    （1） 类似大学图书馆书目索引，提高数据检索的效率，降低数据库的IO成本；
    （2）创建唯一索引，可以爆炸数据库表中的每一行数据的【唯一性】
    （3）在实现数据的参考完整性方面，可以加速表和表之间的连接；
    （4） 在使用分组和排序子句进行数据查询时，可以显著，减少查询中分组和排序时间，降低了CPU的消耗；
    
    
3、 缺点

  (1) 创建索引和维护索引要耗费时间，并且随着数据量的增加，所耗费的时间也会增加；
  (2) 索引需要占用【磁盘空间】
  (3) 虽然索引大大提高了查询速度，同时却会降低更新表的速度。当对表中的数据进行增加、删除和修改的时候 ，
  索引也需要维护；
  
  
  
  
  
  
  
  
  
  
【案例分析】

1、数据表中，一页大概16k，默认占20条记录  ，一页的数据是有限的；
2、查询，可能以主键为搜索状态，因此可以使用二分法；
  
  
【索引在搜索引擎中使用】


假如使用InnoDB

索引之前的查找：

select [列名列表] form 表名 where 列名 = xxx;


1|在一个页中查找

可以使用二分法，按照主键进行划分

2|在很多页进行查找

（1）定位所在记录的页【从每一页开始查，判断是否在同一页】---这个时候就需要使用索引；
（2）从所在的页内中查找相应的记录；





  
  
  
  
  
  
  
  
  
  
    
    







