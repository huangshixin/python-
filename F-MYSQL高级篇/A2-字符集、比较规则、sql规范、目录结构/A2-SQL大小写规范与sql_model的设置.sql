sql_model的参数模式不一致



宽松模式：
：通过设置宽松模式，来保证大多数sql符合标准的sql语法，在迁移的时候，则不需要对sql业务进行较大 的修改


严格模式：
一般统一使用严格模式；


【查看模式】

select @@session.sql_model

select @@global.sql_model



#设置sql_model
set session sql_model =''



