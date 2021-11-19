from _11_01_check_code import  *
print("Tips:QUIT THIS SYSTEM WHEN YOU ENTER 'Q' INTO IT")
while True:
    first = input("请输入第一个名字")
    if first == 'q':
        break
    last  = input("请输入第二个名字")
    if last == 'q':
        break
    fullname = get_formatted_name(first,last)
    full_names = str(get_full_name(first,last))
    print(fullname+'\t'+full_names)

#单元测试和测试用例
""" python当中提供了一种unittest的代码测试工具
操作：
import unittest
以下以测试效果开始

用一个方法去测试这个get_formatted_name
1、给类做一个命名，并且包好test的字样，同时让该类继承unittest.TestCase
2、给方法命名为test----  所有的test开头的方法都会被执行
3、测试unittest当中的assert（断言）的方法：来核实结果是否和预期一致
4、unittest.main()
"""
import unittest
class NameTestCase(unittest.TestCase):#unittest.TestCase这是一个类

    def test_first_last_name(self):
        formatted_name = get_formatted_name('janis','joplin')
        self.assertEqual(formatted_name,'Janis Joplin')

    def test_first_last_middle_name(self):
        """能够准确的处理图像wolfgang amadeus amadeus这样的姓名吗？"""
        formatted_name = get_formatted_names('Wolfgang','Mozart','Amadeus')#在赋值的时候需要对位的匹配'Amadeus'对应的是middle
        print(formatted_name)#这个语句再这里是无效的
        """系统提供的插入比较"""
        self.assertEqual(formatted_name,'WOLFGANG AMADEUS MOZART')

unittest.main()


#出现一种可能：称之为 测试未通过
""" 如何处理测试未通过的结果 """
