class Book:
    def __init__(self, _title, author, isbn):
        self.title = _title
        self.author = author
        self.isbn = isbn
        self.status = True

    def Status(self):
        if self.status == 1:
            return "Available"
        else:
            return "Not available"
    def borrow_book(self):
        if self.status == 1:
            self.status = 0
            return "Book has been borrowed"
        else:
            print("Book is not available for borrowing")

    def return_book(self):
        if self.status == 0:
            self.status = 1
            return "Book has been returned"
        else:
            print("Book is not borrowed")

class Library:
    def __init__(self):

        self.books = []
    def add_book(self):
        t = input("Enter the title of the book: ")
        author = input("Enter the author of the book: ")
        isbn = input("Enter the ISBN of the book: ")
        self.books.append(Book(t, author, isbn))

    def display_books(self):
        for b in self.books:
            print(f"Title: {b.title}, Author: {b.author}, ISBN: {b.isbn}, Status: {b.status}")


    def search_book(self):
        t = input("Enter the title of the book: ")
        for b in self.books:
            if b.title == t:
                print(f"Title: {b.title}, Author: {b.author}, ISBN: {b.isbn}, Status: {Book().status()}")
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
    else:
        print("Invalid choice")



