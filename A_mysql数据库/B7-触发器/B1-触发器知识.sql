触发器 【当某个时间发生的时候，系统会自动的触发】



1、创建

create trigger 触发器名称
(before/after) {insert/update/delete} on 表名  【在表前或者表后】
for each row
触发器执行的语句块

2.举例实现;
创建触发器：创建名称为before_insert 向test_trigger数据表插入数据前,向test_trigger表中插入日志信息；

delimiter//  #定义的时候表示//是结束的意思
create tirgger tir_name
before insert on  test_trigger
for eacch row
begin
    insert into test_trigger_log(t_log)
    values('before insert ...');
    
end//
delimiter;


3.测试
insert into test_trigger(t_note)
values();



4.举例2：
创建名称为after_insert的触发器，向test_trigger数据表中插入数据后，向test_trigger_log数据表中插入
after_insert的日志信息

delimiter//
create trigger after_insert  
after insert on test_triger
for each row
begin 
  insert into test_trigger_log(t_log)#也可以不署名添加
  values('after_insert_log...')
end//

delimiter;


5.举例三：
定义触发器salary-check_trigger,基于员工表employee的insert事件

delimiter//

create trigger salary_check_trigger
before insert on employees
for each row
begin 
      #查询到数据的manager的薪资
      decalre sal double;
      select salary into sal  from employees where employee_id =NEW.manager_id (使用new这个记录的)
      
      if new.salary>sal
          then SIGNAL SQLSTATE 'HY00' SET MEAASGE_TEXT = '薪资高于领导薪资错误'；//固定格式
      end if;
      
end//
delimiter;



6.查看触发器
（1）show triggers；
（2）show create trigger specific_name;


7.删除触发器

drop trigger if exists 名字;




总结：触发器

advantage：
1、保证数据的完整性 
2、记录操作日志
3、在操作数据前，对数据进行合法性检测


shortage：

1、触发器最大的确定是可读性差；



注意点：





