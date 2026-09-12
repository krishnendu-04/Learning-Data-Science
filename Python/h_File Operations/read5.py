file = open("r5.txt","r")
word = {}
for i in file:
    if i.rstrip("\n") not in word:
        word[i.rstrip("\n")] = 1
    else:
        word[i.rstrip("\n")]+=1
print(word)
for key,value in word.items():
    print(key,":",value)