n = int(input("Enter the number: "))
num = n
sq = n*n
count = 0

while(n>0):
    count+=1
    n//=10

pow = 10 ** count

if sq%pow == num:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")