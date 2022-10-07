      1、浮点类型 float   4字节
      2、双精度浮点数  double    8字节


########################################################
      区别：float所占用的字符少，double所占的字节总数大


########################################################
【精度的说明】
        
        M称为精度
        D成为标度
        
        float(5,2)只能显示-999.99~999.99
        
      *****【double能够表达的范围比decimal大，如果精度不需要那么高，就使用浮点型】
【案例】

![image](https://user-images.githubusercontent.com/38878365/194439964-0464a1cb-eb66-4b44-86fd-94d76219dbaf.png)
   
        在float中，如果你是小数位，那么你只能在上述的范围内
        
 ![image](https://user-images.githubusercontent.com/38878365/194440168-3b9b4d05-467d-4199-867e-6195c3622333.png)
        
        double的精度是比float高，且在比较浮点类型的时候尽可能不要使用“=”
        
  
  
  
  
  
【定点数】
      decimal （M.D）  M+2字节
      它在数据的底层是使用【字符串进行存储】
      【你需要使用的精度要高，则使用它】
【案例】
        create table test_decimal(
        f1 decimal,
        f2 decimal(5,2)
        );

        [在decimal不添加的时候 默认（10，0）---且存在四舍五入的行为]

        insert into test_decimal(f1)
        values(123),(123.45)

  
  
  
  
【开发中的经验】

![image](https://user-images.githubusercontent.com/38878365/194440917-e2d339c9-e91d-4ebb-8d57-5ecae44598a1.png)






【位类型】底层的存储是按照十六进制的存储方式;hex()转16，这里不要加，bin（）转二进制
        
        insert into test_bits(f2)
        values(31);

      【使用十进制存储】
