#find all words in a string that are less than 4 letters
string = "in 1984 there were 13 instance of a protest with over 1000 people attending"
lst = string.split()
lst1 = [i for i in lst if len(i)<4 and i.isalpha()]
print(lst1)