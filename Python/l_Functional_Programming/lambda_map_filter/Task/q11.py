words = ["world","longer","in","hierarchy","cat","because","withstand"]
filtered = list(filter(lambda word:len(word)>5,words))
print(filtered)