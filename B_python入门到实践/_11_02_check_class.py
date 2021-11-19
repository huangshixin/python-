import unittest

def test():
    """ 测试类"""
"""
python提供了积累常用的断言
assertEqual（a，b） 判断a==b
assertNotEqual（a，b） a！=b
assertTrue（x） 核实x为true
assertFalse（x） 核实x为false
assertIn（item，list） 核实item这个值在列表当中
assertNotIN(item,list) 核实这个值 不在列表当中
"""

class anonymoussSurvey():
    """ """
    def __init__(self,question):
        
        self.question = question
        self.response = []#对应一个空列表

    def show_question(self):


        return  self.question

    def store_response(self,new_response):

        self.response.append(new_response)

    def show_result(self):

        print("survey result!")
        for result in self.response:
            print('-'+result)