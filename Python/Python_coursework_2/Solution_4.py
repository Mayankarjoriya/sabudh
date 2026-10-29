
I = input("Enter Numbers for Choclates in a packet with spaces in between: ")
m = int(input("Enter the number of Students: "))

packets = [int(i) for i in I.split()]
packets.sort()
diff_list = []
selected_packet = []


for i in range(len(packets)):
    selected_packet.append(packets[i])
    

    for j in range(i+1, i+5):
        if i+5 < len(packets):
            selected_packet.append(packets[j])


        if len(selected_packet) == m:
            diff = max(selected_packet) - min(selected_packet)
            diff_list.append(diff)

            selected_packet =[]


print(f"Minimum Difference:  {min(diff_list)}")








