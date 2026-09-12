def manage_cart(items):
    for i in items:
        print(i,end=",")
    items.append(input("\nAdd new item: "))
    print(items)
    unavailable = input("Enter an unavailable item to remove: ")
    if unavailable in items:
        items.remove(unavailable)
    print(items)
    print("Total number of items: ",len(items))

items = []
n = int(input("Enter the number of items: "))
for i in range(n):
    items.append(input("Enter the item: "))
manage_cart(items)