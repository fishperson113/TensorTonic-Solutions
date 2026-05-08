import numpy as np
import math
def euclidean_distance(x, y):
    """
    Compute the Euclidean (L2) distance between vectors x and y.
    Must return a float.
    """
    # Write code here
    X=np.array(x)
    Y=np.array(y)
    return float(math.sqrt(np.sum((np.abs(X-Y))*(np.abs(X-Y)))))