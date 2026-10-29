import numpy as np

def gradient_descent(x,y,k,tau,learning_rate):

    # number of training examples (n)
    n = x.shape[0]

    # number of independent variable
    m = x.shape[1]

    # coeficents or wieghts
    beta = np.random.randn(m,1)

    previous_cost = 0.0

    for _ in range(k):

        y_pred = x @ beta

        error = y_pred - y

        cost = np.sum(error**2)/(2*n)

        if abs(previous_cost - cost) < tau:
            break

        gradient = (x.T @ error)/n

        beta = beta -learning_rate * gradient

        previous_cost = cost

    return beta , cost

print("Gradient Descent:- ")
print("#"*10)
gradient_descent(10,3,8,9,0.1)