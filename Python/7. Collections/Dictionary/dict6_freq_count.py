string = "ABCDCEFGABCKLU"
dict1 = {}
for i in string:
    if i not in dict1:
        dict1[i] = 1
    else:
        dict1[i]+=1
        print(i)
        break