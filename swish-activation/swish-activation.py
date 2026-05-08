import numpy as np

def swish(x):
    """
    Implement Swish activation function.
    """
    # Write code here
    x=np.array(x)
    result = x*sigmoid(x)
    return result

def sigmoid(x):
    return 1/(1+np.exp(-x))