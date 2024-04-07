import unittest, homework4

# TestSequence
class Test(unittest.TestCase):

    def test_list_to_dict_type(self):
        a = homework4.list_to_dict([])
        self.assertIs(type(a), type({}), "list_to_dict([]) should return a %s but it returns a %s"%(type({}),type(a)))

    def test_list_to_dict_output(self):
        a = homework4.list_to_dict(["a", "b", "c"])
        self.assertEqual(len(a), 3, "list_to_dict, given a list of length 3, returns a dictionary with %d entries: %s"%(len(a), str(a)))
        self.assertIn(0, a, "list_to_dict should return a dict with key 0, but does not: %s"%(str(a)))
        self.assertEqual(a[0], "a", "x=list_to_dict(input_list) does not produce x[0] containing the first element of input_list: %s"%(str(a))) 
        self.assertIn(1, a, "list_to_dict should return a dict with key 1, but does not: %s"%(str(a)))
        self.assertEqual(a[1], "b", "x=list_to_dict(input_list) does not produce x[1] containing the second element of input_list: %s"%(str(a))) 

suite = unittest.defaultTestLoader.loadTestsFromTestCase(Test)
result = unittest.TextTestRunner().run(suite)

n_success = result.testsRun - len(result.errors) - len(result.failures)
print('%d successes out of %d tests run'%(n_success, result.testsRun))
print('Score: %d%%'%(int(100*(n_success/result.testsRun))))
