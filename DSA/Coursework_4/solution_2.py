matrix = [[1,2,3,],
          [4,5,6],
          [7,8,9]]
target =6
cols = len(matrix[0])
rows = len(matrix)

current_point = matrix[0][cols-1]
print(current_point)
current_column = cols-1
current_row = 0

while current_row < rows and current_column >= 0:
    if current_point == target:
        print("Target: ",current_point)
        break
    elif current_point > target:
        current_point = matrix[current_row][current_column]
        current_column -= 1
    else:
        current_point = matrix[current_row][current_column]
        current_row += 1


