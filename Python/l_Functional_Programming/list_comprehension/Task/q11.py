numbers = [i for i in range(1,31)]
print(numbers)
lst1 = ["FizzBuzz" if i%15==0 else "Fizz" if i%3==0 else "Buzz" if i%5==0 else i for i in numbers]
print(lst1)