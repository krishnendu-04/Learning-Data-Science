prices = [100, 250, 75, 500]
discounted = list(map(lambda price:price-price*.10,prices))
print(discounted)