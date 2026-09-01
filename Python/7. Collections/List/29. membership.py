lst = [10,11,45,67,89,3,6,8]
n = int(input("Enter the element to search: "))
print("Found" if n in lst else "Not found")

"""
flag = 0
for i in lst:
    if i==n:
        flag = 1
        break
        
if flag==1:
    print("Item Found)
else:
    print("Item Not Found)
"""