import numpy as np


# =======Part-1 ==================================

a = np.random.randint(0,100, size=10)
b = np.random.randint(-10,10, size=(3,4))
b_flat = b.flatten()
a_copy = a.copy()
a_copy[0] = -1
c = np.array([a[i]  for i in range(len(a)) if i % 2 == 0])

print(f"1D array of length 10 containing integers between 0,100:  {a}")
print(f"2D array of size(3,4) containing integers between -10,10: {b}")
print(f"Flatten b array:                                          {b_flat}")
print(f"Copied array of a starting from -1 :                      {a_copy}")
print(f"1D array containg every second element of a from index 0:  {c}")


# =======Part-2 ==================================

print(f"Third element of a {np.array(a[2])}")
print(f"Last element of b {np.array(b[-1])}")
print(f"First Two rows and last two columns of b: {b[:2,-2:]}")
b_row = b[1:2]
b_col = b[:,0:1]
print(f"b_col : {b_col}")
print(f"b_row: {b_row}")




# =======Part-3 ==================================
d = np.random.randint(1,10,size=10)
e = d + a
b_double = np.multiply(2,b)

f = np.dot(b,b_double.T)

a_mean = np.mean(a)
b_mean = np.mean(b)
b_double_mean = np.mean(b)
g = np.array([a_mean,b_mean,b_double_mean])

print(f"1D array d: {d}")
print(f"element wise addition of d and a : {e}")
print(f"b multiply by 2: {b_double}")
print(f"array multiplcation of b and b_double Transpose : {f}")
print(f"Mean of array a,b and b_double : {g}")





# 4: Numpy array aggregation

# =======Part-3 ==================================

a_sum = np.sum(a)
b_min = np.min(b)
b_double_max = np.max(b)

print(f"Sum of all elements in a: {a_sum}")
print(f"Min of all elements in b : {b_min}")
print(f"Max of all element in b_double : {b_double_max}")