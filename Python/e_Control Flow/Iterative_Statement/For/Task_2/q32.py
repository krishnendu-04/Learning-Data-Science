n = int(input("Enter the number of forest zones: "))
for i in range(1,n+1):
    animals = int(input("Enter the number of animals spotted: "))
    if animals==0:
        print("Z00"+str(i))