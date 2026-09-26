words = ["hello","draw","in","yes","no","book","puzzle"]
lst = [word[::-1] for word in words if len(word)%2==0]
print(lst)