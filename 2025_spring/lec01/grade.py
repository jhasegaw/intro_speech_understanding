import unittest, homework1
import numpy as np

class Test(unittest.TestCase):
    def test_string1(self):
        self.assertEqual(homework1.string1,"test")

    def test_string2(self):
        self.assertEqual(homework1.string2,"hello")


        
suite = unittest.defaultTestLoader.loadTestsFromTestCase(Test)
result = unittest.TextTestRunner().run(suite)

n_success = result.testsRun - len(result.errors) - len(result.failures)
print('%d successes out of %d tests run'%(n_success, result.testsRun))
print('Score: %d%%'%(int(100*(n_success/result.testsRun))))
