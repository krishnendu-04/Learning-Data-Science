n = int(input("Enter the number: "))
sq = n*n
sum = 0
while sq>0:
    digit = sq%10
    sum+=digit
    sq//=10
if sum==n:
    print("Neon Number")
else:
    print("Not Neon Number")