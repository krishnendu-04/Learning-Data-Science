sentence = "This is a sample sentence"
print(sentence)
lst = [len(i) for i in sentence.split() if i[0] not in "aeiou"]
print(lst)