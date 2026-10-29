import numpy as np

def Logistic_regression(X,Y,k,tau,learning_rate):

    m = X.shape[1]
    beta = np.random.randn(m)

    previous_cost =  float("inf")

    for epoch in range(k):
        z = X @ beta
        y_pred = 1 / (1 + np.exp(-z))

        n = X.shape[0]
        epsilon = 1e-15

        y_pred = np.clip(y_pred, epsilon, 1-epsilon)

        cost = -(1/n) * np.sum(Y*np.log(y_pred) + (1-Y)*np.log(1-y_pred))
        error = y_pred - Y.flatten()

        gradient = (1/n) * X.T @ (error)

        beta = beta - learning_rate *gradient

        cost_change = abs(previous_cost - cost)

        if cost_change < tau:
            print(f"stoping at epoch {epoch}")
            print(f"cost change: {cost_change}")
            break

        previous_cost = cost


    return beta , cost


from Solution_1 import GenrateData
X, Y, beta_true= GenrateData(n=100,m=3,theta=0.1)

beta_learned, final_cost = Logistic_regression(
    X,Y,
    k=1000,
    tau=1e-6,
    learning_rate=0.01
)
#
# print(f"final cost: {final_cost}")
# print(f"beta_learned: {beta_learned}")
# print(F"True beta {beta_true}")
#





