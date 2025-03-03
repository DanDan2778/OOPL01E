# LABORATORY 5
# tabulate for displaying the list of books in a table format
from tabulate import tabulate

# Book class
class Book:

# Initialize the Book class with title, author, isbn, and is_available
    def __init__(self, title, author, isbn, is_available = True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = is_available

# Borrow the book method
    def borrow_book(self):
        print('\n'*50)
        self.is_available = False

# Return the book method
    def return_book(self):
        self.is_available = True

# Library class
class Library:

# Initialize the Library class with books
    def __init__(self):
        self.books = []

# Add a book to the list of books
    def add_book(self, book):
        self.books.append(book)

# Display the list of books
    def display_books(self):
        print('\n'*50)
        print(tabulate([[book.title, book.author, book.isbn, "Available" if book.is_available else "Not Available"] for book in self.books], headers=["Title", "Author", "ISBN", "Availability"], tablefmt="fancy_grid"))

# Search for a book in the list of books
    def search_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

# Create Books
Book1 = Book("Harry Potter", "J.K. Rowling", "978-0439708180")
Book2 = Book("The Hobbit", "J.R.R. Tolkien", "978-0345534835")
Book3 = Book("The Da Vinci Code", "Dan Brown", "978-0307474278")
Book4 = Book("The Catcher in the Rye", "J.D. Salinger", "978-0316769488")
Book5 = Book("The Great Gatsby", "F. Scott Fitzgerald", "978-0743273565")

# Add Books to the Library
library = Library()
library.add_book(Book1)
library.add_book(Book2)
library.add_book(Book3)
library.add_book(Book4)
library.add_book(Book5)

# Displays a menu for the user to choose from
while True:
    print(tabulate([[1, "Display Books"], [2, "Borrow Book"], [3, "Return Book"], [4, "Exit"]], headers=["Menu"], tablefmt="orgtbl"))
    choice = int(input("Enter choice: "))

    if choice == 1:
        library.display_books() # Display the list of books
    elif choice == 2: # Borrow a book
        title = input("Enter title: ") # Ask the user to enter the title of the book
        book = library.search_book(title) # Search for the book
        print('\n'*50)
        if book and book.is_available: # If the book is found and is available
            book.borrow_book() # Borrow the book and prints that the book is borrowed
            print(f"{book.title} borrowed")
        elif book and not book.is_available: # If the book is found but is not available
            print(f"{book.title} is not available") # Print that the book is not available
        else: # If the book is not found and tells the user that the book is not in the library
            print("Book not found")
    elif choice == 3: # Return a book
        title = input("Enter title: ")  # Ask the user to enter the title of the book and look for the book in the library
        book = library.search_book(title)
        print('\n'*50)
        if book and not book.is_available: # If the book is found and is not available, change the status of the book to available
            book.return_book()
            print(f"{book.title} returned")
        elif book and book.is_available: # If the book is found and is available, print that the book is already returned
            print(f"{book.title} is already returned")
        else: # If the book is not found, print that the book is not found
            print("Book not found")
    elif choice == 4: # Exit the program
        break
    else: # If the user enters an invalid choice, print that the choice is invalid
        print("Invalid choice")