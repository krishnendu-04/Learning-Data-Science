ordered = ["bat", "ball", "glove", "stumps", "helmet"]
returned = ["ball", "helmet"]
print("Ordered items: ",ordered)
print("Returned items: ",returned)
for i in returned:
    if i in ordered:
        ordered.remove(i)
print("Updated ordered items: ",ordered)