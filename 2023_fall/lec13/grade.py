import unittest, pathlib, json
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
    def import_homework13(self):
        try:
            import homework13
            self.homework13 = homework13
        except:
            self.fail("You did not upload a text file called homework13.py!")

    def extract_stories_from_NPR_text(self, webpage_text):
        try:
            stories = self.homework13.extract_stories_from_NPR_text(webpage_text)
            return stories
        except AttributeError:
            self.fail("homework13.py does not have a method called extract_stories_from_NPR_text!")
    
    def read_nth_story(self, stories, n, filename):
        try:
            self.homework13.read_nth_story(stories, n, filename)
        except AttributeError:
            self.fail("homework13.py does not have a method called read_nth_story!")
    
    def assertIsFile(self, path):
        if not pathlib.Path(path).resolve().is_file():
            raise AssertionError("File does not exist: %s" % str(path))

    def test_extract_stories_from_NPR_text_exists(self):
        self.import_homework13()
        with open('npr_webpage.html') as f:
            webpage_text = f.read()
        self.extract_stories_from_NPR_text(webpage_text)
        self.assertTrue("homework13.py contains a method called 'extract_stories_from_NPR_text'")
       
    def test_read_nth_story_exists(self):
        self.import_homework13()
        with open('stories.json') as f:
            stories = json.load(f)
        self.read_nth_story(stories, 3, 'test.mp3')
        self.assertTrue("homework13.py contains a method called 'read_nth_story'")
       
    def test_extract_stories_from_NPR_text_returns_list_of_strings(self):
        self.import_homework13()
        with open('npr_webpage.html') as f:
            webpage_text = f.read()
        stories = self.extract_stories_from_NPR_text(webpage_text)
        self.assertIsInstance(stories, list, 'extract_stories_from_NPR_text should return a list')
        self.assertGreater(len(stories), 0, 'extract_stories_from_NPR_text should not be zero-length')
        self.assertIsInstance(stories[0],tuple,'extract_stories_from_NPR_text should be list of tuples')
        self.assertIsInstance(stories[0][0],str,'extract_stories_from_NPR_text should be list of tuples of strings')
       
    def test_extract_stories_from_NPR_text_returns_correct_list(self):
        self.import_homework13()
        with open('npr_webpage.html') as f:
            webpage_text = f.read()
        with open('stories.json') as f:
            ref = json.load(f)
        stories = self.extract_stories_from_NPR_text(webpage_text)
        self.assertIsInstance(stories, list, 'extract_stories_from_NPR_text should return a list')
        self.assertGreater(len(stories), 0, 'extract_stories_from_NPR_text should not be zero-length')
        self.assertIsInstance(stories[0],tuple,'extract_stories_from_NPR_text should be list of tuples')
        self.assertIsInstance(stories[0][0],str,'extract_stories_from_NPR_text should be list of tuples of strings')
        self.assertEqual(stories[0][0], ref[0][0],
                         '''
                         extract_stories_from_NPR_text should return %s, instead it returns %s
                         '''%(ref[0][0],stories[0][0]))
       
    def test_read_nth_story_creates_file(self):
        self.import_homework13()
        with open('stories.json') as f:
            stories = json.load(f)
        self.read_nth_story(stories, 3, 'test.mp3')
        self.assertIsFile("test.mp3")

    def test_read_nth_story_creates_correct_synthesis(self):
        self.import_homework13()
        with open('stories.json') as f:
            stories = json.load(f)
        self.read_nth_story(stories, 3, 'test.mp3')
        with open("test.mp3", "rb") as f:
            hypothesis = f.read()
        with open("solution.mp3", "rb") as f:
            reference = f.read()
        self.assertEqual(int(len(hypothesis)/1024), int(len(reference)/1024),
                         '''
                         read_nth_story creates a file with the wrong content.
                         '''
        )

suite = unittest.defaultTestLoader.loadTestsFromTestCase(Test)
result = unittest.TextTestRunner().run(suite)

n_success = result.testsRun - len(result.errors) - len(result.failures)
print('%d successes out of %d tests run'%(n_success, result.testsRun))
print('Score: %d%%'%(int(100*(n_success/result.testsRun))))
                                
                    
                        

