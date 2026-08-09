n = int(input("Enter the number of samples: "))
for i in range(1,n+1):
    pH = float(input("Enter the pH of the sample: "))
    if 6.5<=pH<=8.5:
        pass
    else:
        print("S00"+str(i))