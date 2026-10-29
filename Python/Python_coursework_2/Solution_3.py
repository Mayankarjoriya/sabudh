I = input("Enter an Integer for array with spaces in between:- ")
sum = int(input("Enter sum:- "))

uni = [int(i) for i in I.split()]

Number_of_pair = 0

for i in range(len(uni)):
    temp = uni[i]
    remaining = sum - temp
    starting_point = i + 1

    for j in range(starting_point, len(uni)):
        if i != j:
            if uni[j] == remaining:
                Number_of_pair += 1
                pair = (temp,uni[j])
                print(f"Pairs: {pair}")

print(f"Number of pairs: {Number_of_pair}")

