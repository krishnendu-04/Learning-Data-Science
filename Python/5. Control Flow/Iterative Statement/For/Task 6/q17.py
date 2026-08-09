n = int(input("Enter the total number of volunteers: "))
for i in range(1,n+1):
    trees = int(input("Enter the number of trees planted: "))
    if trees>=20:
        print("Volunteer ID: V00"+str(i))