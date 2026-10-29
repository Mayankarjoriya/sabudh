import numpy as np

def GenrateData(n,m,theta):
    """
    n = number of data points
    m = number of features
    theta = noise probability (0 to 1)
    """

    beta = np.random.randn(m+1)

    X = np.random.randn(n,m)
    ones = np.ones((n,1))
    X = np.hstack([ones,X])

    y = X @ beta

    sigmoid_z = 1/ (1+ np.exp(-y))
    y = (sigmoid_z > 0.5).astype(int)

    flip_mask = np.random.binomial(1,theta,n)
    y = y^flip_mask
    # y = np.logical_xor(y,flip_mask).astype(int)

    return X, y, beta


X,Y,beta = GenrateData(n=100, m=3, theta=0.1)
print(f"X Shape: {X.shape}")
print(f"Y Shape: {Y.shape}")
print(f"beta shape : {beta.shape}")



