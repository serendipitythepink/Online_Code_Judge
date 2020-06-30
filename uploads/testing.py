from to_be_tested import say_hello
import unittest


class MyTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open('test_result.txt', 'w') as fwrite:
            fwrite.write('')
    
    def test_upload1(self):
        try:
            self.assertEqual(say_hello(), 'Hello  running!')
            with open('test_result.txt', 'a') as fappend:
                fappend.write('Test1:Pass\n')
        except:
            with open('test_result.txt', 'a') as fappend:
                fappend.write('Test1:Fail\n')
    
    def test_upload2(self):
        try:
            self.assertEqual(say_hello(), 'Hello I am the uploaded!')
            with open('test_result.txt', 'a') as fappend:
                fappend.write('Test2:Pass\n')
        except:
            with open('test_result.txt', 'a') as fappend:
                fappend.write('Test2:Fail\n')
    
    def test_upload3(self):
        try:
            self.assertEqual(say_hello(), 'Hello!')
            with open('test_result.txt', 'a') as fappend:
                fappend.write('Test3:Pass\n')
        except:
            with open('test_result.txt', 'a') as fappend:
                fappend.write('Test3:Fail\n')

if __name__ == '__main__':
    unittest.main()