
事务区别于文件系统的额重要特征之一，InnoDB支持事务：


什么是事务： 一组操作单元，使得数据从一组数据转换到另一个状态；

事务的原则： 保证所有事务都作为一个【工作单元】来执行，即使出了故障，都不能改变这种执行方式；
      【在一个事务中执行多个操作时，要么所有的事务都被提交，那么修改就永久保存，要么都不执行，事务回滚】
      
      
【案例】 AA用户给BB转账100,因此存在两个update，AA减少100，BB增加100；      
      
事务的四个特性：
    
    
    
【原子性】

事务作为一个不可分割单位，要么全部提交，要么回滚失败


【一致性】
在事务执行的前后，数据从一个【合法性状态】转变为另一个合法性的状态；
什么是合法状态呢？

一个事务在设定过程中“语义”（不是语法）上的合法性；


【隔离性】
一个事务的执行，不能被【其它事务干扰】，事务之间相互并发；


【持久性】
当事务执行成功后 ，数据的改变时【永久的】












