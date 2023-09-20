import unittest, homework5
import numpy as np

# TestSequence
class Test(unittest.TestCase):
    def test_center_of_gravity(self):
        a = homework5.center_of_gravity([1,2,3,2,1])
        self.assertAlmostEqual(a,2.0,'''Center of gravity of [1,2,3,2,1] should be 2.0''')
        
    def test_matched_identity(self):
        I = homework5.matched_identity([1,2,3,2,1])
        self.assertEqual(len(I), 5, '''I should have 5 rows if input is [1,2,3,2,1]''')
        self.assertEqual(len(I[0]), 5, '''I should have 5 columns if input is [1,2,3,2,1]''')
        eye = np.eye(5)
        for m in range(5):
            for n in range(5):
                self.assertAlmostEqual(I[m][n], eye[m][n], '''I[%d,%d] should be %g, not %g'''%(m,n,eye[m,n],I[m,n]))
        
    def test_sine_and_cosine(self):
        (t,x,y) = homework5.sine_and_cosine(0,np.pi,20)
        theta = np.linspace(0,np.pi,20)
        cos = np.cos(theta)
        sin = np.sin(theta)
        self.assertEqual(len(t), 20, '''First vector returned by sine_and_cosine should have length 20''')
        self.assertEqual(len(x), 20, '''2nd vector returned by sine_and_cosine should have length 20''')
        self.assertAlmostEqual(x[1], cos[1],'''x[1] should be %g, not %g'''%(cos[1],x[1]))
        self.assertEqual(len(y), 20, '''3rd vector returned by sine_and_cosine should have length 20''')
        self.assertAlmostEqual(y[1], sin[1],'''y[1] should be %g, not %g'''%(sin[1],y[1]))

suite = unittest.defaultTestLoader.loadTestsFromTestCase(Test)
result = unittest.TextTestRunner().run(suite)

n_success = result.testsRun - len(result.errors) - len(result.failures)
print('%d successes out of %d tests run'%(n_success, result.testsRun))
print('Score: %d%%'%(int(100*(n_success/result.testsRun))))
