words = ["level","python","madam","apple","radar","code","refer"]
print(words)
count = 0
longest = ""
for word in words:
    flag = True
    for i in range(len(word)):
        if word[i]!=word[-(i+1)]:
            flag = False
            break
    if flag==True:
        print(word)
        count+=1
        if len(word)>len(longest):
            longest = word
print("Number of palindrome words: ",count)
print("LOngest palindrome word: ",longest)