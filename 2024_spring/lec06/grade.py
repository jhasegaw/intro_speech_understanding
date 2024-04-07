import unittest, homework6
import numpy as np

# TestSequence
class Test(unittest.TestCase):
    def test_minimum_Fs(self):
        Fs = homework6.minimum_Fs(440)
        self.assertEqual(Fs,880,'Fs should be 2f, not %d'%(Fs))
        
    def test_omega(self):
        omega = homework6.omega(1000,8000)
        self.assertAlmostEqual(omega,np.pi/4,'omega should be 2πf/Fs, not %g'%(omega))
        
    def test_pure_tone_duration(self):
        N = int(8000/440)
        omega = 2*np.pi*440/8000
        x = homework6.pure_tone(omega, N)
        self.assertEqual(len(x),N,'pure_tone length should be %d not %d'%(N,len(x)))

    def test_pure_tone_value(self):
        N = int(8000/440)
        omega = 2*np.pi*440/8000
        x = homework6.pure_tone(omega, N)
        y = np.cos(omega*np.arange(N))
        self.assertEqual(x[4],y[4],'pure_tone 5th sample should be %g not %g'%(y[5],x[4]))

suite = unittest.defaultTestLoader.loadTestsFromTestCase(Test)
result = unittest.TextTestRunner().run(suite)

n_success = result.testsRun - len(result.errors) - len(result.failures)
print('%d successes out of %d tests run'%(n_success, result.testsRun))
print('Score: %d%%'%(int(100*(n_success/result.testsRun))))
