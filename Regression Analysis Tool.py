import numpy as np

def compute_mse(X, y, N):
    import numpy as np
    from numpy.linalg import inv
    betas = inv(X.T @ X) @ X.T @ y
    y_hat = X[:, 0] * betas[0]
    for i in range(1, X.shape[1]):
        y_add = X[:, i] * betas[i]
        y_hat += y_add
    mse = ((np.sum((y - y_hat) ** 2))/N)
    return betas, y_hat, mse
