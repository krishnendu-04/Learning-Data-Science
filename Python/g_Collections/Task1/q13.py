def laptop_info():
    laptop_specs = ("Dell", "XPS 13", 13.4, "Intel Core i7", "16GB", "512GB SSD", 1199.99)
    for i in laptop_specs:
        print(i)
    print("RAM: ",laptop_specs[4])
    print("Price: ",laptop_specs[-1])

laptop_info()