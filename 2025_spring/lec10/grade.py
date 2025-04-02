import unittest, homework10
import numpy as np

data = np.load('recording.npz')
speech = data['speech']
Fs = data['Fs']

# TestSequence
class Test(unittest.TestCase):
    def test_waveform_to_frames(self):
        frame_length = int(0.025*Fs)
        step = int(0.01*Fs)
        frames = homework10.waveform_to_frames(speech, frame_length, step)
        num_frames = int((len(speech)-frame_length)/step)
        self.assertEqual(len(frames.shape), 2, 'waveform_to_frames should return a matrix')
        self.assertEqual(frames.shape[0],frame_length,'waveform_to_frames # rows should be frame_length')
        self.assertGreaterEqual(frames.shape[1],num_frames,
                                '''
                                waveform_to_frames # columns should be >=
                                (len(waveform)-frame_length)/step
                                ''')
        self.assertEqual(frames[3,5], speech[5*step + 3],
                         'waveform_to_frames[3,5] should be waveform[5*step+3]')

    def test_frames_to_stft(self):
        frame_length = int(0.025*Fs)
        step = int(0.01*Fs)
        frames = homework10.waveform_to_frames(speech, frame_length, step)
        stft = homework10.frames_to_stft(frames)
        
        self.assertEqual(len(stft.shape), 2, 'frames_to_stft should return a matrix')
        self.assertTrue(np.iscomplexobj(stft), 'frames_to_stft output should be complex')
        self.assertEqual(stft.shape[0],frames.shape[0],
                         'frames_to_stft input and output should be same size')
        self.assertEqual(stft.shape[1],frames.shape[1],
                         'frames_to_stft input and output should be same size')
        ref = np.fft.fft(frames,axis=0)
        self.assertAlmostEqual(np.sum(np.imag(ref)), np.sum(np.imag(stft)), places=1,
                               msg="frames_to_stft output doesn't match correct answer")
        self.assertAlmostEqual(np.sum(np.real(ref)), np.sum(np.real(stft)), places=1,
                               msg="frames_to_stft output doesn't match correct answer")
        
    def test_stft_to_spectrogram(self):
        frame_length = int(0.025*Fs)
        step = int(0.01*Fs)
        frames = homework10.waveform_to_frames(speech, frame_length, step)
        stft = homework10.frames_to_stft(frames)
        spectrogram = homework10.stft_to_spectrogram(stft)
        self.assertEqual(len(spectrogram.shape),2,'stft_to_spectrogram should return a matrix')
        self.assertFalse(np.iscomplexobj(spectrogram),'stft_to_spectrogram output should NOT be complex')
        self.assertEqual(stft.shape[0],spectrogram.shape[0],
                         'stft_to_spectrogram input and output should be same size')
        self.assertEqual(stft.shape[1],spectrogram.shape[1],
                         'stft_to_spectrogram input and output should be same size')
        self.assertEqual(np.amax(spectrogram),0,msg='np.amax(spectrogram) should be 0')
        self.assertGreaterEqual(np.amin(spectrogram),-60,msg='np.amin(spectrogram) should be >=-60')
        ref = 20*np.log10(np.maximum(0.001,np.abs(stft)/np.amax(np.abs(stft))))
        self.assertAlmostEqual(np.sum(ref), np.sum(spectrogram), places=1,
                               msg="stft_to_spectrogram output doesn't match correct answer")
        
suite = unittest.defaultTestLoader.loadTestsFromTestCase(Test)
result = unittest.TextTestRunner().run(suite)

n_success = result.testsRun - len(result.errors) - len(result.failures)
print('%d successes out of %d tests run'%(n_success, result.testsRun))
print('Score: %d%%'%(int(100*(n_success/result.testsRun))))
                                
                    
                        

