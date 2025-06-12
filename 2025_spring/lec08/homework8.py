import numpy as np

def dft_matrix(N):
    '''
    Create a DFT transform matrix, W, of size N.
    
    @param:
    N (scalar): number of columns in the transform matrix
    
    @result:
    W (NxN array): a matrix of dtype='complex' whose (k,n)^th element is:
           W[k,n] = cos(2*np.pi*k*n/N) - j*sin(2*np.pi*k*n/N)
    '''
    #raise RuntimeError("You need to write this part")
    W = np.zeros((N,N),dtype='complex')
    for k in range(0,N):
        for n in range(0,N):
            W[k,n] = np.cos(2*np.pi*k*n/N)-(0+1j)*np.sin(2*np.pi*k*n/N)
    return W



