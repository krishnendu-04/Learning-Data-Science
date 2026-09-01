string = "ABCDCEFGABCKLU"
lst = []
for i in string:
    if i not in lst:
        lst.append(i)
    else:
        print(i)
        break