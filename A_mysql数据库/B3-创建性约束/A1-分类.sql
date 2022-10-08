1、为什么需要约束？

数据完整性：指的是数据的【精确性】、【可靠性】

sql规范以约束的方式对表的数据进行额外的条件限制；

    1、实体完整性： 例如一个表中，不能存在两条相同的记录----靠主键约束
    2、域完整性： not null 等
    3、引用完整性： 员工所在部门，在部门表中----靠外键约束
    4、用户自定义完整性：给定的要求 需要被约束---constraint约束

实体、域、用户自定义、引用（外键）





1.1  基础知识
什么叫约束呢？ 对表中的字段进行强制的约束；

1.2 约束的分类

    约束的字段的个数  ：单列 vs  多列
    
    约束作用的范围：
          【列级约束】：将此约束声明在对应的字段后面
          【表级约束】：在表中所有字段都声明完，在所有字段后面声明约束CONSTRAINT





%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%约束的功能%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
设置一些约束后，对增删改查会有影响

1、not null:设置字段非空，可以对某一个列设置


    1、可以在创建表的时候添加【只有列级约束】
    create table test1(
    id int not null,
    last_name varchar(10) not NULL,
    salary decimal(10,2)
    );
【如果在建表时候没添加约束，可以在修改表时候添加】  使用modify方法  
alter TABLE test1
modify email varchar(10) NOT NULL;  修改表，需要注意，若表中有非空字段，那么这条语句不会执行成功；

  
  
  
    
2、unique：唯一值，但是可以多次添加NULL值

    1、可以单列约束、也可以多列约束
     create table test2(
    id int unique ,
    last_name varchar(10) not NULL,
    email varchar(25) unique,#邮箱约束
    salary decimal(10,2)
    );
    
    create table test2(
    id int unique ,
    last_name varchar(10) not NULL,
    email varchar(25),#邮箱约束
    salary decimal(10,2),
    
    #【表级约束】
    CONSTRAINT uk_test2_email unique(email)  #使用constraint关键字
    );
    
方式1：  字段约束  
ALTER TABLE test2 modify email varchar(10) UNIQUE;

方式2：类似于表约束（添加约束）
ALTER TABLE test2
ADD CONSTRAINT UK_TESTE2 UNIQUE(email);



【延申题】
create table user(
id int,
name varchar(15),
passwaord varcha(25),

#作用在两个列上
CONSTRAINT uk_user  UNIQUE(name,password) #两个合并作为一个唯一性约束
)


##################################################################################



primary key：主键【非空且唯一】/unique可以是空  ，primary key是有值且非空

      用于唯一的标识数据的完整性(实体完整性）

      create table test3(
      id int primary key,
      last_name varchar(10),
      email varchar(15)
      );
      
      
      
      #表级约束
      create table test3(
      id int,
      last_name varchar(10),
      email varchar(15)
      constraint uk_test3 primary key(id)#mysql的主键名总是primary ，即使你自己命名后
      );

      
      
        #表级约束，方式2
      create table test4(
      id int,
      last_name varchar(10),
      email varchar(15)
      primary key(id)#mysql的主键名总是primary ，即使你自己命名后
      );
      
      【复合的主键约束---是不能为空的，】---此外，其它是可以删除的；
      
      实际开发中，是不会去删除主键约束的；


##################################################################################

auto_increament
--一个表中最多只能有一个自增长列
--当需要产生唯一标识符或顺序值时，可以设置自增长
--自增长的约束列必须时【键列】（主键列、唯一键列）
自增约束的数据类型必须时整数类型


      create table test4(
      id int primary key  auto_increment,#每次插入数据的时候，就不需要额外赋值新值
      last_name varchar(10),
      email varchar(15)
      primary key(id)#mysql的主键名总是primary ，即使你自己命名后
      );

【如果你赋值一个新的id的时候，在下次添加数据的时候，会从最大的id数开始auto_increment】

alter table test4
modify id int auto_increment;

【5.7特性】
在自增的时候，如果删除一条记录，再添加字段的时候，会从【未删除前】最大的记录处开始自增；
但是重启服务器后，会从最大的值开始自增（因为这数据写在内存中）
【8.0新特性】
从8.0开始，将上述的特性【持久化】
    
      
##################################################################################

foreign key：外键---引用完整性








##################################################################################


check
default

1.3 如何添加约束？/删除约束？

--添加唯一性约束的列上也会自动创建唯一索引
--删除唯一约束只能通过删除唯一索引的方式删除
--删除时需要指定唯一索引名，唯一索引名和唯一约束名一样
--如果创建唯一约束时未指定名称，如果是单列，就默认和列名相同；


select * from information_schema.table_constraints  where table_name = 'student_course';

#删除唯一性索引
alter table test2
drop INDEX last_name;

alter table test2
drop index uk_test2_sal;#索引名



2、如何查看表中的约束  table_constraints

select * from information_schema.table_constraints  where table_name = 'employees';














