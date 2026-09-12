def shopping_categories():
    cust_a = {
        "Books",
        "Clothing",
        "Electronics",
        "Groceries",
        "Home Decor",
    }
    cust_b = {
        "Beauty",
        "Clothing",
        "Electronics",
        "Footwear",
        "Sports",
    }
    print("Common categories:\n ",cust_a.intersection(cust_b))
    print("Unique categories of customer A:\n ",cust_a-cust_b)
    print("Unique categories of customer B:\n ",cust_b-cust_a)
    print("All categories:\n ",cust_a.union(cust_b))

shopping_categories()