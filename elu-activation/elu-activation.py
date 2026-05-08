import numpy as np
def elu(x, alpha):
    """
    Apply ELU activation to each element.
    """
    # Write code here
    u=np.array(x)
    result = np.where(u>0,u,alpha*(np.exp(u)-1))
    return result.tolist()