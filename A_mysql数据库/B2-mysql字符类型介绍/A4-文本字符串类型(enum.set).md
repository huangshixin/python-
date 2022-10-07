文本字符串类型

        在MYSQL 中，文本字符串总体 char 、varchar、tinytext 、text、mediumtext、longtext

        enum、set等
![image](https://user-images.githubusercontent.com/38878365/194446504-aa9a7e15-5cf1-43c9-87d2-6e82a2f7f268.png)
        


        char    固定长度   M   0《=M《=255  M个字节
        varchar   可变长度  M  0<=M<=655535    实际长度加1字节
        
【分析】
      char类型一般需要预先定义字符串长度，如果不指定M，则表示实际长度
      
      create table test_char(
      f1 char(5)
      f2 char
      );
      
      假设字符没有达到M，则使用空格填充
      select char_length(c2)
      from employees;
      
      
      [但是你使用varchar]那么需要指定长度
      
      1、如果是固定的信息，且很短；---那么使用char 
      2、十分频繁的去改变column，那么使用varchar
      
![image](https://user-images.githubusercontent.com/38878365/194447325-c206c10f-23be-4909-b9bb-aa1fef5fe2a2.png)
      
 
 
 
【text】

![image](https://user-images.githubusercontent.com/38878365/194447664-e04975bd-22ca-437f-b87d-0882fde97234.png)

   
   
   
   
【enum】类型

      设置字段值时，enum类型允许从成员中取单个值，不能一次性选取多个值；
      
      create table test_enum(
      season ENUM('spring'，'summer','autumn','wine','unknow');#在添加这个字段的时候，只能添加括号内的字段


      insert into test_enum(season)
      values('spring');
      
      #还可以这样添加【按照索引值进行添加】
      insert into test_enum(season)
      values(1),(3);
 
 
【set类型】

      create table test_set(
      s SET('A','B','C')
      );


      INSERT INTO test_set (s) values ('A'),('A,B');

      1、插入重复的set类型成员的时候，mysql会自动删除重复的成员
      2、向set类型的字段插入set成员中不存在的值时，MySQL会抛出错误


![image](https://user-images.githubusercontent.com/38878365/194448676-e5b280a6-0715-4469-9a4f-92d0d4e139d8.png)


      
      

    
