books = ["Pride and Prejudice","Jane Eyre","The Great Gatsby","The Alchemist","The Hobbit","Fahrenheit 451","Jane Eyre","The Great Gatsby"]
print(books)
l1 =[]
print("Duplicate books are: ")
for book in books:
    if book not in l1:
        l1.append(book)
    else:
        print(book,end=',')
print("\nUnique books names: ",l1)