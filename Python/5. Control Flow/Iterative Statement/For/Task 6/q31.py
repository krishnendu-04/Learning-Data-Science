n = int(input("Enter the number of students: "))
for i in range(1,n+1):
    bricks = int(input("Enter the number of bricks: "))
    if bricks>500:
        print("Worker W00"+str(i)+" is eligible for productivity bonus")