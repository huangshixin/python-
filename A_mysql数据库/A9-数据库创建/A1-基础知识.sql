1、尽量不使用关键字作为表名，否则使用 ' table_name'
2、字段一致性 ，两张表的有关联字段，需要保持一致性
3、数据库常见方法
    【创建表的三种方式】
    （1）【创建表】create database if not exist mytests1;  顺表判断已经存在，不存在则创建
    （2）【创建表】 create database character set 'gbk'创建数据库 给定字符集
    （3）【展示表】show create database mytest2；
    
    
    1.2【管理数据库】
    
    （1）shou database 查数据库
    （2）use mytest2；使用个别数据库
    （3）show tables 查看数据库中保存的表
    
    1.3 修改数据库
    alter database mytest character set 'utf8';
    
    1.4 删除数据库
    drop database if exist mytest1;
    
    drop tables
    
    
    
    
