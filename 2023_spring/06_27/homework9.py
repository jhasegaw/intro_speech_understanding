import numpy as np

def waveform_to_frames(waveform, frame_length, step):
    '''
    Chop a waveform into overlapping frames.
    
    @params:
    waveform (np.ndarray(N)) - the waveform
    frame_length (scalar) - length of the frame, in samples
    step (scalar) - step size, in samples
    
    @returns:
    frames (np.ndarray((frame_length, num_frames))) - waveform chopped into frames
    
    num_frames should be at least int((len(speech)-frame_length)/step); it may be longer.
    For every n and t such that 0 <= t*step+n <= N-1, it should be the case that 
       frames[n,t] = waveform[t*step+n]
    '''
    frames = np.zeros((frame_length, 5)) # change this
    return frames

def frames_to_stft(frames):
    '''
    Take the FFT of every column of the frames matrix.
    
    @params:
    frames (np.ndarray((frame_length, num_frames))) - the speech samples (real-valued)
    
    @returns:
    stft (np.ndarray((frame_length,num_frames))) - the STFT (complex-valued)
    '''
    stft = np.zeros(frames.shape, dtype='complex') # change this
    return stft

def stft_to_spectrogram(stft):
    '''
    Calculate the level, in decibels, of each complex-valued sample of the STFT,
    normalized so the highest value is 0dB, 
    and clipped so that the lowest value is -60dB.
    
    @params:
    stft (np.ndarray((frame_length,num_frames))) - STFT (complex-valued)
    
    @returns:
    spectrogram (np.ndarray((frame_length,num_frames)) - spectrogram (real-valued)
    
    The spectrogram should be expressed in decibels (20*log10(abs(stft)).
    np.amax(spectrogram) should be 0dB.
    np.amin(spectrogram) should be no smaller than -60dB.
    '''
    spectrogram = np.zeros(stft.shape) # change this
    return spectrogram


