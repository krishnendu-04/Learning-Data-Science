sentence = "cat dog cat dog rat bat cat dog rat bat rat"
lst = sentence.split()
dict1={}
for i in lst:
    if i not in dict1:
        dict1[i] = 1
    else:
        dict1[i]+=1
print(dict1)