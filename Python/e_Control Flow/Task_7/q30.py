n = int(input("Enter the number: "))

#OddOrEven
if n%2==0:
    print("Even")
else:
    print("Odd")

#PrimeOrNotPrime
if n<2:
    print("Not prime")
else:
    flag = 0
    for i in range(2,n):
        if n%i==0:
            flag = 1
            break
    if flag==0:
        print("Prime")
    else:
        print("Not prime")

#PalindromeOrNot
rev = 0
a = n
while(a>0):
    last1 = a%10
    rev = rev*10 + last1
    a//=10
if n==rev:
    print("Palindrome")
else:
    print("Not Palindrome")

#Armstrong
sum1 = 0
b = n
while(b>0):
    last2 = b%10
    sum1 += last2**(len(str(n)))
    b//=10
if n==sum1:
    print("Armstrong")
else:
    print("Not Armstrong")

#Strong
sum2 = 0
c = n 
while(c>0):
    last3 = c%10
    fact = 1
    for i in range(1,last3):
        fact*=i
    sum2+=fact
    c//=10
if sum2==n:
    print("Strong Number")
else:
    print("Not Strong Number")

#HarshadsNumber
sum3 = 0
d = n
while(d>0):
    last4 = d%10
    sum3+=last4
    d//=10
if n%sum3==0:
    print("Harshads Number")
else:
    print("Not Harshads Number")