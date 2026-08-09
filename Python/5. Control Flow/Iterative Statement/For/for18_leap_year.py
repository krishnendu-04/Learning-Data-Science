year = int(input("Enter the year: "))
flag = 0
if year%4==0:
    flag = 1
    if year%100==0:
        if year%400==0:
            flag = 1
        else:
            flag = 0
if flag==1:
    print("Leap year")
else:
    print("Not a leap year")