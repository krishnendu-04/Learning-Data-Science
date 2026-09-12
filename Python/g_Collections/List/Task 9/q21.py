products = ["Laptop", "Mouse", "Laptop", "Keyboard", "Mouse", "Monitor", "Printer"]
print(products)
unique = []
count = []
print("\nDuplicate product(s) are: ")
for product in products:
    if product not in unique:
        unique.append(product)
        count.append(products.count(product))
    else:
        print(product,end=',')
print("\n\nCount of each item:")
for i in range(len(unique)):
    print(unique[i],":",count[i])