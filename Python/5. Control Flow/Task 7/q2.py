num = int(input("Enter the number: "))
flag = 0
if num<2:
    print("Not prime")
else:
    for i in range(2,num):
        if num%i==0:
            flag = 1
    if flag!=0:
        print("Not prime")
    else:
        print("Prime")