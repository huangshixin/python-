1、尽量不使用关键字作为表名，否则使用 ' table_name'
2、字段一致性 ，两张表的有关联字段，需要保持一致性
3、数据库常见方法
    【创建表的三种方式】
    （1）【创建表】create database if not exist mytests1;  顺表判断已经存在，不存在则创建
    （2）【创建表】 create database character set 'gbk'创建数据库 给定字符集
    （3）【展示表】show create database mytest2；
    
    
    1.2【管理数据库】
    
    （1）shou databases 查数据库
    （2）use mytest2；使用个别数据库
    （3）show tables 查看数据库中保存的表
    
    1.3 【修改数据库】
    alter database mytest character set 'utf8';
    
    1.4 【删除数据库】
    drop database if exist mytest1;
    
    drop tables
    
    
    1.5【创建表的方式】
    
    整数 tinyint int
    浮点 double
    定点数类型 decimal
    二进制 binary
    json josn对象和josn数组
    
    方式1：
    create table table_name
    方式2:
    create table if not exist table_name character set 'uft8' #常用这种方式
    
    查看表：show create table table_name;
    
    1.6【创建表中字段----基于现有的表创建新的表】
    create table mytes2
    as
    select employee_id,last,salary
    from employees;【按照employees中的某些字段，去构建新的表，【会保留employees中的数据】】
    
    
    【要表数据】如果进行多表查询后，再按照以上方式创建新的表，那么多表中的字段【别名】会成为新表中的数据 
    【不要有数据】  使用过滤条件，写一个条件，使得条件中的数据 ，原数据不满足
                    or[或者]
                    create table rmploy
                    as
                    select * from employees where 1=2; 1永远不等于2；因此就没有数据
                    
    1.7【修改表】 add
    Alter TABLE myempl
     （1） 添加一个字段到表中 :
     Alter TABLE myempl
     ADD salary double(10,2) #默认添加到表中的最后一个字段
     
     Alter TABLE myempl
     add  phone_number varchar(20) first; 放在第一个
     
     Alter TABLE myempl
     add  email varchar(10) AFTER emp_name;  在某个字段后
     
         
     （2）修改一个字段 [modify]
     Alter TABLE myempl
     MOdify emp_name varchar(15) default 'aaa';
     （3）重命名表中字段
     Alter TABLE myempl
    CHANGE salary monthly_salary double(10,2); 使用change关键字，然后再输入 数据类型和 字段名（不必须）
    （4）删除某一列 【drop column】
      Alter TABLE myempl
    drop column my_emaile;删除某一个字段
    
    
    1.8【重命名表】 change
    方式1： rename table myemp1 TO myemp11;
    方式2： alter myempl2 rename to myemp12
    
    
    1.9【删除表】 不光将表结构删除掉，同时表中的数据也删除掉，释放空间
    drop table if exists myemp12;
    
    
    2.0【清空表】 只清空表数据，但是删除表结构
    truncate table employees_copy;
                    
    
    2.1【commit】一旦提交数据，则数据就被永久的保存在了数据库中，意味着不可回滚；
       【rollback】 ：可能可以回滚数据，一旦执行rollback，则可以实现数据的回滚；--最近的一次
       
       
    2.2 truncate 和 delete from的区别是什么？
    delete from只是删除表中的数据，【数据理论上可以回滚】
    但是truncate是一下子清空表中的所有数据，但是数据不可以回滚
       
    DDL和DML的说明
    1、DDL操作一旦执行，就不可回滚，指令set autcommit =False对DDL操作失效；[因为再DDL操作后，会自动执行一次commit，且不受set autocommit的影响]
    2、DML的操默认情况，也是不可以回滚，因为在mysql中 有一个字段set autocommit = True，默认是true
    ，因此会自动提交数据，需要进行字段修改；【指的是delete from】
    
    【演示步骤】
    commit;
    
    select * from employ_copy;
    
    set autocommit = False;先设置该字段
    
    之后再回滚
    ROLLBACK;
    
  
