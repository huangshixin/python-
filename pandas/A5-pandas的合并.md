1、merge和concat的区别在于，合并需要【按照共同的某一列】进行合并
    
![image](https://user-images.githubusercontent.com/38878365/193443183-e269f856-dfb9-444a-9de9-3770f7edd38b.png)
    
![image](https://user-images.githubusercontent.com/38878365/193443194-535cfbb8-a1db-4030-a3b6-fb88b8c5319f.png)
    
![image](https://user-images.githubusercontent.com/38878365/193443205-06b0b6f6-fb0b-4a44-a384-112a59ee0484.png)
    
![image](https://user-images.githubusercontent.com/38878365/193443223-0defda4c-e785-4a5d-997d-f1602573e98d.png)


2、merge  （对应的数据连接到一起） 一对多

![image](https://user-images.githubusercontent.com/38878365/193443304-5a94ffa7-8ef6-47a3-ab24-76a18e120ac5.png)

3、concate 级联 （直接在下方合并，当然默认axis=1）
![image](https://user-images.githubusercontent.com/38878365/193443343-d31b56f1-7ab0-4a8c-a33f-3ca72cca3a97.png)



4、多对一的合并  [前一个表数据比后一个表数据多]
![image](https://user-images.githubusercontent.com/38878365/193443509-b241362c-7247-47c2-a65a-dba1959fbedd.png)


5、多对多：【当两个表格中的字段，有多个是重复的】
        pd.merge(table3,table4)
          【默认机制】
          1、默认把字段相同的列作为合并的一句
          2、如果有多个列的标签相同，则会同时参考多列合并


6、key的规范

      1\使用on=显式指定哪一列为key，当有多个key相同时使用
      2、使用left_on和right_on左右两边的列作为key，当左右两边的key不相等时候使用
      
      pd.merge(table3,table4,on=['手机型号','发货地区'])#多个重复字段
      
      
      【当没有重复的列标签，但是想合并】----如果合并的列名称不同，会自动保留所有的原始值
      可以使用left_on \right_on
      pd.merge(table1,table2,left_on="型号",right_on="手机型号")#两个都在同一个表
      
      
7、内合并、外合并

![image](https://user-images.githubusercontent.com/38878365/193444085-6d1c511d-2329-4878-b05e-6b6d0a8ac469.png)



      
      
  
  




