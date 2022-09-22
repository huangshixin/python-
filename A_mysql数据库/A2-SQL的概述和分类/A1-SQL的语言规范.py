数据库（Database）是按照数据结构来组织、存储和管理数据的仓库;
【大处着眼、小处着手】

DDL:数据【定义】语言   create 、drop、alter、rename、truncate 【从无到有的创建文件】
  
DML:数据【操作】语言  update、select、insert、delete 【增删改查】
  
DCL:  数据【控制】语言  rollback（回滚）、commit（提交）、savapoint（保存点）、grant、revoke（回收权限）
  
 

规则：

1、sql语句可以是多行，且需要满足缩进要求
2、每句sql语句必须以;作为结尾----------【为什么呢？】当一个sql中存在多个 sql语句 那么系统执行的时候就会出现问题；
3、关键字不能被缩进和 【换行】
4、sql语句中的 括号（包含多种形式的）必须是成对出现；



规范：
1、linux下 ，sql的大小写是敏感的----统一规范，注意大小写；





【注释】

单行注释： #
多行注释： /* 内容 */



【导入数据】
第一种：
soure + sql文件全路径；


第二种：
使用可视化界面导入： navicat为例，选择数据库名字，执行sql脚本





