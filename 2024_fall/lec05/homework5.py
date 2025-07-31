import numpy as np
import matplotlib.pyplot as plt

def center_of_gravity(x):
    '''
    Find the center of gravity of a vector, x.
    If x=[x0,x1,...,xn], then you should return
    c = ( 0*x0 + 1*x1 + 2*x2 + ... + n*xn ) / sum(x)
    where n = len(x)-1.
    
    Recommended method: use np.arange, np.dot, and np.sum.
    
    @param:
    x (array): a 1d numpy array
    
    @result:
    c (scalar): x's center of gravity
    '''
    c = 0  # np.dot(x, np.arange(len(x)))) / np.sum (x)
    return c

def matched_identity(x):
    '''
    Create an identity matrix that has the same number of rows as x has elements.
    Hint: use len(x), and use np.eye.
    
    @param:
    x (array): a 1d numpy array, of length N
    
    @result:
    I (array): a 2d numpy array: an NxN identity matrix
    '''
    I =  np.eye(len(x))
    return I

def sine_and_cosine(t_start, t_end, t_steps):
    '''
    Create a time axis, and compute its cosine and sine.
    Hint: use np.linspace, np.cos, and np.sin
    
    @param:
    t_start (scalar): the starting time
    t_end (scalar): the ending time
    t_steps (scalar): length of t, x, and y
    
    @result:
    t (array of length t_steps): time axis, t_start through t_end inclusive
    x (array of length t_steps): cos(t)
    y (array of length t_steps): sin(t)
    '''
    t = np.linspace(t_start,t_end,t_steps) 
    x = np.cos(t)
    y = np.sin(t)
        return t, x, y