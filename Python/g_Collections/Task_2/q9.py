issued = [
    "Atomic Habits",
    "The Alchemist",
    "To Kill a Mockingbird",
    "1984",
    "Rich Dad Poor Dad"
]
returned = [
    "To Kill a Mockingbird",
    "Pride and Prejudice",
    "1984",
    "The Great Gatsby",
    "The Catcher in the Rye"
]
print("Issued books: ",issued)
print("Returned books: ",returned)
for i in returned:
    if i in issued:
        issued.remove(i)
print("Updated issued books: ",issued)