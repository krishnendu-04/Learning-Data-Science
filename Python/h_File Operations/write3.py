r1 = open("w2_fruits.txt","r")
w1 = open("w3_fruits_without_apple.txt","w")
for i in r1:
    if i!="Apple\n" and i!="Apple":
        w1.write(i)