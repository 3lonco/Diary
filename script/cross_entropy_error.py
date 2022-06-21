import numpy as np


def cross_entropy_error(y, t):
    # Where, we plus delta because np.log(0) is negative infinity that stop a model from proceeding this process.
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)
    batch_size = y.shape[0]
    delta = 1e-7
    return -np.sum(np.log(y[np.arange(batch_size), t] + delta)) / batch_size
