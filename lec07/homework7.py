import numpy as np

def major_chord(f, Fs):
    '''
    Generate a one-half-second major chord, based at frequency f, with sampling frequency Fs.
    '''
    duration = 0.5  # seconds
    t = np.arange(0, duration, 1/Fs)

    # Frequencies of the chord
    f_root = f
    f_major_third = f * (2 ** (4/12))   # 4 semitones up
    f_major_fifth = f * (2 ** (7/12))   # 7 semitones up

    # Generate the chord by summing sinusoids
    x = (
        np.sin(2 * np.pi * f_root * t) +
        np.sin(2 * np.pi * f_major_third * t) +
        np.sin(2 * np.pi * f_major_fifth * t)
    )

    return x


def dft_matrix(N):
    '''
    Create a DFT transform matrix, W, of size N.
    '''
    n = np.arange(N)
    k = n.reshape((N, 1))

    W = np.exp(-2j * np.pi * k * n / N)

    return W


def spectral_analysis(x, Fs):
    '''
    Find the three loudest frequencies in x.
    '''
    N = len(x)

    # Compute DFT using FFT (more efficient than matrix multiplication)
    X = np.fft.fft(x)
    magnitude = np.abs(X)

    # Only use positive frequencies
    freqs = np.fft.fftfreq(N, d=1/Fs)
    positive_indices = freqs >= 0

    freqs = freqs[positive_indices]
    magnitude = magnitude[positive_indices]

    # Find indices of three largest peaks
    peak_indices = np.argsort(magnitude)[-3:]

    # Get corresponding frequencies
    peak_freqs = freqs[peak_indices]

    # Sort frequencies
    f1, f2, f3 = np.sort(peak_freqs)

    return f1, f2, f3
