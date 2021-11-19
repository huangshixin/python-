from _11_02_check_class import *
import unittest

question = "what language did you first learn to speak?"
my_survey = anonymoussSurvey(question)#此时系统中的question已经有个新的值，并且创建了一个空的response

my_survey.show_question()
print("enter 'q' at any time to quit.\n")
while True:
    response = input("language:")
    if response == 'q':
        break
    else:
        my_survey.store_response(response)

print("\nThank you to everyone who participated in this party tonight ")#tonight 前面不需要介词

#开始测试项目
class Test_response(unittest.TestCase):

    def test_response_name(self):
        question = "what language did you first learn to speak?"
        response_name = anonymoussSurvey(question)
        response_name.store_response('ENGLISH')

        self.assertIn('ENGLISH',my_survey.response)

    def test_store_three_response(self):
        question = "what language did you first learn to speak?"
        response_name = anonymoussSurvey(question)
        response = ['ENGLISH','FRANCE','CHINESE']
        for items in response:
            response_name.store_response(items)
            self.assertIn(items,response_name.response)


unittest.main()