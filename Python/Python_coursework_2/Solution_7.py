import random

n = int(input("Enter Number of rows:- "))
m = int(input("Enter Number of columns:- "))

matrix = []

for i in range(n):
    row =[]

    for j in range(m):
        row.append(random.randint(1,9))
    matrix.append(row)

print(f"Original Matrix:- {matrix}")

def rotate_matrix(matrix):
    transpose = [list(row) for row in zip(*matrix)]

    for row in transpose:
        row.reverse()

    return transpose


print(f"\n90 degree clockwise Rotated Matrix:- {rotate_matrix(matrix)}")
