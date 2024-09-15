import unittest
from contextlib import contextmanager,redirect_stderr,redirect_stdout
from os import devnull

@contextmanager
def suppress_stdout_stderr():
    """A context manager that redirects stdout and stderr to devnull"""
    with open(devnull, 'w') as fnull:
        with redirect_stderr(fnull) as err, redirect_stdout(fnull) as out:
            yield (err, out)


# TestSequence
class Test(unittest.TestCase):
    def test_method_runs(self):
        import homework11
        try:
            transcription = homework11.transcribe_wavefile("webdata.wav")
        except:
            self.fail("homework11.transcribe_wavefile does not run (has errors)")
        self.assertTrue(True, "homework11.transcribe_wavefile runs")
       
    def test_method_returns_str(self):
        import homework11
        transcription = homework11.transcribe_wavefile("webdata.wav")
        self.assertIs(type(transcription), type("hello"),
                      '''
                      transcribe_wavefile('webdata.wav') should return a str
                      but it returns a %s
                      '''%(type(transcription)))

    def test_method_works_with_known_input(self):
        import homework11
        filename = '264752__copyc4t__phone-messages-english-and-italian.flac'
        transcription = homework11.transcribe_wavefile(filename)
        ref = "thank you please wait"
        self.assertEqual(transcription[:len(ref)],ref,
                         '''
                         transcribe_wavefile('264752__copyc4t__phone-messages-english-and-italian.flac') should return a string starting with
                         %s but instead it returns %s
                         '''%(ref,transcription))
        
suite = unittest.defaultTestLoader.loadTestsFromTestCase(Test)
result = unittest.TextTestRunner().run(suite)

n_success = result.testsRun - len(result.errors) - len(result.failures)
print('%d successes out of %d tests run'%(n_success, result.testsRun))
print('Score: %d%%'%(int(100*(n_success/result.testsRun))))
                                
                    
                        

