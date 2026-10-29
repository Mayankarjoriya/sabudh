from Machine_learning.ML_Coursework_2.Solution_3 import accuracy
from Solution_2 import Logistic_regression
from Solution_1 import GenrateData
import numpy as np


def LogisticRegularization(X,Y,k,tau,learning_rate, lambda_reg=0.0,
                               reg_type=None):

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

        # ========= ADD Rgularization =========
        if reg_type == 'L2':
            cost += (lambda_reg / (2 * n)) * np.sum(beta[1:] ** 2)
            gradient[1:] += (lambda_reg/n) *beta[1:]

        elif reg_type == 'L1':
            cost += (lambda_reg / n) * np.sum(np.abs(beta[1:]))
            gradient[1:] += (lambda_reg/n)*np.sign(beta[1:])
        else:
            continue

        beta = beta - learning_rate *gradient

        cost_change = abs(previous_cost - cost)

        if cost_change < tau:
            print(f"stoping at epoch {epoch}")
            print(f"cost change: {cost_change}")
            break

        previous_cost = cost


    return beta , cost

lambda_reg = [0,0.01,0.1,1,10,100]
m=4
n=100
X,Y,beta_true = GenrateData(m,m,theta=0.3)




for lam in lambda_reg:

    print(f"\nFor lambda = {lam}")
    """"L2 regularization"""
    beta_l2, cost_l2, = LogisticRegularization(X,Y,k=100,tau=1e-6,
                                               learning_rate=0.1,
                                               lambda_reg=lam,
                                               reg_type='L2')
    """"L1 regularization"""
    beta_l1 , cost_l1 = LogisticRegularization(X,Y,
                                               k=100,
                                               tau=1e-6,
                                               learning_rate=0.1,
                                               lambda_reg=lam,
                                               reg_type='L1')

    """"Logistic regression Without regularization"""

    beta,cost= Logistic_regression(X,Y,
                                   k=100,
                                    tau=1e-6,
                                    learning_rate=0.1,
                                   )
    error_l2 = np.linalg.norm(beta_l2-beta_true)
    error_l1 = np.linalg.norm(beta_l1 - beta_true)
    error = np.linalg.norm(beta - beta_true)

    print(f"\nL2 error: {error_l2}",
          f"\nL1 error: {error_l1}",
          f"\nWithout regularization Error: {error}")

    print(f" \nL1 beta = {np.round(beta_l2,3)}")
    print(f" \nL2 beta = {np.round(beta_l1,3)}")
    print(f" \nWithout regularization beta = {np.round(beta_true,3)}")

