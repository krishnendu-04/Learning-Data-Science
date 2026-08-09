for i in range(1800,2025):
    if i%4==0:
        print(i,"is a leap year")
        if i%100==0:
            if i%400==0:
                print(i,"is a leap year")