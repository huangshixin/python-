MYSQL 5.7  不支持check   但是MYSQL8.0支持


          【使用check字段】
          create table test10(
          id int,
          last_name varchar(15),
          salary decimal(10,2) check(salary>2000),#检测以下，某些值不能低于多少；
          sex  char check('男' or '女')
          );

![image](https://user-images.githubusercontent.com/38878365/194734373-7fdf27e5-327b-4f87-b76b-d6f3526f9a7a.png)







