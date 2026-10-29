i = input("enter numbers")

num_list = [int(x) for x in i.split()]

filtered_list = []

for j in num_list:
   if j%5 == 0:
      if j > 500:
         break
      elif j > 150:
         continue
      else:
         filtered_list.append(j)
   else:
      print("invalid input")

print(filtered_list)
