import unittest, pathlib
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
    def import_homework12(self):
        try:
            import homework12
            self.homework12 = homework12
        except:
            self.fail("You did not upload a text file called homework12.py!")

    def synthesize(self, text, lang, filename):
        try:
            self.homework12.synthesize(text, lang, filename)
        except AttributeError:
            self.fail("homework12.py does not have a method called synthesize!")
    
    def assertIsFile(self, path):
        if not pathlib.Path(path).resolve().is_file():
            raise AssertionError("File does not exist: %s" % str(path))

    def test_method_exists(self):
        self.import_homework12()
        self.synthesize("This is speech synthesis!","en","english.mp3")
        self.assertTrue("homework12.py contains a method called 'synthesize'")
       
    def test_method_creates_file(self):
        self.import_homework12()
        self.synthesize("This is speech synthesis!","en","english.mp3")
        self.assertIsFile("english.mp3")

    def test_method_creates_correct_synthesis_english(self):
        self.import_homework12()
        self.synthesize("This is speech synthesis!","en","english.mp3")
        with open("english.mp3", "rb") as f:
            hypothesis = f.read()
        with open("solution_english.mp3", "rb") as f:
            reference = f.read()
        self.assertEqual(int(len(hypothesis)/1024), int(len(reference)/1024),
                         '''
                         homework12.synthesize("This is speech synthesis!","en","english.mp3")
                         creates a file with the wrong content.
                         '''
        )

    def test_method_creates_correct_synthesis_spanish(self):
        self.import_homework12()
        self.synthesize("¡Esto es síntesis de voz!","es","spanish.mp3")
        with open("spanish.mp3", "rb") as f:
            hypothesis = f.read()
        with open("solution_spanish.mp3", "rb") as f:
            reference = f.read()
        self.assertEqual(int(len(hypothesis)/1024), int(len(reference)/1024),
                         '''
                         homework12.synthesize, when called with a non-English text string,
                         creates a file with the wrong content.
                         '''
        )

suite = unittest.defaultTestLoader.loadTestsFromTestCase(Test)
result = unittest.TextTestRunner().run(suite)

n_success = result.testsRun - len(result.errors) - len(result.failures)
print('%d successes out of %d tests run'%(n_success, result.testsRun))
print('Score: %d%%'%(int(100*(n_success/result.testsRun))))
                                
                    
                        

