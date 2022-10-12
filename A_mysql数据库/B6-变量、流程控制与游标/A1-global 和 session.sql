1.变量由系统定义，不是用户定义，属于 [服务器 ]层面。

【展示 show】  【查询 select】  【赋值  set】

优点：【可以使用变量来存储计算的中间结果，或者输出最终的结果数据】

2.启动MySQL服务，生成MySQL服务实例期间，MySQL将为MySQL服务器内存中的系统变量赋值，
这些系统变量定义了当前MySQL服务实例的属性、特征。这些系统变量的值要么是 编译MySQL时参数
的默认值，要么是 配置文件 （例如my.ini等）中的参数值。



1.1 系统变量 （全局系统变量、会话系统变量） 和 用户自定义的变量
变量可以划分为 1、系统变量  2、用户自定义变量 
    （1）系统变量属于服务器层级，因此只能由系统进行定义
    （2）用户自定义变量，可以用户自定义



1.2 查看系统变量  【关键字 show --- variables】

#查看所有全局变量
SHOW GLOBAL VARIABLES;
#查看所有会话变量 【session这里可以不加----建议默认加上】
SHOW SESSION VARIABLES;
或
SHOW VARIABLES;

###########################################################################################

#查询【部分】系统变量---[查询语句一样]

语法： show global/session variables like

SHOW GLOBAL VARIABLES LIKE "admin_%";

SHOW session VARIABLES LIKE 'CHARACTER_%';



###########################################################################################

1.3 #查看【指定的】系统变量  ---【查询关键字  select】
【作为 MySQL 编码规范，MySQL 中的系统变量以 两个“@” 开头，其中“@@global”仅用于标记全局系统变
量，“@@session”仅用于标记会话系统变量。】

--->>>【@@是引用系统变量或者局部变量，单没有标记global or session的时候，系统会先去会话中查，然后再去全局中查】

语法： select @@gobal/session.变量名

【首先会去会话里面查，如果没有再去全局里面查】

SELECT @@global.变量名; #【这里的变量名必须是全局的】
#查看指定的会话变量的值
SELECT @@session.变量名;#【这里的变量名必须是会话的】


select @@max_connection;  


###########################################################################################

1.4 修改系统变量的值
语法：
方式1：修改MySQL 配置文件 ，继而修改MySQL系统变量的值 【永久改变，该方法需要重启MySQL服务】
方式2：在MySQL服务运行期间，使用“set”命令重新设置系统变【只存在本服务中】


方式1：
SET @@global.变量名=变量值; 
【select @@gobal.max_connection;----set @@gobal.max_connection=value;】
【由于采用了@@的形式，相当于改变的是系统中的ini文件】


#方式2：
SET GLOBAL 变量名=变量值; set global max_connection =167;
【只改变本次服务的变量值】


#为某个会话变量赋值
#方式1：
SET @@session.变量名=变量值;
#方式2：
SET SESSION 变量名=变量值;


第一步肯定是查询

show global variables;

#方式1：
set @@global.max_connection=161; 这种修改是永久修改，需要重启服务器
#方式2：
set global max_connection=161;  针对的是当前的服务,但是这个服务结束后就失效了









