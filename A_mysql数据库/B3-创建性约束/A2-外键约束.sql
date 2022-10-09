主表 和 从表 ---这是一个对应的关系；

如果想在从表中加入数据，则主表一定要存在相应的字段


外键约束
1、先创建主表
create table dept1(
dept_id int primary key,
dept_name varchar(15)
);


2、创建从表

create table emp1(
emp_id int primary key auto_incerment,
emp_name varhcar(15),
department_name int,
#表级约束

CONSTRAINT fk_emp1_dept_id foreign key (department_id) references dept1(dept_id);
);

【在添加过程中，可能出现以下错误】
1、主表中的dept_id没有唯一性约束，这时候，设定外键的时候会报错；

2、删除、更新的失败；---关联问题


7.3  在alter table的时候添加外键约束

ALTER TABLE emp2
add constraint fk_emp1_dept_id foreign key (department_id) references dept1(dept_id);


#查看表中约束
select * from informationn_schema.table_constraints
where table_name = 'emp2';



【约束的等级】

1、cascade：在父表上update/delete记录时，同步update/delete子表的匹配；
2、set null 在父表上update/delete记录时，将子表上匹配记录的列设为null，但是注意子表的外键
3、No action 如果子表中有匹配的记录，则不允许对父表对应的候选键进行更新或者删除操作


on update 用cascade
在delete 用restrict

#结论：

最好采用cascade进行更新，为了级联更新
删除最好采用restrict，当有关联的时候，就提示删除失败；


删除外键约束

alter table emp1
drop foreign key fk_name;


#手动删除外键约束对应
show index from emp1；---查外键名

alter table emp1
drop index fk_emp1;





【开发场景】


1、两个表存在一对一，一对多的关系，是否需要外键约束【不一定】

2、外键创建是否创建的区别在于是否限制


3、那建和不建外键约束和查询没有关系？【没有】  只和增删改有关系



阿里开发规范

1、不得使用外键和级联

2、外键与级联更新适用于【单机低并发】，不适用于分布式、高并发集群；

级联更新是强阻塞，存在数据库【更新风险】影响数据库的插入速度；













