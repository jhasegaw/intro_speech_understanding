import numpy as np

def generate_pure_tone(frequency, sample_rate, duration):
    '''
    Generate a pure tone at the specified frequency, sampling rate, and duration.
    
    @parameter:
    frequency (scalar) - the frequency of the pure tone, in Hertz
    sample_rate (scalar) - how many samples per second?
    duration (scalar) - the duration of the pure tone, in seconds
    
    @return:
    x (array) - the pure tone signal
    '''
    t = np.linspace(0,duration,int(duration*sample_rate))
    x = np.sin(2*np.pi*frequency*t)
    return(x)

