lst = [(i,"poor") if i<=40 else (i,"average") if 41<=i<=60 else (i,"excellent") for i in range(1,101)]
print(lst)