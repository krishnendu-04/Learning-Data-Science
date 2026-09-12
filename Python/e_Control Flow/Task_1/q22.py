n = int(input("Enter the number in decimal: "))
bin = 0
place = 1
while(n>0):
    rem = n%2
    bin = bin + rem*place
    place = place*10
    n//=2
print(bin)