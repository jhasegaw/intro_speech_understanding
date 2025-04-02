import unittest, homework8
import numpy as np

# TestSequence
class Test(unittest.TestCase):
    def test_W_is_ndarray(self):
        W = homework8.dft_matrix(30)
        ref = np.zeros((30,30))
        self.assertIs(type(W), type(ref), "dft_matrix should return a numpy array")
        
    def test_W_is_complex(self):
        W = homework8.dft_matrix(30)
        self.assertEqual(W.dtype,complex,'W=dft_matrix(N) should be complex')
        
    def test_W_is_N_by_N(self):
        W = homework8.dft_matrix(30)
        self.assertEqual(len(W),30,'W=dft_matrix(N) should have N rows')
        self.assertEqual(len(W[0]),30,'W=dft_matrix(N) should have N columns')

    def test_W_gives_DFT_of_x(self):
        N = 30
        n = np.arange(N)
        x = np.cos(2*np.pi*3*n/N + np.pi/4)
        ref = np.round(np.abs(np.fft.fft(x))).astype('int')
        W = homework8.dft_matrix(N)
        X = np.round(np.abs(np.matmul(W,x))).astype('int')
        self.assertEqual(X[3],ref[3],'abs(X[3]) should be %d, not %d'%(ref[3],X[3]))

suite = unittest.defaultTestLoader.loadTestsFromTestCase(Test)
result = unittest.TextTestRunner().run(suite)

n_success = result.testsRun - len(result.errors) - len(result.failures)
print('%d successes out of %d tests run'%(n_success, result.testsRun))
print('Score: %d%%'%(int(100*(n_success/result.testsRun))))
