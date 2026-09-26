string = "appu123789@gmail.com"
print(string)
digits = [i for i in string if i.isdigit()]
letters = [i for i in string if i.isalpha()]
spcl = [i for i in string if not i.isalnum() and i!=" "]
print(digits)
print(letters)
print(spcl)