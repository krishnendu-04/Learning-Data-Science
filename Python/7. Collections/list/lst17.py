sent = "Luminartechnolab"
vowels = "AEIOUaeiou"
consonants = []
for i in sent:
    if i not in vowels:
        consonants.append(i)
print(consonants)