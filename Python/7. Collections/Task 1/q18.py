def library_books():
    books_dict = {
        101: "To Kill a Mockingbird",
        102: "1984",
        103: "The Great Gatsby",
        104: "Pride and Prejudice"
    }
    print(books_dict)
    search = int(input("Enter the ID of the book to search: "))
    if search in books_dict:
        print("Book found")
    else:
        print("Book not found")
    damaged = int(input("Enter the ID of the damaged book: "))
    del books_dict[damaged]
    print("Updated books after removing damaged ones: ",books_dict)
    print("\nAll available books: ")
    for i in books_dict:
        print(books_dict[i])

library_books()