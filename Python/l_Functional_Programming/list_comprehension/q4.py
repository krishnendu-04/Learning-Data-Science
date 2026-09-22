string = "practice list comprehension problems to drill your head"
vowels = "aeiou"
#count vowels
lst1 = [i for i in string if i in vowels]
print("Number of vowels: ",len(lst1))