reserved_seats = ("A1", "VIP-1", "B4", "VIP-2", "C12", "VIP-1", "D5")
print(reserved_seats)
count = 0
vip = "VIP"
for i in reserved_seats:
    if vip in i:
        count+=1
print("Number of VIP reserved seats: ",count)