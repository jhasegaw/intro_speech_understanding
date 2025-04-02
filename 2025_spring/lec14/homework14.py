import datetime, gtts, bs4, random, speech_recognition

def what_time_is_it(lang, filename):
    '''
    Tell me what time it is.
    
    Parameters:
    lang (str) - language in which to speak
    filename (str) - the filename into which the audio should be recorded
    '''
    raise RuntimeError("You need to write this part!")
    
def tell_me_a_joke(lang, audiofile):
    '''
    Tell me a joke.
    
    @params:
    filename (str) - filename containing the database of jokes
    lang (str) - language
    audiofile (str) - audiofile in which to record the joke
    '''
    raise RuntimeError("You need to write this part!")

def what_day_is_it(lang, audiofile):
    '''
    Tell me what day it is.

    @params:
    lang (str) - language in which to record the date
    audiofile (str) - filename in which to read the date
    
    @returns:
    url (str) - URL that you can look up in order to see the calendar for this month and year
    '''
    raise RuntimeError("You need to write this part!")

def personal_assistant(lang, filename):
    '''
    Listen to the user, and respond to one of three types of requests:
    What time is it?
    What day is it?
    Tell me a joke!
    
    @params:
    lang (str) - language
    filename (str) - filename in which to store the result
    '''
    raise RuntimeError("You need to write this part!")
