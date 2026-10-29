list = input("enter numbers with space in between:- ")

Uni = sorted([int(x) for x in list.split()])
print(f"sorted array {Uni}\n")
n = len(Uni)
result = []
nes = []
for i in range(n):

    left = i+1
    right = n-1
    nes = []

    while left < right:
        nes = []
        total = Uni[left] + Uni[right] + Uni[i]
        if total == 0:
            nes.append(Uni[left])
            nes.append(Uni[right])
            nes.append(Uni[i])
            print("triplet found: ",nes)
            print(f"fixed number: {Uni[i]}  \nindice number: {i}")
            print()

            result.append(nes)


            right -= 1
            left += 1
            if left < right:
                break
        elif total < 0:
            left += 1
        elif total > 0:
            right -= 1



print(f"All triplets found:- {result}")








