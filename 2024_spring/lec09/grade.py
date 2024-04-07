import unittest, homework9, json
import numpy as np

with open('speeches.json','r') as f:
    speeches = { k:np.array(v) for k,v in json.load(f).items() }

# TestSequence
class Test(unittest.TestCase):
    def test_synthesis_correct_length(self):
        X = np.fft.fft(speeches['a'])
        x = homework9.fourier_synthesis(20, X, 80)
        self.assertEqual(len(x), len(X), "fourier_synthesis output length should equal input length")
        
    def test_synthesis_magnitude(self):
        X = np.fft.fft(speeches['a'])
        x = homework9.fourier_synthesis(20, X, 80)
        X2 = np.fft.fft(x)
        maxamp = np.argmax(np.abs(X))
        self.assertAlmostEqual(np.abs(X[maxamp]), np.abs(X2[maxamp]),
                               msg="np.fft.fft(fourier_synthesis) should have same magnitudes as X")
        
    def test_synthesis_phase(self):
        X = np.fft.fft(speeches['a'])
        x = homework9.fourier_synthesis(20, X, 80)
        X2 = np.fft.fft(x)
        maxamp = np.argmax(np.abs(X))
        self.assertAlmostEqual(np.angle(X[maxamp]), np.angle(X2[maxamp]),
                               msg="np.fft.fft(fourier_synthesis) should have same phase as X")

suite = unittest.defaultTestLoader.loadTestsFromTestCase(Test)
result = unittest.TextTestRunner().run(suite)

n_success = result.testsRun - len(result.errors) - len(result.failures)
print('%d successes out of %d tests run'%(n_success, result.testsRun))
print('Score: %d%%'%(int(100*(n_success/result.testsRun))))
