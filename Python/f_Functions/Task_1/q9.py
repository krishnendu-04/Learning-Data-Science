import math
def statistics_report(data):
    mean = sum(data) / len(data)
    print("Mean: ",mean)
    diff=0
    for i in data:
        diff += (i - mean)**2
    var = (diff)/len(data)
    print("Variance: ",var)
    std = math.sqrt(var)
    print("Standard Deviation: ",std)
    data
    data_range = max(data) - min(data)
    print("Range: ",data_range)
    data.sort()
    if len(data)!=0:
        if len(data)%2!=0:
            median = data[len(data)//2]
            print("Median: ",median)
        else:
            median = (data[len(data)//2 - 1] + data[len(data)//2]) /2 
            print("Median: ",median)

n = int(input("enter the number of elements in the list: "))
data =[]
for i in range(n):
    data.append(int(input("enter the element: ")))
statistics_report(data)