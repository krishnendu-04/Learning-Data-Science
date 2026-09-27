nums = [121,1234,90,565,43,21,787]
pal = list(map(lambda num:str(num),filter(lambda no:str(no)[::-1]==str(no),nums)))
print(pal)