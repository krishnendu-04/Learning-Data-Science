store_a = (101, 102, 103, 104, 105, 106)
store_b = (201, 102, 203,105,202)
print(store_a)
print(store_b)
merge = store_a+store_b
print("After merging: ",merge)
seen = []
dupli = []
for i in merge:
    if i in seen:
        dupli.append(i)
    else:
        seen.append(i)
print("\nDuplicate IDs: ",dupli)