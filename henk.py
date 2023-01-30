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

N = 100
kak = np.array([4,67,2,7,3,7,2])
kak = kak[:, np.newaxis]
X = np.array([1,2,3,4,5,6,7])
X = X[:, np.newaxis]
y = np.array([6,7,8,9,1,2,3])
y = y[:, np.newaxis]
icept = np.ones((X.size, 1))
X_1 = np.hstack((icept, X))
X_2 = np.hstack((X_1, y))
X_3 = np.hstack((X_2, kak))
    #run lstsq
    #calc y_hat

 # which emotion): %.2f" % emo_neutral_contrast)
