visitors = [600,990,1200,3000,830,500,2400]
print(visitors)
count = 0
for visitor in visitors:
    if visitor>1000:
        count+=1
print("Number of days with more than 1000 visitors: ",count)
print("Busiest day: ",visitors.index(max(visitors))+1)