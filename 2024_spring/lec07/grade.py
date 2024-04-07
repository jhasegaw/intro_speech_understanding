import unittest, homework7
import numpy as np

def voiced_excitation(duration, F0, Fs):
    '''
    Create voiced speeech excitation.
    
    @param:
    duration (scalar) - length of the excitation, in samples
    F0 (scalar) - pitch frequency, in Hertz
    Fs (scalar) - sampling frequency, in samples/second
    
    @returns:
    excitation (np.ndarray) - the excitation signal, such that
      excitation[n] = -1 if n is an integer multiple of int(np.round(Fs/F0))
      excitation[n] = 0 otherwise
    '''
    T0 = int(np.round(Fs/F0))
    excitation = np.zeros(duration)
    excitation[::T0] = -1
    return excitation

def resonator(x, F, BW, Fs):
    '''
    Generate the output of a resonator.
    
    @param:
    x (np.ndarray(N)) - the excitation signal
    F (scalar) - resonant frequency, in Hertz
    BW (scalar) - resonant bandwidth, in Hertz
    Fs (scalar) - sampling frequency, in samples/second
    
    @returns:
    y (np.ndarray(N)) - resonant output
    '''
    C = -np.exp(-2*np.pi*BW/Fs)
    B = 2 * np.exp(-np.pi*BW/Fs) * np.cos(2*np.pi*F/Fs)
    A = 1 - B - C
    y = np.zeros(len(x))
    y[0] = A*x[0]
    y[1] = A*x[1] + B*y[0]
    for n in range(2,len(y)):
        y[n] = A*x[n] + B*y[n-1] + C*y[n-2]
    return y


# TestSequence
class Test(unittest.TestCase):
    def test_voiced_excitation(self):
        excitation = homework7.voiced_excitation(8000, 100, 8000)
        self.assertEqual(len(excitation), 8000, 'voiced_excitation(8000...) should be 8000 samples long')
        self.assertEqual(excitation[0], -1, "voiced_excitation[0] should be -1")
        self.assertEqual(excitation[1], 0, "voiced_excitation[1] should be 0")
        self.assertEqual(excitation[2], 0, "voiced_excitation[2] should be 0")
        self.assertEqual(excitation[80], -1, "voiced_excitation[80] should be -1 if F0=100")
        
    def test_resonator(self):
        x = np.zeros(100)
        x[0] = -1
        F = 500
        BW = 100
        Fs = 8000
        C = -np.exp(-2*np.pi*BW/Fs)
        B = 2 * np.exp(-np.pi*BW/Fs) * np.cos(2*np.pi*F/Fs)
        A = 1 - B - C
        y = np.zeros(len(x))
        y[0] = A*x[0]
        y[1] = A*x[1] + B*y[0]
        for n in range(2,len(y)):
            y[n] = A*x[n] + B*y[n-1] + C*y[n-2]
        resonance = homework7.resonator(x, F, BW, Fs)
        self.assertEqual(len(resonance), len(y), 'resonator output should be same length as x')
        self.assertAlmostEqual(resonance[0], y[0], 'resonator[0] should be %g'%(x[0]))
        self.assertAlmostEqual(resonance[1], y[1], 'resonator[1] should be %g'%(x[1]))
        self.assertAlmostEqual(resonance[2], y[2], 'resonator[2] should be %g'%(x[2]))
        
    def test_synthesize_vowel(self):
        duration = 8000
        F0 = 110
        F1 = 500
        F2 = 1500
        F3 = 2500
        F4 = 3500
        BW1 = 100
        BW2 = 200
        BW3 = 300
        BW4 = 400
        Fs = 8000
        resonance = homework7.synthesize_vowel(duration,F0,F1,F2,F3,F4,BW1,BW2,BW3,BW4,Fs)
        excitation = voiced_excitation(duration, F0, Fs)
        y1 = resonator(excitation, F1, BW1, Fs)
        y2 = resonator(y1, F2, BW2, Fs)
        y3 = resonator(y2, F3, BW3, Fs)
        x = resonator(y3, F4, BW4, Fs)
        self.assertEqual(len(resonance), duration, 'synthesize_vowel output length should equal duration')
        self.assertAlmostEqual(resonance[0], x[0], 'synthesize_vowel[0] should be %g'%(x[0]))
        self.assertAlmostEqual(resonance[1], x[1], 'synthesize_vowel[1] should be %g'%(x[1]))
        self.assertAlmostEqual(resonance[2], x[2], 'synthesize_vowel[2] should be %g'%(x[2]))


suite = unittest.defaultTestLoader.loadTestsFromTestCase(Test)
result = unittest.TextTestRunner().run(suite)

n_success = result.testsRun - len(result.errors) - len(result.failures)
print('%d successes out of %d tests run'%(n_success, result.testsRun))
print('Score: %d%%'%(int(100*(n_success/result.testsRun))))
