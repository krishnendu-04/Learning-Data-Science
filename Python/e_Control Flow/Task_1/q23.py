bin = int(input("Enter the number in binary: "))
place = 0
dec = 0
while (bin>0):
    last = bin%10
    dec += (2**(place))*(last)
    place+=1
    bin//=10
print(dec)