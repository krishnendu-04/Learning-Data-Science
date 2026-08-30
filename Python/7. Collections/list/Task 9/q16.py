seat =[12,25,8,2,15,17,11,9,4,6,13,20]
print(seat)
if 15 in seat:
    print("Seat No:15 is booked")
else:
    print("Seat No:15 is not booked")
seat.append(18)
print("Updated seats: ",seat)
seat.sort()
print("Sorted seats: ",seat)