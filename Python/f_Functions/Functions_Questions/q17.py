def table(num):
    for i in range(1,11):
        print(i,"X",num,"=",i*num)
n = int(input("Enter the number: "))
table(n)