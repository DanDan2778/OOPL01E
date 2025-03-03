# LABORATORY 5
from tabulate import tabulate

class Book:
    def __init__(self, title, author, isbn, is_available = True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = is_available

    def borrow_book(self):
        print('\n'*50)
        self.is_available = False

    def return_book(self):
        self.is_available = True

class Library:
    def __init__(self):
        self.books = []
    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        print('\n'*50)
        print(tabulate([[book.title, book.author, book.isbn, "Available" if book.is_available else "Not Available"] for book in self.books], headers=["Title", "Author", "ISBN", "Availability"], tablefmt="fancy_grid"))

    def search_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

Book1 = Book("Harry Potter", "J.K. Rowling", "978-0439708180")
Book2 = Book("The Hobbit", "J.R.R. Tolkien", "978-0345534835")
Book3 = Book("The Da Vinci Code", "Dan Brown", "978-0307474278")
Book4 = Book("The Catcher in the Rye", "J.D. Salinger", "978-0316769488")
Book5 = Book("The Great Gatsby", "F. Scott Fitzgerald", "978-0743273565")

library = Library()
library.add_book(Book1)
library.add_book(Book2)
library.add_book(Book3)
library.add_book(Book4)
library.add_book(Book5)

while True:
    print("1. Display Books")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        library.display_books()
    elif choice == 2:
        title = input("Enter title: ")
        book = library.search_book(title)
        print('\n'*50)
        if book and book.is_available:
            book.borrow_book()
            print(f"{book.title} borrowed")
        elif book and not book.is_available:
            print(f"{book.title} is not available")
        else:
            print("Book not found")
    elif choice == 3:
        title = input("Enter title: ")
        book = library.search_book(title)
        print('\n'*50)
        if book and not book.is_available:
            book.return_book()
            print(f"{book.title} returned")
        elif book and book.is_available:
            print(f"{book.title} is already returned")
        else:
            print("Book not found")
    elif choice == 4:
        break
    else:
        print("Invalid choice")