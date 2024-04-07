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
    def import_homework14(self):
        try:
            import homework14
            self.homework14 = homework14
        except:
            self.fail("You did not upload a text file called homework14.py!")

    def assertIsFile(self, path):
        if not pathlib.Path(path).resolve().is_file():
            raise AssertionError("File does not exist: %s" % str(path))

    def test_what_time_is_it_runs(self):
        self.import_homework14()
        try:
            self.homework14.what_time_is_it("en","time_en.mp3")
        except:
            self.fail("homework14.what_time_is_it does not finish!")
        self.assertTrue("homework14.py contains a method called what_time_is_it")
       
    def test_tell_me_a_joke_runs(self):
        self.import_homework14()
        try:
            self.homework14.tell_me_a_joke("en", "joke_en.mp3")
        except:
            self.fail("homework14.tell_me_a_joke does not finish!")
        self.assertTrue("homework14.py contains a method called tell_me_a_joke")
       
    def test_what_day_is_it_runs(self):
        self.import_homework14()
        try:
            self.homework14.what_day_is_it("en","calendar_en.mp3")
        except:
            self.fail("homework14.what_day_is_it does not finish!")
        self.assertTrue("homework14.py contains a method called what_day_is_it")
       
    def test_what_time_is_it_creates_file(self):
        self.import_homework14()
        try:
            self.homework14.what_time_is_it("ja","time_ja.mp3")
        except AttributeError:
            self.fail("homework14.py does not have a method called what_time_is_it!")
        self.assertIsFile("time_ja.mp3")
       
    def test_tell_me_a_joke_creates_file(self):
        self.import_homework14()
        try:
            self.homework14.tell_me_a_joke("ja", "joke_ja.mp3")
        except AttributeError:
            self.fail("homework14.py does not have a method called tell_me_a_joke!")
        except:
            pass
        self.assertIsFile("joke_ja.mp3")
       
    def test_what_day_is_it_creates_file(self):
        self.import_homework14()
        try:
            self.homework14.what_day_is_it("ja","calendar_ja.mp3")
        except AttributeError:
            self.fail("homework14.py does not have a method called what_day_is_it!")
        except:
            pass
        self.assertIsFile("calendar_ja.mp3")
       
suite = unittest.defaultTestLoader.loadTestsFromTestCase(Test)
result = unittest.TextTestRunner().run(suite)

n_success = result.testsRun - len(result.errors) - len(result.failures)
print('%d successes out of %d tests run'%(n_success, result.testsRun))
print('Score: %d%%'%(int(100*(n_success/result.testsRun))))
                                
                    
                        
