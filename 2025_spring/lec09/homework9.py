import numpy as np

def fourier_synthesis(num_harmonics, X, T0):
    '''
    Use Fourier synthesis to resynthesize speech from its Fourier transform.
    
    @param:
    num_harmonics (scalar): the number of harmonics to resynthesize
    X (np.ndarray(N)): a length-N Fourier transform
    T0 (scalar): the pitch period, in samples
        
    @result:
    x (np.ndarray(N)): a length-N waveform, resynthesized using Fourier synthesis
    
    The Fourier synthesis equation is this:
    
    x[n] = (2/N) * sum_{l=1}^{num_harmonics} |X[l*N//T0]| * cos(2*pi*l*n/T0 + angle(X[l*N//T0]))
    '''
    #raise RuntimeError("You need to change this part")
    N = len(X)
    x = np.zeros(N)
    n = np.arange(N)
    for l in range(1,num_harmonics+1):
        x = x + (2/N) * np.abs(X[l*N//T0])* np.cos(2*np.pi*l*n/T0 + np.angle(X[l*N//T0]))
    return x

