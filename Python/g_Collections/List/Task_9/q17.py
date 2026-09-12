prices = [100,760,450,120,280,800,1000,330]
print(prices)
for price in prices:
    if price>500:
        print(price,end=",")
prices.sort()
print("\nSecond highest price: ",prices[-2])