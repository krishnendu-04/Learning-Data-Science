bus_seat = ["B","E","B","E","E","B","B","E"]
print(bus_seat)
booked = 0
for seats in bus_seat:
    if seats=="B":
        booked+=1
print("Booked seats: ",booked)

for i in range(len(bus_seat)):
    if bus_seat[i]=="E":
        bus_seat[i] = "B"
        break
print("Updated bus seats after booking first available seat: ",bus_seat)

for i in range(len(bus_seat)-1,-1,-1):
    if bus_seat[i]=="B":
        bus_seat[i] = "E"
        break
print("Updatde bus seats after cancelling the last available seat: ",bus_seat)