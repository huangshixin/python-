create table test_json(
js json
【在MySQL8中，json类型提供了可进行字典验证的json文档和优化的存储结构

);



【如何向表中插入json数据】

insert into test_json(js)
values ('{"name":"songhk","age':"18","address":"{"province":"beijing","city":"beijing"}}}')



如何取json中特定位置的字符呢

select js ->'$.name' AS NAME, js -> '$.address' as address
from test_json;




【规则】
 
 json字段 ->'$.json中的key'  AS 别名
