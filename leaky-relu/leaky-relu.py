import numpy as np

def leaky_relu(x, alpha=0.01):
    """
    Vectorized Leaky ReLU implementation.
    """
    # Write code here
    u= np.array(x)
    
    return np.where(u<0,alpha*u,u)