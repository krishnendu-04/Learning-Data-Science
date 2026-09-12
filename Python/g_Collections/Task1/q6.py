def price_report(prices):
    prices.sort(reverse=True)
    print("Second highest price: ",prices[1])
    count = 0
    for i in prices:
        if i>1000:
            count+=1
    print("Count of prices above 1000: ",count)
    print("Prices in descending order: ",prices)

n = int(input("Enter the number of products: "))
prices = []
for i in range(n):
    prices.append(float(input("Enter the price of the product: ")))
price_report(prices)