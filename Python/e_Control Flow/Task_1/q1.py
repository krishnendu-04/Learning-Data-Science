n = int(input("Enter the limit: "))
a = 0
b = 1
print(a,b,end=",")
for i in range(2,n):
    c = a+b
    print(c,end = ",")
    a = b
    b = c


#a,b = 0,1
#for i in range(n):
#print(a)
#a,b=b,a+b