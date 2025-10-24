import numpy as np
def perceptronOutput(W,X):
    if np.dot(W,X) >= 0:
        return 1
    else:
        return -1
#  Initial set of weights      
W = [-0.6, 0.75, 0.5]