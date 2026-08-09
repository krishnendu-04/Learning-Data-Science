num = int(input("Enter the number: "))
n = num
sq = n**2
sum = 0
while(sq>0):
    b = sq%10
    sum+=b
    sq//=10
if sum==num:
    print("Neon number")
else:
    print("Not neon number")