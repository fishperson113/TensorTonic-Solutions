import numpy as np

def rnn_step_forward(x_t, h_prev, Wx, Wh, b):
    """
    Returns: h_t of shape (H,)
    """
    # Write code here
    x_t=np.array(x_t)
    h_prev=np.array(h_prev)
    Wx=np.array(Wx)
    Wh=np.array(Wh)
    b=np.array(b)
    sum=x_t@Wx+h_prev@Wh+b
    return tanh(sum).flatten()

def tanh(x):
    x=np.array(x,dtype=float)
    return (np.exp(x)-np.exp(-x))/(np.exp(x)+np.exp(-x))