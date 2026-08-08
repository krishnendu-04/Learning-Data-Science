secret = 121
guess = int(input("Guess the secret number: "))
attempts=1
while guess!=secret:
    attempts+=1
    guess = int(input("Guess the secret number: "))
print("Number of guesses: ",attempts)