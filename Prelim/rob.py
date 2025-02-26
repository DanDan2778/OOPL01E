class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = "Available"

    def borrow_book(self):
        if self.status == "Available":
            self.status = "Borrowed"
        else:
            print("Book is not available for borrowing")

    def return_book(self):
        if self.status == "Borrowed":
            self.status = "Available"
        else:
            print("Book is not borrowed")

class Library:
    def __init__(self):

        self.books = []
    def add_book(self):
        title = input("Enter the title of the book: ")
        author = input("Enter the author of the book: ")
        isbn = input("Enter the ISBN of the book: ")
        self.books.append(Book(title, author, isbn))

    def display_books(self):
        for book in self.books:
            print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}, Status: {book.status}")


    def search_book(self):
        title = input("Enter the title of the book: ")
        for book in self.books:
            if book.title == title:
                print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}, Status: {book.status}")
                return
        print("Book not found")

library = Library()
while True:
    choice = int(input("1: Add a book\n2: Display books\n3: Search for a book\n4: Borrow a book\n5: Return a book\n6: Exit \nEnter the number of your choice:"))
    if choice == 1:
        library.add_book()
    elif choice == 2:
        library.display_books()
    elif choice == 3:
        library.search_book()
    elif choice == 4:
        title = input("Enter the title of the book: ")
        for book in library.books:
            if book.title == title:
                book.borrow_book()
                break
        else:
            print("Book not found")
    elif choice == 5:
        title = input("Enter the title of the book: ")
        for book in library.books:
            if book.title == title:
                book.return_book()
                break
        else:
            print("Book not found")
    elif choice == 6:
        break



