I = input("Enter number with spaces in between: ")

uni = [int(x) for x in I.split()]

for i in range(1, len(uni)):
    if uni[i] < 0:
        temp = uni[i]
        j = i

    while j >0 and uni[j-1] >= 0:
        uni[j] = uni[j-1]
        j -= 1

    uni[j] = temp

print(uni)