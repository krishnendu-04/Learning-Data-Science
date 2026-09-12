def prime_range(lower, upper):
    for i in range(lower,upper+1):
        if i<2:
            continue
        else:
            flag = 1
            for j in range(2,i):
                if i%j==0:
                    flag = 0
                    break
            if flag==1:
                print(i)
low = int(input("Enter the lower range: "))
up = int(input("Enter the upper range: "))
prime_range(low, up)