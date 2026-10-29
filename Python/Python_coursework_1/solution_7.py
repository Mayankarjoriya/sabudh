i = input("enter a numbers: ")

num_list = [int(x) for x in i.split(" ")]
filtered_list = []

for i in range( len(num_list)):
    if i == 0:
        continue
    elif i % 2 == 0:
        continue
    else:
        filtered_list.append(num_list[i])

print(filtered_list)