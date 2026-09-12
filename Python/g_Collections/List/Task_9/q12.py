purchased_products = ["Mobile","TV","Speaker","Mouse","CPU"]
print(purchased_products)
if "Laptop" in purchased_products:
    print("Laptop found")
else:
    print("Laptop not found")
purchased_products.extend(["Laptop","Headphone"])
print(purchased_products)
purchased_products.remove("Mouse")
print(purchased_products)
