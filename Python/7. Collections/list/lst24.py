lst = ["apple","orange","banana"]
#.append(element) ----> adds the element to the end of the list
lst.append("pappaya")
#.extend(list) ----> adds multiple element to the end of the list
lst.extend(["blueberry","cherry"])
#.insert(pos,element) ----> adds the 2nd mentioned object to the first mentioned position of the list
lst.insert(1,"mango")
print(lst)
#.remove(element) ----> removes the mentioned element from the beginning of the list
lst.remove("banana")
#.pop() ----> gets the last element of the list and removes it from the list
lst.pop()
#.pop(index) ----> removes the element from the mentioned position
lst.pop(1)
print(lst)
#.index(element) ----> retreives the index of the element
print(lst.index("orange"))
#.reverse() ----> reverses the list
lst.reverse()
print(lst)
#.sort()/.sort(reverse=True) ----> reverses the list in ascending/descending order
lst.sort()
lst.append("apple")
print(lst)
#sum(lst) ----> returns the sum of the elements in the list
#min(lst) ----> returns the minimum value in the list
#max(lst) ----> returns the maximum value in the list
#len(lst) ----> returns the length of the list
#.count(element) ----> returns the count of the mentioned element
print(lst.count("apple"))
#.copy() ----> copies the list 
fruits = lst.copy()
print(fruits)
#.clear() ----> empties the list
lst.clear()
print(lst)