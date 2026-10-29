import numpy as np

from Solution_1 import GenrateData
from Solution_2 import Logistic_regression

# ################DATA SET 1 #########################################333
X, Y,true_beta = GenrateData(
    n=100,
    m=4,
    theta=0.3
)

beta_learned,final_cost = Logistic_regression(
    X,
    Y,
    k=1000,
    tau=1e-6,
    learning_rate=0.1,
)

# ###############DATA SET 2 ##############################33
X2, Y2,true_beta2 = GenrateData(
    n=100,
    m=4,
    theta=0.2
)

beta_learned2,final_cost2 = Logistic_regression(
    X2,
    Y2,
    k=1000,
    tau=1e-6,
    learning_rate=0.1,
)

# ###############DATA SET 3 ##############################33
X3, Y3,true_beta3 = GenrateData(
    n=1000,
    m=4,
    theta=0.3
)

beta_learned3,final_cost3 = Logistic_regression(
    X3,
    Y3,
    k=1000,
    tau=1e-6,
    learning_rate=0.1,
)



print(f"Final cost: {final_cost}")
print(f"Beta: {beta_learned}")
print(f"True beta: {true_beta}")


# Error
# Euclidean Distance
ed_distance = np.linalg.norm(beta_learned - true_beta)
print(f"Euclidean distance For Data Set 1 (Noise - 30%): {ed_distance}")
ed_distance_2 = np.linalg.norm(beta_learned2 - true_beta2)
print(f"Euclidean distance For Data Set 2 (Noise - 20%): {ed_distance_2}")
ed_distance3 =np.linalg.norm(beta_learned3 - true_beta3)
print(f"Euclidean distance For Data Set 3 (Noise - 30%): {ed_distance3}")


# Test dataset
X_test, Y_test, true_beta_test = GenrateData(
    n=100,
    m=4,
    theta=0
)
beta_learned_test,final_cost_test = Logistic_regression(
    X_test,
    Y_test,
    k=1000,
    tau=1e-6,
    learning_rate=0.1,
)


print("#"*50, "\n")
print(f"Final cost for test set: {final_cost_test}")
print(f"Beta For testset: {beta_learned_test}")
print(f"True beta for testset: {true_beta_test}")
print(f"Euclidean distance for testset: {np.linalg.norm(beta_learned_test - true_beta_test)}")


# Accueacy


z_test = X_test @ beta_learned
z_test2 = X_test @ beta_learned2
z_test3 = X_test @ beta_learned3

probabilities = 1/ (1+np.exp(-z_test))
probabilities2 = 1/(1+np.exp(-z_test2))
probabilities3 = 1/(1+np.exp(-z_test3))

Y_pred = (probabilities >0.5).astype(int)
Y_pred2 = (probabilities2 >0.5).astype(int)
Y_pred3 = (probabilities3 >0.5).astype(int)


accuracy = np.mean(Y_pred == Y_test.flatten())
accuracy_2 = np.mean(Y_pred2 == Y_test.flatten())
accuracy_3 = np.mean(Y_pred3 == Y_test.flatten())

print(f"Accuracy with Data-Set 1 with n=100 & theta(noise)=30%: {accuracy}")
print(f"Accuracy with Data-Set 2 with n=100 & theta(noise)=20%: {accuracy_2}")
print(f"Accuracy with Data-Set 3 with n=1000 & theta(noise)=30%: {accuracy_3}")





###########################################################################################
############## Theoritical Gradient ######################################################


def Logistic_regression_2(X,Y,k,tau,learning_rate):

    m = X.shape[1]
    beta = np.random.randn(m)

    previous_cost =  float("inf")

    for epoch in range(k):
        z = X @ beta
        y_pred = 1 / (1/np.exp(-z))

        n = X.shape[0]
        epsilon = 1e-15

        y_pred = np.clip(y_pred, epsilon, 1-epsilon)

        # Gradient part

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


    return beta , cost , error

beta, final_cost, error = Logistic_regression_2(X,Y,k=1000,tau=1e-6,learning_rate=0.1)
number_of_point_in_error = error.shape[0]
print((1/number_of_point_in_error) * np.sum(error))