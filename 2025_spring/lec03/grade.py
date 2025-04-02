import unittest, homework3


# TestSequence
class Test(unittest.TestCase):

    def test_cancellation_type(self):
        a = homework3.cancellation([], "a")
        self.assertIs(type(a), type([]), "cancellation([]) should return a %s but it returns a %s"%(type([]),type(a)))

    def test_cancellation_output(self):
        a = homework3.cancellation([True, False, "a", "b", "c", 1, 2, 3], "b")
        self.assertEqual(len(a), 3, "cancellation returned a list of the wrong length")
        self.assertEqual(a[0], True, "cancellation returned a list with the wrong values")
        self.assertEqual(a[1], False, "cancellation returned a list with the wrong values")
        self.assertEqual(a[2], "a", "cancellation returned a list with the wrong values")

    def test_copy_all_but_skip_word_type(self):
        a = homework3.copy_all_but_skip_word([], "a")
        self.assertIs(type(a), type([]), "copy_all_but_skip_word([]) should return a %s but it returns a %s"%(type([]),type(a)))

    def test_copy_all_but_skip_word_output(self):
        a = homework3.copy_all_but_skip_word([True, "b", False, "a", "b", "c", 1, 2, 3], "b")
        self.assertEqual(len(a), 7, "copy_all_but_skip_word returned a list of the wrong length")
        self.assertEqual(a[0], True, "copy_all_but_skip_word returned a list with the wrong values")
        self.assertEqual(a[1], False, "copy_all_but_skip_word returned a list with the wrong values")
        self.assertEqual(a[2], "a", "copy_all_but_skip_word returned a list with the wrong values")
        self.assertEqual(a[3], "c", "copy_all_but_skip_word returned a list with the wrong values")

    def test_my_average_type(self):
        a = homework3.my_average([0.14])
        self.assertIs(type(a), type(0.14), "my_average([0.14]) should return a %s but it returns a %s"%(type(0.14),type(a)))

    def test_my_average_output(self):
        a = homework3.my_average([4, 3, 2, 1, 0, -1, -2, -1.6])
        self.assertAlmostEqual(a, 0.675, places=2, msg="my_average returned an incorrect average")

suite = unittest.defaultTestLoader.loadTestsFromTestCase(Test)
result = unittest.TextTestRunner().run(suite)

n_success = result.testsRun - len(result.errors) - len(result.failures)
print('%d successes out of %d tests run'%(n_success, result.testsRun))
print('Score: %d%%'%(int(100*(n_success/result.testsRun))))
