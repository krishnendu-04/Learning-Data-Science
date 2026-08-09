n = int(input("Enter the total number of workers: "))
for i in range(1,n+1):
    toys = int(input("Enter the number of toys produced: "))
    if toys>100:
        print("Worker ID: W00"+str(i))