import numpy as np

def new_dataset(sigma, n, m):
    rng = np.random.default_rng()

    x_features = rng.normal(size=(n,m))

    intercept = np.ones((n,1))

    x = np.concatenate((intercept, x_features), axis =1)

    beta = rng.normal(size= (m+1,1))

    noise = rng.normal(loc = 0,scale=sigma,size=(n,1))

    y= x@beta +noise

    return x,y,beta

print("#"*10)
sigma = int(input("Enter Noise/Standard deviation:- "))
print("#"*10)
n = int(input("Enter Size of dataset:- "))
print("#"*10)
m = int(input("Enter Number of independent variables/features:- "))
print("")
print("New Dataset:- ")
print(new_dataset(sigma,n,m))

